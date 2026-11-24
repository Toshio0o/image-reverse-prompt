#!/usr/bin/env python3
"""从本地图片按像素提取主色卡（6 色带百分比），供图像反推 skill 使用。

用法：
  python3 extract_palette.py <图片路径> [--colors N] [--json]

方法：缩放到最长边 200 像素后转到 LAB 色彩空间做 k-means 聚类
（固定随机种子，结果可复现），按像素占比排序；再合并色差
Delta E 小于 8 的近似色，避免浅灰背景之类的大面积纯色占掉
多个槽位。LAB 聚类比 RGB 更符合人眼对颜色的区分，深绿墙面
和深棕裤子这类 RGB 距离很近的颜色也能分开。角色按占比分配：
最大为“主色”，第二为“辅色”，其余为“辅助色”，占比低于 5% 的
为“点缀色”。

依赖 Pillow 加 numpy，不联网，不写文件。2026-11-24 实测：红墙图
主色砖红 #9B5849 占 40.4%，绿马甲图主色深棕灰 #2E241F 占 27.0%，
衬衫米白 #DBD0C0 占 10.2%，与目测主色一致；低明度下墙面绿与深
棕的聚类边界可能有出入。数值是参考级，不是像素级精确。
"""

import argparse
import json
import sys

import numpy as np
from PIL import Image

SEED = 42
MERGE_DELTA_E = 8


def rgb_to_lab(rgb):
    """sRGB（0 到 255）转 CIE LAB，D65 白点。"""
    srgb = rgb / 255.0
    linear = np.where(
        srgb <= 0.04045, srgb / 12.92, ((srgb + 0.055) / 1.055) ** 2.4
    )
    m = np.array(
        [
            [0.4124, 0.3576, 0.1805],
            [0.2126, 0.7152, 0.0722],
            [0.0193, 0.1192, 0.9505],
        ]
    )
    xyz = linear @ m.T
    xyz /= np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, xyz ** (1 / 3), 7.787 * xyz + 16 / 116)
    lab = np.empty_like(f)
    lab[:, 0] = 116 * f[:, 1] - 16
    lab[:, 1] = 500 * (f[:, 0] - f[:, 1])
    lab[:, 2] = 200 * (f[:, 1] - f[:, 2])
    return lab


def lab_to_rgb(lab):
    """CIE LAB 转 sRGB（0 到 255），D65 白点。"""
    f = np.empty_like(lab, dtype=float)
    f[:, 1] = (lab[:, 0] + 16) / 116
    f[:, 0] = lab[:, 1] / 500 + f[:, 1]
    f[:, 2] = f[:, 1] - lab[:, 2] / 200
    xyz = np.where(
        f**3 > 0.008856, f**3, (f - 16 / 116) / 7.787
    ) * np.array([0.95047, 1.0, 1.08883])
    m = np.array(
        [
            [3.2406, -1.5372, -0.4986],
            [-0.9689, 1.8758, 0.0415],
            [0.0557, -0.2040, 1.0570],
        ]
    )
    linear = xyz @ m.T
    srgb = np.where(
        linear <= 0.0031308, 12.92 * linear, 1.055 * linear ** (1 / 2.4) - 0.055
    )
    return np.clip(np.round(srgb * 255), 0, 255).astype(int)


def kmeans(points, k, iterations=15):
    rng = np.random.default_rng(SEED)
    first = rng.integers(len(points))
    centers = [points[first]]
    closest = np.sum((points - centers[0]) ** 2, axis=1)
    for _ in range(1, k):
        probs = closest / closest.sum()
        idx = rng.choice(len(points), p=probs)
        centers.append(points[idx])
        dist = np.sum((points - points[idx]) ** 2, axis=1)
        closest = np.minimum(closest, dist)
    centers = np.array(centers, dtype=float)
    for _ in range(iterations):
        dist = ((points[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)
        labels = dist.argmin(axis=1)
        new_centers = centers.copy()
        for j in range(k):
            members = points[labels == j]
            if len(members):
                new_centers[j] = members.mean(axis=0)
        if np.allclose(new_centers, centers):
            break
        centers = new_centers
    return centers, labels


def extract_palette(path, n_colors=6, max_side=200):
    img = Image.open(path).convert("RGB")
    img.thumbnail((max_side, max_side), Image.LANCZOS)
    pixels = np.asarray(img, dtype=float).reshape(-1, 3)
    lab = rgb_to_lab(pixels)
    centers, labels = kmeans(lab, n_colors)
    total = len(pixels)
    groups = []
    for j in range(n_colors):
        count = int((labels == j).sum())
        if count:
            groups.append([centers[j], count])
    groups.sort(key=lambda g: g[1], reverse=True)
    merged = []
    for center, count in groups:
        for m in merged:
            if np.linalg.norm(center - m[0]) < MERGE_DELTA_E:
                m[0] = (m[0] * m[1] + center * count) / (m[1] + count)
                m[1] += count
                break
        else:
            merged.append([center, count])
    merged.sort(key=lambda m: m[1], reverse=True)
    rgb_centers = lab_to_rgb(np.array([m[0] for m in merged]))
    colors = []
    for rank, ((_, count), (r, g, b)) in enumerate(zip(merged, rgb_centers)):
        share = round(count / total * 100, 1)
        if rank == 0:
            role = "主色"
        elif rank == 1:
            role = "辅色"
        elif share < 5:
            role = "点缀色"
        else:
            role = "辅助色"
        colors.append(
            {"hex": "#%02X%02X%02X" % (r, g, b), "share": share, "role": role}
        )
    return colors


def main():
    parser = argparse.ArgumentParser(description="提取图片主色卡")
    parser.add_argument("image", help="图片路径")
    parser.add_argument("--colors", type=int, default=6, help="颜色数，默认 6")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args()
    try:
        colors = extract_palette(args.image, args.colors)
    except (OSError, ValueError) as exc:
        print(f"读取图片失败：{exc}", file=sys.stderr)
        sys.exit(1)
    if args.json:
        print(json.dumps(colors, ensure_ascii=False, indent=2))
    else:
        for c in colors:
            print(f"{c['hex']} {c['role']} {c['share']}%")


if __name__ == "__main__":
    main()
