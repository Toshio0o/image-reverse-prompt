# 反推实测范例

前两例来自 2026-11-24 人像实测（两张街拍），后三例来自同日 skill 建成后的通用层实测（风景、建筑、产品，Unsplash 公开图）。每例都按 skill 五步流程走完，元数据为精简版，完整字段见 `schema.md`。

## 例 1：人像，红墙橙帽行走（c2-cityboy-redwall.jpg）

- 类型：portrait。2026-11-24 人像实测第一张（街拍）。
- 元数据要点：主体为黑人男性全身、侧面行走、身体朝右；服装分层为橙色棒球帽、橄榄绿细格纹短夹克、白衬衫、淡黄 T 恤、棕色宽腿长裤、黑白低帮帆布鞋；左手提米白帆布托特包；背景为砖红粗糙墙面加灰混凝土基座加沥青路面，墙脚有潮湿污痕。
- 核验教训：首版三处错（行走方向说反、双手插兜、托特包认成折叠伞），本例中文提示词为修正后版本。
- 中文提示词：低饱和复古街拍、柔和自然光、轻微胶片颗粒、真实城市环境纹理。真人摄影，全身男性街头穿搭，年轻年龄感，深棕色肤调，身形高挑偏瘦，侧身向右行走，头部略低，帽檐遮住部分眼部，右手插在外套口袋，左手提米白帆布托特包，左腿向后迈步、右腿承重，姿态松弛自然。穿橙红色棒球帽，帽面带小型白色标志，橄榄绿色细格纹宽松夹克，露出白色衬衫和淡黄 T 恤，棕色宽腿长裤，黑白低帮帆布鞋。人物位于画面中央偏右，完整呈现头部至鞋底，背景是大面积粗糙砖红色涂层墙面，下方接浅灰混凝土基座和灰色沥青路面，墙脚带深色潮湿污痕；平视略低机位，整体暖中性低饱和配色，保留真实皮肤阴影、墙面纹理和轻微抓拍感，避免棚拍摆姿和过度精修。
- 英文提示词：Full-body street style photograph of a Black man walking in mid-stride, side profile facing right, head slightly lowered, one foot lifted off the ground. He wears an orange baseball cap with a small white logo, an olive-green fine-checked overshirt jacket layered over a white collared shirt and pale yellow t-shirt, brown wide-leg trousers, black low-top canvas sneakers with white soles, carrying a beige canvas tote bag in his left hand. Background is a textured rust-red terracotta wall above a grey concrete base, asphalt ground. Overcast soft diffused daylight, muted film tones, candid City Boy street photography, vertical composition, eye-level shot.
- 色卡（脚本实测）：#9B5849 主色 40.4%；#928A81 辅色 21.1%；#B6AFA9 辅助色 17.7%；#302019 辅助色 10.5%；#5D4C3D 辅助色 9.8%；#DA6F50 点缀色 0.5%。

## 例 2：人像，绿马甲喝咖啡（b1-amvint-greenvest.jpg）

- 类型：portrait。2026-11-24 人像实测第二张（街拍）。
- 元数据要点：年轻东亚男性全身正面站立，右手举白色纸杯喝水遮住口鼻，左手插裤袋；服装分层为黑色报童帽、黑框眼镜、白衬衫（袖口挽起）、棕色花纹领带、橄榄绿 V 领格纹针织马甲、棕色皮带、深棕宽腿长裤、棕色皮鞋；腰间钥匙串、左肩透明印花托特包、手腕细手链；背景为深绿釉面砖墙、白色管道、顶部空调外机。
- 核验要点：配饰逐件齐全（眼镜、手链首版漏了，本例已补）；纸杯遮脸动作明确，防错提示写避免把遮脸改成露完整面部。
- 中文提示词：复古低饱和街拍、轻微柔焦与细颗粒手机快照质感。真人摄影，全身年轻男性居中略偏左站在深绿灰色小砖墙前，画面从黑色平檐帽到棕色鞋完整收进；一手举白色纸杯饮水遮住口鼻，一手插裤袋，脸部大部分被帽檐和纸杯遮挡，姿态随意松弛。身形高挑偏瘦、肩窄腿长，穿白色宽松长袖衬衫、橄榄绿粗针织背心、暗红棕领带、宽松深棕长裤与棕色皮带，裤腿在鞋面自然堆褶；肩侧挂彩色印花布袋，腰侧垂着小钥匙饰物，戴黑框眼镜、手腕有细手链。柔和阴天漫射光，浅肤色保留自然暖米色，整体以深绿灰、橄榄绿、白与棕色构成低饱和复古色调。背景保留砖墙、金属管线和上方浅色设备结构，略微柔化但不压过人物；衣物纹理和全身轮廓清楚可辨，避免裁掉鞋部或把纸杯遮脸动作改成露出完整面部。
- 英文提示词：Full-body vintage street style photograph of a young East Asian man standing front-facing, drinking from a white paper cup held to his mouth, the cup partially covering his lower face. He wears a black newsboy cap, black-framed glasses, a white shirt with rolled sleeves, a patterned brown tie, an olive-green V-neck checked knit vest, a brown leather belt with a keychain hanging from the loop, dark brown wide-leg trousers and brown leather shoes, a translucent printed tote bag on his shoulder and a thin bracelet. Background is a dark green glazed brick wall with white pipes and air conditioning units above. Soft daylight, muted retro film tones, American vintage City Boy style, vertical composition, eye-level shot.
- 色卡（脚本实测）：#2E241F 主色 27.0%；#434035 辅色 26.8%；#655E4E 辅助色 22.5%；#8D8372 辅助色 11.5%；#DBD0C0 辅助色 10.2%；#815441 点缀色 2.0%。

## 例 3：风景，高山云海日出（Unsplash photo-1506905925346）

- 类型：landscape。
- 元数据：图像类型为真人摄影（风光摄影）；氛围壮阔宁静、低角度暖金色阳光；横幅、平视略高机位、雪山居左、云海占下半幅、天空占上半幅；光线为低角度暖光、金色洒在雪峰、冷暖对比；色彩为冷蓝灰云海加暖粉橙天空加雪白峰顶；成像清晰锐利、远景带大气透视雾感；风格为高山风光摄影；防错为避免把云海写成水面、避免雪山比例失调。地貌为高山雪峰群、连绵山脊、山谷云海；天气晴朗、山谷云海翻涌；时间为日出或日落（低角度暖光，画面无法确定是日出还是日落）、高海拔常年积雪；景深为前景近处岩石山脊、中景云海、远景雪峰与天际线；自然细节为雪峰棱角分明、积雪覆盖山脊线、云海如棉絮翻滚；人为元素无。
- 核验要点：确认下半幅是云海不是水面；日出还是日落无法从画面确定，写日出或日落，不直接断言；前景岩石与远景雪峰层次分清。
- 中文提示词：壮阔高山风光、低角度暖金色阳光。横幅摄影，雪峰群立于云海之上，主峰居左棱角分明、积雪覆盖山脊；下半幅为翻涌的云海如棉絮铺满山谷，前景为近处深色岩石山脊；天空由粉橙渐变为淡蓝，暖金色阳光洒在雪峰顶，冷暖对撞。远景带大气透视雾感，画面清晰锐利。避免把云海写成水面。
- 英文提示词：Majestic alpine landscape photograph at sunrise or sunset, snow-capped peaks rising above a sea of clouds. A sharp pyramidal summit stands left of center, its ridges covered in snow and lit gold by the low sun; below, a thick blanket of clouds fills the valley like rolling cotton, with a dark rocky ridge in the foreground. The sky gradients from warm pink-orange at the horizon to pale blue above. Clear and sharp with soft atmospheric haze in the distance, cool blue-grey tones against warm sunlight, wide horizontal composition, eye-level view from a high vantage point.
- 色卡（脚本实测）：#5D6C8A 主色 24.4%；#36435A 辅色 21.2%；#1B2029 辅助色 19.4%；#9C9CB1 辅助色 19.3%；#E4BAA4 辅助色 8.8%；#8B747D 辅助色 6.8%。

## 例 4：建筑，白色解构主义建筑（Unsplash photo-1487958449943）

- 类型：architecture。
- 元数据：图像类型为真人摄影（建筑摄影）；氛围冷峻、现代、几何感强；横幅、低角度仰拍、建筑占右半幅、天空占左上；光线为白天柔和漫射光、浅蓝天、轻微云层；色彩为白色加浅灰蓝为主、黑窗框线条点缀、低饱和冷调；成像清晰锐利、瓷砖网格纹理清楚；风格为现代解构主义建筑摄影；防错为避免把几何体块写对称、避免加暖色。建筑类型为文化建筑、解构主义现代建筑；结构为倾斜的白色金字塔体块加三角形玻璃幕墙加横向长方体基座，体块穿插、非对称；材料为白色瓷砖贴面（菱形网格）、玻璃幕墙（黑框网格）、混凝土基座；开口为三角形玻璃幕墙大面积开窗、顶部方形小窗、底层横向条窗；环境为右侧远处白色低层建筑、街灯、少量树木；视角为低角度仰拍、轻微透视上收。
- 核验要点：确认体块非对称（金字塔倾斜、玻璃幕墙只在左侧）；确认仰拍不是平视；确认瓷砖是菱形网格不是方形。
- 中文提示词：冷峻现代解构主义建筑摄影。横幅低角度仰拍，白色几何体块建筑占右半幅：倾斜的金字塔形塔楼贴白色菱形瓷砖，左侧接三角形玻璃幕墙（黑框网格），下方为横向长方体基座带条形窗；浅蓝天带薄云，右侧远处有白色低层建筑与黑色街灯。白色加浅灰蓝低饱和冷调，瓷砖网格纹理清晰。避免把体块写对称。
- 英文提示词：Modern deconstructivist architecture photograph, low-angle view. A white geometric building fills the right half of the frame: a leaning pyramid tower clad in white diamond-patterned tiles, joined to a triangular glass curtain wall with a black grid frame, above a horizontal rectangular base with strip windows. Pale blue sky with thin clouds; white low-rise buildings and a black street lamp in the distance on the right. Low-saturation cool palette of white and pale blue-grey, crisp tile grid texture, wide horizontal composition.
- 色卡（脚本实测）：#EAEEF1 主色 50.7%；#C5D2DA 辅色 19.2%；#A7B7C1 辅助色 18.7%；#6A7D86 辅助色 7.0%；#374246 点缀色 4.4%。

## 例 5：产品，白色智能手表（Unsplash photo-1523275335684）

- 类型：product。
- 元数据：图像类型为产品渲染图（观感偏 3D 渲染）；氛围极简、干净、科技感；横幅、俯拍微斜、两只表对角线排列、右侧手表被画面右边缘部分裁切、中间保留大面积留白；光线为柔和均匀影棚光、轻微投影、无硬阴影；色彩为白色加浅灰为主、黑色表盘是唯一深色点缀；成像光滑哑光、轻微渐变阴影、画面极干净；风格为极简主义产品渲染；防错为避免给表盘加图案或文字、避免加背景杂物、避免把被裁切的右表画完整。产品主体为智能手表两只，一只正面朝上（黑色圆形表盘）、一只背面朝上（白色圆形表背）；材质为白色哑光硅胶表带、白色金属表壳、黑色玻璃表盘；品牌标识文字无（表盘与表背均无文字 logo）；摆放为对角线平铺、左下到右上、表带自然伸展；背景为浅灰纯色、无道具；光影为顶部柔和漫射光、表身下方轻微投影；细节特写为表带调节孔、表扣、表耳连接处。
- 核验要点：确认两只表、一正一反（不是同一只的两个角度拼图）；确认表盘与表背均无文字；确认右表是否被边缘裁切、中间留白；表带孔数不用精确数，写调节孔清晰即可。
- 中文提示词：极简智能手表产品渲染。横幅俯拍微斜，两只白色智能手表对角线平铺在浅灰纯色背景上，中间保留大面积留白：一只正面朝上、黑色圆形表盘无任何图案文字，一只背面朝上、白色圆形表背，右侧手表被画面右边缘部分裁切；白色哑光硅胶表带自然伸展，表带调节孔与表扣清晰。顶部柔和漫射光，表身下方轻微投影。白色加浅灰为主，黑色表盘是唯一深色点缀。避免给表盘加图案或文字、避免加背景杂物、避免把被裁切的右表画完整。
- 英文提示词：Minimalist smartwatch product render, top-down view at a slight angle. Two white smartwatches lie diagonally on a plain light-grey background with large empty space in the middle: one face-up with a black round display showing no pattern or text, one face-down showing a white round case back, the right watch partially cropped by the right edge of the frame. Matte white silicone straps extend naturally, with adjustment holes and buckles clearly visible. Soft even studio lighting with gentle shadows beneath the watches. Predominantly white and light grey, the black display the only dark accent, wide horizontal composition.
- 色卡（脚本实测）：#D9D9D9 主色 92.7%；#B4B4B4 辅色 2.8%；#979797 点缀色 1.9%；#282828 点缀色 1.9%；#717171 点缀色 0.7%。

## 例 6：室内，现代波西米亚风客厅（Unsplash photo-1616486338812）

- 类型：interior。2026-11-24 skill 基准版；核验时补了浅灰绿墙面、坐姿视线机位与窗外庭院，圆形针织蒲团为关键陈设不可漏。
- 元数据：图像类型为室内摄影（观感偏 3D 渲染）；氛围温暖、明亮、现代波西米亚风，轻松居家；横幅、平视（机位约与坐姿视线齐平）、客厅全景、沙发居右、装饰墙居左、窗户在右；光线为右侧窗户自然光、明亮均匀、轻微阴影；色彩为米白、浅灰、暖木色为主，墙面带浅灰绿，绿植点缀，低饱和暖中性；成像清晰锐利、织物纹理细腻；风格为现代波西米亚风室内设计；防错为避免把装饰墙画错成纯色墙、避免漏掉牛头骨装饰。空间类型为客厅；布局为 L 形沙发靠右墙、茶几居中、单人椅在左、装饰墙在左墙、窗户在右墙，动线开阔；家具为米白 L 形布艺沙发（右侧带贵妃榻）、圆形双层木质茶几、藤编单人椅、圆形针织蒲团、黑色小边桌；材质配色为米白布艺、浅木色、藤编、针织，配色米白加浅灰加暖木色；灯光为右侧大窗自然光、窗帘米色、光线明亮均匀，窗外可见绿色庭院；装饰细节为牛头骨挂饰（黑色长角）、圆形编织挂毯、流苏挂毯、多幅画框（牛肖像、几何图案）、圆形大挂钟（白底黑字）、绿植（茶几、角落、墙面挂盆）、抱枕多件、搭毯，最左侧有一扇白色房门。
- 核验要点：确认沙发是 L 形、贵妃榻在右侧；确认牛头骨在左墙高处；确认挂钟在后墙；确认窗户在右侧；确认茶几是双层圆形木质；确认蒲团是圆形针织；确认墙面颜色（浅灰绿）和窗外景观。
- 中文提示词：温暖明亮的现代波西米亚风客厅。横幅平视全景，机位约与坐姿视线齐平，右侧是米白 L 形布艺沙发（带右侧贵妃榻），配多件白灰米色抱枕与一条搭毯；中央为圆形双层木质茶几，上面放黑白条纹碗装绿植、下层放书；左侧有藤编单人椅、黑色小边桌（上放白色马克杯）与圆形针织蒲团。左墙为装饰墙：高处挂黑色长角牛头骨，下方多幅画框、圆形编织挂毯与流苏挂毯；后墙挂白色圆形大挂钟。浅灰绿墙面、浅色木地板与浅色地毯；右侧大窗配米色窗帘，窗外可见绿色庭院，墙面挂盆绿植。米白、浅灰、暖木色为主，绿植点缀，右侧窗户自然光、明亮均匀。避免把装饰墙画错成纯色墙、避免漏掉牛头骨装饰。
- 英文提示词：Warm bright modern bohemian living room, wide horizontal eye-level view, camera about at seated eye level. A cream L-shaped fabric sectional with a chaise on the right fills the right side, dressed with white, grey and beige throw pillows and a draped throw blanket. A round two-tier wooden coffee table stands in the center, holding a black-and-white striped bowl with a green plant and books on the lower shelf. To the left, a rattan armchair with a cream cushion, a small black side table with a white mug, and a round knitted pouf. The left wall is a gallery wall: a longhorn steer skull with black horns mounted high, framed prints, round woven wall hangings and a macrame tapestry; a large round white wall clock hangs on the back wall. Pale grey-green walls, light wood floor with a pale area rug. Tall windows with beige curtains on the right, a green garden visible outside, wall-mounted planters with green plants. Cream, light grey and warm wood tones with green plant accents, soft natural window light, clean and airy.
- 色卡（脚本实测）：#AFAD9F 主色 26.3%；#E6E7E0 辅色 22.0%；#948E7A 辅助色 18.2%；#CAC8BC 辅助色 17.3%；#6D634E 辅助色 11.3%；#322E20 点缀色 4.8%。

## 例 7：食物，BBQ 鸡肉菠萝披萨（Unsplash photo-1565299624946）

- 类型：food。2026-11-24 skill 基准版；食物层随后按扩展规则正式建层（见例 11）。
- 元数据：图像类型为真人摄影（美食摄影）；氛围温暖、诱人、家常烟火气；竖幅、俯拍、披萨占满画面中心、斜向摆放；光线为柔和自然光、暖调、轻微阴影、质感突出；色彩为金黄芝士加焦红酱汁加深棕木板，绿色香菜点缀，暖调浓郁；成像清晰锐利、芝士拉丝与焦边细节清楚；风格为美食摄影、俯拍平铺风；防错为避免把披萨写成完整未切、避免漏掉菠萝和红洋葱。菜品主体为 BBQ 鸡肉菠萝披萨，已切块（约 6 块，左侧边缘略有裁切）；食材配料为鸡丝、菠萝块、红洋葱丝、香菜叶、融化芝士、BBQ 酱汁；摆盘容器为深色木质长方形砧板；点缀物为香菜叶、半个红洋葱、一瓣蒜；熟度状态为芝士融化、饼边微焦。
- 核验要点：确认切片约 6 块、确认菠萝块与红洋葱丝、确认砧板是深色木质长方形、确认周围散落的香菜与半个红洋葱。
- 中文提示词：温暖诱人的美食摄影，俯拍。竖幅画面，一只 BBQ 鸡肉菠萝披萨斜放在深色木质长方形砧板上，已切成 6 块；表面铺满融化的金黄芝士、鸡丝、菠萝块、红洋葱丝，淋 BBQ 酱汁，撒香菜叶，饼边微微焦黄。砧板周围散落香菜叶、半个紫红洋葱与一瓣蒜，深棕木纹背景。柔和暖调自然光，芝士与酱汁质感清晰。避免把披萨写成完整未切、避免漏掉菠萝和红洋葱。
- 英文提示词：Warm appetizing food photography, top-down view. A BBQ chicken and pineapple pizza rests diagonally on a dark wooden rectangular board, cut into 6 slices; topped with melted golden cheese, shredded chicken, pineapple chunks, thin red onion slices, drizzled BBQ sauce and fresh cilantro leaves, the crust lightly browned. Cilantro sprigs, half a red onion and a garlic clove scattered around the board on a dark wood surface. Soft warm natural light, clear cheese and sauce textures, rich warm tones, vertical composition.
- 色卡（脚本实测）：#352721 主色 47.7%；#D58B31 辅色 16.4%；#874A23 辅助色 15.8%；#DFC29D 辅助色 13.0%；#47721A 辅助色 5.5%；#6E1A61 点缀色 1.6%。

## 例 8：动物，比格犬正面特写（Unsplash photo-1543466835）

- 类型：animal。2026-11-24 skill 基准版；动物层随后按扩展规则正式建层（见例 12）。
- 元数据：图像类型为真人摄影（宠物摄影）；氛围快乐、亲切、治愈；横幅、正面特写、狗头居中占满画面、浅景深；光线为柔和自然光、均匀、无硬阴影；色彩为黄褐色皮毛加白色口鼻与胸口，粉色舌头，背景土褐与绿色虚化；成像清晰锐利、毛发与鼻头纹理清楚、背景柔和虚化；风格为宠物肖像摄影；防错为避免把耳朵画竖起来（比格是垂耳）、避免闭嘴（嘴张开吐舌头）。动物主体为比格犬、成年、头肩特写；毛色为黄褐色加白色，额头白线；表情动作为嘴张开、粉色舌头伸出、眼睛圆亮、神态快乐；配饰为黑色项圈；背景为户外土路与绿色草地、大幅虚化。
- 核验要点：确认品种特征（垂耳、长耳、黄褐白三色）、确认舌头伸出、确认黑色项圈、确认背景虚化。
- 中文提示词：快乐治愈的宠物肖像摄影，正面特写。横幅画面，一只成年比格犬头部居中占满画面：黄褐色皮毛、白色口鼻与胸口、额头有一道白色线，两只长垂耳贴在脸侧；嘴巴张开、粉色舌头伸出，眼睛圆亮有神，神态快乐放松；脖子上戴黑色项圈。背景为户外土路与绿色草地，大幅虚化。柔和自然光，毛发与鼻头纹理清晰。避免把耳朵画竖起来、避免画成闭嘴。
- 英文提示词：Happy heartwarming pet portrait photograph, front-facing close-up. An adult beagle fills the center of the frame: tan and white coat with a white stripe down the forehead, long floppy ears resting against its cheeks; mouth open with a pink tongue out, round bright eyes, joyful relaxed expression; a black collar around its neck. The background is a blurred outdoor dirt path with green grass. Soft natural daylight, clear fur and nose textures, shallow depth of field, horizontal composition.
- 色卡（脚本实测）：#9C8670 主色 41.8%；#D1B390 辅色 21.9%；#584F37 辅助色 14.5%；#5C7038 辅助色 9.3%；#CFC1BC 辅助色 6.3%；#201C19 辅助色 6.2%。

## 例 9：艺术绘画，荷兰黄金时代花卉静物油画（Unsplash photo-1579783902614）

- 类型：artwork（古典静物油画；原定测插画/二次元，Unsplash 稳定拿到的这张是古典油画，非二次元，二次元另找图补测）。2026-11-24 skill 基准版；艺术绘画层随后按扩展规则正式建层（见例 13）。
- 元数据：图像类型为古典油画（荷兰黄金时代花卉静物）；氛围华丽、浓郁、古典庄重；竖幅、居中对称式构图、花束占满画面、深色背景；光线为戏剧性侧光、花朵明亮、背景深暗、明暗对比强烈；色彩为深黑背景加鲜艳花色（红、橙、粉、白、黄、蓝紫），高饱和花朵对深暗底；成像为油画笔触细腻、花瓣与昆虫细节精致；风格为荷兰黄金时代花卉静物油画；防错为避免把背景画亮、避免漏掉昆虫与台面静物。画作主体为青铜花瓶插满各色花卉；花种为红罂粟、红白条纹郁金香、粉白玫瑰、蓝色鸢尾、黄花、白色绣球等；昆虫为蝴蝶、蜻蜓、蜗牛、蜜蜂；台面静物为粉色玫瑰、玉米棒、麦穗、蝴蝶；花瓶为青铜色带金色装饰；背景为纯黑深色。
- 核验要点：确认花束品种多样（至少罂粟、郁金香、玫瑰、鸢尾）、确认昆虫（蝴蝶在右上、蜻蜓在左上、蜗牛在瓶下）、确认台面有玉米与麦穗、确认背景纯黑。
- 中文提示词：荷兰黄金时代花卉静物油画。竖幅画面，深黑色背景中央一只青铜花瓶插满各色花卉：顶部一朵硕大橙红罂粟，两侧为红白条纹郁金香，配粉白玫瑰、蓝色鸢尾、黄花、白色绣球与绿叶，花朵鲜艳饱满；花丛间有蝴蝶、蜻蜓、蜜蜂，瓶下台面有一只蜗牛、一朵粉色玫瑰、玉米棒与麦穗。戏剧性侧光，花朵明亮、背景深暗，明暗对比强烈，笔触细腻。避免把背景画亮、避免漏掉昆虫与台面静物。
- 英文提示词：Dutch Golden Age floral still life oil painting. On a deep black background, an ornate bronze vase overflows with flowers: a large frilled orange-red poppy at the top, red-and-white striped tulips on either side, pink and white roses, a blue iris, yellow blooms, white hydrangeas and green foliage. Butterflies, a dragonfly and a bee among the blossoms; on the stone ledge below, a snail, a pink rose, an ear of corn and wheat stalks. Dramatic side lighting, luminous flowers against the dark ground, strong chiaroscuro, fine detailed brushwork, vertical composition.
- 色卡（脚本实测）：#15130A 主色 61.9%；#342E19 辅色 16.0%；#6A5E3C 辅助色 6.8%；#BA441A 辅助色 5.9%；#71301A 辅助色 5.5%；#C4A78A 点缀色 3.9%。

## 例 10：车辆，灰色福特野马正面（Unsplash photo-1494976388531）

- 类型：vehicle。2026-11-24 skill 基准版；车辆层随后按扩展规则正式建层（见例 14）。
- 元数据：图像类型为真人摄影（汽车摄影）；氛围冷峻、力量感、阴郁大气；横幅、正面平视、车头居中、低机位；光线为阴天漫射光、均匀、车漆反光柔和；色彩为深灰车身加灰色天空与沥青路面，黄色标线点缀，低饱和冷调；成像清晰锐利、车漆与灯组细节清楚；风格为汽车宣传摄影；防错为避免把车写成侧面、避免漏掉挡风玻璃横幅文字。车辆主体为福特野马 Mustang、深灰色、正面；前脸细节为三条竖纹 LED 日间行车灯、黑色蜂窝格栅、野马徽标、雾灯亮起、引擎盖散热口；挡风玻璃文字为白色 STEEDA 横幅；环境为空旷停车场、黄色中线、两侧高杆路灯、阴天、远处低矮建筑。
- 核验要点：确认正面视角、确认三条 LED 日行灯、确认挡风玻璃 STEEDA 文字、确认雾灯亮起、确认黄色标线。
- 中文提示词：冷峻力量感的汽车摄影，正面平视。横幅画面，一辆深灰色福特野马正面居中：三条竖纹 LED 日间行车灯、黑色蜂窝状进气格栅、中央野马徽标，两侧雾灯亮起，引擎盖带散热口；挡风玻璃上方贴白色 STEEDA 横幅文字。空旷沥青停车场，一条黄色标线从车头向前延伸，两侧各有一根高杆路灯，远处低矮建筑，阴天灰色天空。低饱和冷调，车漆反光柔和。避免把车写成侧面、避免漏掉挡风玻璃横幅文字。
- 英文提示词：Cool powerful automotive photograph, front-on eye-level view. A dark grey Ford Mustang faces the camera head-on: triple-bar LED daytime running lights, black honeycomb grille with the running-horse emblem, fog lights on, hood vents; a white STEEDA banner across the top of the windshield. An empty asphalt parking lot, a yellow center line leading away from the car, tall lamp posts on either side, low buildings in the distance under an overcast grey sky. Low-saturation cool tones, soft reflections on the paintwork, horizontal composition.
- 色卡（脚本实测）：#BCBDC7 主色 20.8%；#93959C 辅色 16.8%；#DCDBE0 辅助色 16.4%；#6D7276 辅助色 15.5%；#484D51 辅助色 15.4%；#0F1011 辅助色 15.0%。

## 例 11：食物，韩式热狗棒芝士拉丝（用户直发图，2026-11-24）

- 类型：food。2026-11-24 用户直发图反推；本例为第二张食物图，食物层已按扩展规则正式建层。
- 元数据：图像类型为真人摄影（美食摄影）；氛围温暖、诱人、家常烟火气；竖幅、斜俯拍约 45 度、餐盘斜置、三根热狗棒斜向排列；光线为明亮暖调自然光、柔和、轻微阴影；色彩为金黄酥皮加红白酱料加白色餐盘，绿植点缀，暖调浓郁；成像清晰锐利、酥皮颗粒与拉丝芝士细节清楚；风格为美食摄影、社交媒体美食图；防错为避免把三根画成完整未动、避免漏掉切开的芝士拉丝。菜品主体为韩式热狗棒（玉米热狗），3 根、竹签串起；食材配料为面包糠酥皮、香肠、融化芝士；酱料为番茄酱与蛋黄酱、波浪形交叉淋面；摆盘容器为白色长方形餐盘；点缀道具为两只白色小瓷碗（番茄酱、蛋黄酱）、右上角绿叶植物、右下角黑白格纹餐布；熟度状态为外壳金黄酥脆、前方一根从中部切开拉开、芝士拉丝。
- 核验要点：确认 3 根、确认前方一根切开拉丝、确认红白双色酱料波浪纹、确认两只酱料碗内容（左番茄酱、上蛋黄酱）、确认竹签（上方两根清晰可见、前方一根右端出画不可见）。
- 中文提示词：温暖诱人的美食摄影，斜俯拍。竖幅画面，一只白色长方形餐盘斜放三根韩式热狗棒：金黄酥脆的面包糠外壳，表面淋红白相间的番茄酱与蛋黄酱波浪纹，竹签从右上方伸出；最前方一根从中间切开拉开，融化的芝士在断口处牵出长丝，露出里面粉色香肠。餐盘左上方两只白色小瓷碗，一碗番茄酱、一碗蛋黄酱；右上角一小丛绿叶植物，右下角黑白格纹餐布一角，浅色木桌背景。明亮暖调自然光，酥脆外壳与拉丝芝士质感清晰。避免把三根画成完整未动、避免漏掉切开的芝士拉丝。
- 英文提示词：Warm appetizing food photography, angled top-down view. Three Korean corn dogs lie diagonally on a white rectangular plate: golden crispy breadcrumb coating drizzled with zigzag lines of red ketchup and white mayonnaise, wooden skewers sticking out at the top right; the front one is cut open in the middle, melted cheese stretching in a long pull between the halves, revealing a pink sausage inside. Two small white ramekins at the top left hold ketchup and mayonnaise; a small green leafy plant in the top-right corner, a black-and-white checked cloth at the bottom right, light wooden table. Bright warm natural light, crisp coating and cheese-pull textures clearly visible, vertical composition.
- 色卡（脚本实测）：#CC5C22 主色 33.1%；#E6DBD5 辅色 25.0%；#C9AB91 辅助色 23.4%；#94735B 辅助色 12.6%；#8C973F 点缀色 3.0%；#405211 点缀色 2.9%。

## 例 12：动物，戴花环的白色小兔子（用户直发图，2026-11-24）

- 类型：animal。2026-11-24 用户直发图反推；本例为第二张动物图，动物层已按扩展规则正式建层。
- 元数据：图像类型为真人摄影（宠物摄影）；氛围温暖、治愈、春日梦幻；竖幅、低机位平视（与兔子齐平）、兔子居中偏左、面向右侧；光线为金色黄昏阳光、暖调、毛发边缘泛暖光、柔和；色彩为白色毛发加绿色草地，粉色花朵与黄色花心点缀，暖调柔和；成像清晰锐利、毛发细腻、背景柔和虚化；风格为宠物肖像摄影、春日田野风；防错为避免把耳朵画成垂耳（两耳竖起）、避免漏掉头上的花环。动物主体为白色小兔子、幼年、侧身坐姿、面向右侧；毛色毛发为纯白、蓬松柔软；特征细节为两只长耳竖起、耳内粉红、深棕色圆眼睛、粉色鼻子、白色胡须；表情动作为安静乖巧、侧脸向右；配饰为小花环（一朵粉色五瓣花贴在耳边、配小粉花与绿叶）；环境背景为春日草地、青草与苜蓿、白色雏菊（黄心）与紫色野花散落、背景绿色树木大幅虚化。
- 核验要点：确认面向右侧（侧脸）、确认两耳竖起、确认花环与粉色五瓣花、确认雏菊白瓣黄心、确认背景虚化。
- 中文提示词：温暖治愈的宠物摄影，低机位平视。竖幅画面，一只白色小兔子侧身坐在春日草地上，面向右侧：两只长耳朵竖起，耳内粉红；深棕色圆眼睛，粉色鼻子，白色胡须；头上戴一顶小花环，一朵粉色五瓣花贴在耳边，配绿色小叶。身下是青草与苜蓿，周围散落白色小雏菊与紫色野花，背景为虚化的绿色树木。金色黄昏阳光洒落，毛发边缘泛暖光，柔和梦幻。避免把耳朵画成垂耳、避免漏掉头上的花环。
- 英文提示词：Warm heartwarming pet photography, low ground-level view. A small white bunny sits in profile in a spring meadow, facing right: two long ears upright with pink inner ears, dark brown round eyes, a pink nose and white whiskers; a tiny flower crown on its head, one large pink five-petalled flower by its ear with small green leaves. Green grass and clover beneath, white daisies with yellow centers and small purple wildflowers scattered around, blurred green trees in the background. Golden evening sunlight, warm rim light on the fur, soft and dreamy, vertical composition.
- 色卡（脚本实测）：#606E2E 主色 22.6%；#4C4D28 辅色 21.8%；#C8C1BC 辅助色 19.3%；#918365 辅助色 12.9%；#A59D56 辅助色 12.3%；#2A2616 辅助色 11.2%。注：粉色花朵面积太小，未进入 6 色色卡。

## 例 13：艺术绘画，印象派玫瑰花卉油画（Pinterest Pin 852165560739680514，用户发链接，2026-11-24）

- 类型：artwork。2026-11-24 用户发 Pinterest 链接反推；本例为第二张艺术绘画图，艺术绘画层已按扩展规则正式建层。
- 元数据：图像类型为油画（印象派风格花卉油画）；氛围浪漫、柔和、朦胧梦幻；竖幅、花束占满画面、深色背景、花朵由上至下层叠；光线为柔和漫射光、花朵明亮、背景深暗、明暗对比中等；色彩为深灰黑背景加奶白淡黄花朵，珊瑚粉点缀，低饱和冷底暖花；成像为厚涂油画肌理、刮刀与笔触痕迹明显、松散写意；风格为印象派花卉油画；防错为避免把背景画亮、避免把笔触画成细腻写实、避免漏掉粉色玫瑰。媒介画种为布面油画；风格流派为印象派风格；画面主体为玫瑰花束（以白玫瑰、奶油色玫瑰为主，配珊瑚粉玫瑰）；笔触技法为厚涂、刮刀抹、笔触松散写意、花瓣边缘虚化；构图与色彩为竖幅满构图、花朵层叠由上至下、深灰黑底、明暗对比；细节母题为右下角红色签名（字迹不清）、画面细红色竖线与刮擦痕迹。
- 核验要点：确认花种以玫瑰为主（白、奶油、珊瑚粉）、确认厚涂笔触、确认深色背景、确认右下角红色签名（字迹不清）。
- 中文提示词：浪漫柔和的印象派花卉油画。竖幅画面，深灰黑背景上开满层叠的玫瑰：以白色与奶油色玫瑰为主，点缀几朵珊瑚粉玫瑰，花瓣厚涂松散、边缘虚化，刮刀与笔触痕迹明显；花朵由上至下铺满画面，右下角有红色签名。柔和漫射光，花朵明亮、背景深暗，冷底暖花。避免把背景画亮、避免把笔触画成细腻写实、避免漏掉粉色玫瑰。
- 英文提示词：Romantic soft Impressionist floral oil painting. On a dark grey-black ground, roses bloom in dense layers from top to bottom: mostly white and cream roses with a few coral-pink blooms, thick impasto petals with loose, blurred edges and visible palette-knife and brush marks; a red signature in the bottom-right corner. Soft diffused light, luminous flowers against the dark ground, cool background with warm blossoms, vertical composition.
- 色卡（脚本实测）：#242324 主色 27.3%；#4F5358 辅色 24.2%；#B0A9A1 辅助色 15.3%；#80725C 辅助色 15.3%；#AD9C73 辅助色 10.4%；#975B4A 辅助色 7.5%。

## 例 14：车辆，酒红色保时捷 911 巴黎街景（Pinterest Pin 907967974898066386，用户发链接，2026-11-24）

- 类型：vehicle。2026-11-24 用户发 Pinterest 链接反推；本例为第二张车辆图，车辆层已按扩展规则正式建层。
- 元数据：图像类型为真人摄影（汽车摄影）；氛围优雅、高级、巴黎街头气息；竖幅、低机位三刻侧面、车在画面下半部、建筑占上半部；光线为明亮日光、树影斑驳、漆面反光清晰；色彩为酒红车漆加米色石材加灰色石板路，绿植点缀，暖调高级；成像清晰锐利、漆面倒影与石板纹理清楚；风格为汽车宣传摄影、巴黎街景风；防错为避免把车写成正面、避免漏掉盾徽与黄色卡钳。车辆主体为保时捷 911（992 世代）、酒红色金属漆；视角角度为三刻侧面、车头朝右前方、低机位；车身细节为蛙眼圆 LED 大灯、车头金色盾徽、黑色前包围进气口、黑色多辐轮毂、黄色刹车卡钳；标识文字为车头盾徽（无横幅文字）；环境场景为巴黎石板街道、奥斯曼式建筑（米色石材立面、法式高窗、黑色铁艺阳台配绿植、拱形黑色双开大门、门前圆形修剪绿植）、左侧绿树与黑色复古路灯、远处一辆黑色轿车；漆面光影为明亮日光、漆面映出街景倒影、树影洒在墙面。
- 核验要点：确认保时捷 911（蛙眼圆灯、车头盾徽）、确认三刻侧面角度（非正面）、确认酒红金属漆、确认黑色轮毂与黄色卡钳、确认巴黎奥斯曼建筑（米色石材、黑铁阳台、拱形黑门）、确认石板路。
- 中文提示词：优雅高级的汽车摄影，低机位三刻侧面。竖幅画面，一辆酒红色保时捷 911 停在巴黎石板街道上，车头朝右前方：圆润的蛙眼 LED 大灯、车头金色盾徽、黑色前包围进气口，黑色多辐轮毂配黄色刹车卡钳，金属漆面映出街景倒影。身后是米色奥斯曼式建筑立面：高大的法式窗、黑色铁艺阳台配绿植、拱形黑色双开大门、门前圆形修剪绿植；左侧绿树与黑色复古路灯，远处还有一辆黑色轿车。明亮日光，树影斑驳洒在墙面。避免把车写成正面、避免漏掉盾徽与黄色卡钳。
- 英文提示词：Elegant high-end automotive photography, low three-quarter front view. A burgundy Porsche 911 sits on a Parisian cobblestone street, nose pointing to the right: round frog-eye LED headlights, gold Porsche crest on the hood, black front intakes, black multi-spoke wheels with yellow brake calipers, the metallic paint reflecting the streetscape. Behind it, a cream Haussmann facade with tall French windows, black wrought-iron balconies with green plants, arched black double doors and round topiary bushes; green trees and a black vintage street lamp to the left, another black car far down the street. Bright daylight, dappled tree shadows on the stonework, vertical composition.
- 色卡（脚本实测）：#736F6C 主色 22.6%；#191411 辅色 20.4%；#ADA399 辅助色 20.2%；#443933 辅助色 16.1%；#92826B 辅助色 13.0%；#5F5B30 辅助色 7.7%。注：酒红色车漆被归入深棕色系，未单独成色。

## 例 15：插画，国风仙侠女子侧脸（Pinterest Pin 838302918190306286，用户发链接，2026-11-24）

- 类型：illustration。2026-11-24 用户发 Pinterest 链接反推；首张插画/二次元类图；插画层随后按扩展规则正式建层（见例 16）。
- 元数据：图像类型为插画（国风仙侠风格数字绘画）；氛围梦幻、唯美、空灵缥缈；竖幅、女子侧脸居中偏上、面向右侧、下半幅为山峦云雾；光线为柔和漫射光、无明确光源、整体发光感；色彩为薄荷绿、天蓝、淡紫、粉色交织的粉彩色调，星光点点；成像为数字绘画、笔触柔和、边缘晕染、梦幻虚化；风格为国风仙侠插画、唯美古风；防错为避免画成写实照片、避免在画面右下角画水印。画面主体为长发女子侧脸（闭目凝神、面向右侧）与青绿山峦的人景合一构图；人物细节为深蓝色长发如水流般向左飘散、与云雾山峦融为一体，发间别银色云纹发簪，脸颊有点点蓝色花钿，肤色白皙、唇色粉红；动作神态为轻嗅面前一朵粉色花、神情安详；配角元素为右上角粉色花朵（似木兰？）与金色新月；环境背景为下半幅青绿山峦、松树、流云与星光；文字水印为右下角微博水印 @吟耳汤（生图时不复现）。
- 核验要点：确认面向右侧（侧脸）、确认闭目、确认蓝发飘向左侧并与山峦相融、确认右上角新月、确认右下角水印内容。
- 中文提示词：梦幻唯美的国风仙侠插画。竖幅画面，一位长发女子侧脸向右、闭目凝神：深蓝色长发如水流般向左飘散、与云雾山峦融为一体，发间别银色云纹发簪，脸颊有点点蓝色花钿；她正轻嗅面前一朵粉色花，右上角一弯金色新月。她的肩颈化作白色云雾，下半幅是青绿山峦、松树与流云，薄荷绿、天蓝、淡紫、粉色交织，星光点点。避免画成写实照片、避免在画面右下角画水印。
- 英文提示词：Dreamy ethereal Chinese fantasy anime illustration. A long-haired woman in profile faces right with eyes closed: deep blue hair flows left like water, dissolving into clouds and mountains, silver cloud-shaped hairpins, small blue decorative dots on her cheek; she leans in to smell a pink blossom, a golden crescent moon in the top-right corner. Her shoulders melt into white mist, and the lower half is misty green-blue mountains with pine trees and drifting clouds. Pastel mint green, sky blue, lavender and pink with scattered starlight, vertical composition.
- 色卡（脚本实测）：#DAE1D8 主色 25.3%；#ADC3D3 辅色 20.7%；#7B9EA2 辅助色 17.1%；#D9C4C3 辅助色 14.7%；#A3C7AE 辅助色 13.6%；#7C96D0 辅助色 8.6%。

## 例 16：插画，日系二次元金发少女花墙（Pinterest Pin 964192601515762918，用户发链接，2026-11-24）

- 类型：illustration。2026-11-24 用户发 Pinterest 链接反推；本例为第二张插画图，插画层已按扩展规则正式建层。
- 元数据：图像类型为插画（日系二次元风格数字绘画）；氛围清新、梦幻、甜美；竖幅、少女半身正面居中、花墙铺满背景；光线为明亮日光、透过花叶洒落、柔和；色彩为橙色花朵加深绿叶片，配浅蓝紫服装与粉白肤色，撞色鲜明；成像为数字绘画、上色柔和、线条清晰、光影细腻；风格为日系二次元插画、清新少女风；防错为避免把手画错（手指数量与爱心手势）、避免把辫子画成散发。画风为日系二次元；角色主体为金发少女、半身正面、齐刘海、大眼睛、脸颊泛红晕；姿态表情为双手举到胸前比出爱心手势、唇边衔一朵橙色喇叭花、神情羞涩甜美；服装造型为白色吊带裙、外搭浅蓝紫色宽松开衫、一侧肩膀微露、两条麻花辫发尾系浅蓝色蝴蝶结；背景世界为铺满画面的绿色叶片与橙色花朵（似金莲花/牵牛花？）；渲染质感为柔和上色、粉彩色调、阳光透过花叶的光斑。
- 核验要点：确认两条麻花辫与蓝色蝴蝶结、确认爱心手势、确认唇边橙色花、确认开衫浅蓝紫色、确认背景花墙橙绿配色。
- 中文提示词：清新梦幻的日系二次元插画。竖幅画面，一位金发少女半身正面站在橙色花墙前：两条麻花辫垂在胸前、发尾系浅蓝色蝴蝶结，齐刘海，大眼睛微微泛红晕；双手举到胸前比出爱心手势，唇边衔一朵橙色喇叭花。她穿白色吊带裙、外搭浅蓝紫色宽松开衫，一侧肩膀微露。身后是铺满画面的绿色叶片与橙色花朵，阳光透过花叶洒落。避免把手画错（手指数量与爱心手势）、避免把辫子画成散发。
- 英文提示词：Fresh dreamy Japanese anime illustration. A blonde girl stands half-length facing the camera before a wall of orange flowers: two braids fall over her chest tied with light blue bows, straight bangs, large eyes with a soft blush; both hands raised to her chest forming a heart shape, an orange trumpet flower held to her lips. She wears a white camisole dress under a loose lavender-blue cardigan, one shoulder slightly bare. Dense green leaves and orange blossoms fill the background, sunlight filtering through. Soft pastel shading, vertical composition.
- 色卡（脚本实测）：#E0C5D7 主色 26.6%；#B4907E 辅色 23.1%；#425F66 辅助色 18.7%；#B1B3EC 辅助色 13.1%；#E57A3B 辅助色 10.5%；#7D85C8 辅助色 8.0%。

## 例 17：风景，巴黎黄昏城市全景与黑猫（Pinterest Pin 387520742962846387，用户发链接，2026-11-24）

- 类型：landscape（城市黄昏风景；次类型 architecture 建筑元素）。2026-11-24 用户发 Pinterest 链接反推。
- 元数据：图像类型为写实风格城市风景画（数字绘画观感）；氛围浪漫、静谧、带一丝忧郁的黄昏；竖幅、高视角俯瞰、黑猫与路灯在右前景、河流居中、城市与落日在远景；光线为黄昏落日余晖加城市灯火、暖橙与深蓝灰对比；色彩为深蓝灰暮色为主，暖橙灯火与落日点缀，蓝橙对比；成像细腻写实、光影层次丰富、远景略带雾气；风格为写实城市风景插画、巴黎黄昏；防错为避免把黑猫漏掉、避免把落日画成正午太阳。地貌地形为城市河景（塞纳河）、河岸建筑群；天气大气为晴朗黄昏、薄雾、能见度高；时间季节为日落时分、冬季（枯树枝）；景深层次为前景黑猫与路灯、中景河流与船只、远景城市天际线与落日；自然元素细节为河面橙色灯火倒影、顶部枯树枝桠；人为元素为圆顶建筑、双尖塔教堂、奥斯曼式楼房、桥梁、路灯、铁艺栏杆、船只。
- 核验要点：确认黑猫在右前景栏杆上（背对镜头）、确认路灯点亮、确认落日半沉在地平线、确认圆顶建筑在左、双尖塔在中、确认河面倒影。
- 中文提示词：浪漫静谧的巴黎黄昏城市风景。竖幅高视角，一只黑猫蹲坐在阳台铁艺栏杆上、背对镜头眺望落日，旁边一盏点亮的复古欧式路灯洒出暖橙色光晕；下方是塞纳河，河面映着两岸灯火的橙色倒影，几艘小船缓缓行驶。对岸是巴黎老城：左侧圆顶建筑与双尖塔教堂剪影，成排的奥斯曼式楼房亮着暖黄窗光；地平线上落日半沉，天空橙粉晚霞，顶部枯树枝桠入画。深蓝灰暮色与暖橙灯火对比，宁静浪漫。避免把黑猫漏掉、避免把落日画成正午太阳。
- 英文提示词：Romantic tranquil Parisian cityscape at dusk. From a high balcony, a black cat sits on an ornate iron railing with its back to the viewer, gazing at the sunset, beside a lit vintage street lamp glowing warm orange; below, the Seine mirrors the orange lights of both banks, small boats drifting on the water. Across the river, the old city: a domed building and twin Gothic spires in silhouette, rows of Haussmann buildings with warm glowing windows; the sun half-sunk on the horizon, an orange-pink sunset sky, bare winter branches framing the top. Deep blue-grey dusk against warm orange lights, serene and romantic, tall vertical composition.
- 色卡（脚本实测）：#28241E 主色 48.9%；#645952 辅色 23.9%；#4C392C 辅助色 16.0%；#906752 辅助色 5.4%；#BA6545 点缀色 3.6%；#E69A65 点缀色 2.3%。

## 例 18：人像（双人），夏日草坡上的男女与收录机（Pinterest Pin 908530924845699413，用户发链接，2026-11-24）

- 类型：portrait（双人合影；次类型 landscape 天空草地）。2026-11-24 用户发 Pinterest 链接反推。注意：原图文件是横着存的（480×853 竖幅文件，内容需逆时针转 90 度才是正向 16:9 横幅），本例按转正后的场景反推。
- 元数据：图像类型为真人摄影（电影感双人照片）；氛围清新、夏日、青春怀旧；横幅 16:9、低机位仰拍、男生坐右下、女生站左中、天空占上半幅；光线为明亮日光、左上方来光、柔和阴影；色彩为蓝天白云加绿草，黑白服装对比，饱和度适中；成像清晰锐利、电影感、景深较深；风格为青春电影剧照风；防错为避免把两人画成面对镜头、避免漏掉收录机。主体人物为一男一女、青年、东亚面孔；身形轮廓为男生坐姿屈膝、女生站姿修长；肤色肤调为自然浅肤色；动作表情为男生双手捧咖啡杯、抬头望向女生，女生右手搭在额前眺望远方；微表情情绪为男生专注仰望、女生出神远眺；发型妆容配饰为男生黑色短发、女生黑色短发、无明显配饰；服装结构贴合为男生白短袖衬衫加黑阔腿裤加黑鞋、女生白短袖衬衫加黑色长裙加白鞋；服装材质为棉质衬衫、垂坠长裙；皮肤光泽细节为自然日光下的真实肤质；场景背景为草地山坡、灌木岩石、辽阔蓝天与大朵积云，右下角一台灰色老式收录机。
- 核验要点：确认原图需逆时针转 90 度、确认男生坐右、女生站左、确认男生双手捧杯、确认女生右手搭额、确认收录机在右下角。
- 中文提示词：清新夏日的电影感双人照片。横幅 16:9，低机位仰拍。草地山坡上，一位男生坐在右侧地面：白衬衫、黑阔腿裤，双手捧着一杯外带咖啡，抬头望向左侧的女生；女生站在左侧：白短袖衬衫、黑色长裙，肩背黑色单肩包，右手搭在额前眺望远方。身后是辽阔蓝天与大朵积云，绿草灌木与岩石，右下角地上放着一台灰色老式收录机。明亮日光，青春电影感。避免把两人画成面对镜头、避免漏掉收录机。
- 英文提示词：Fresh summery cinematic photograph of two young people. Wide 16:9 frame, low angle looking slightly up. On a grassy rocky hillside, a young man sits on the ground at the right in a white shirt and black wide-leg trousers, holding a takeaway coffee cup in both hands, looking up at the young woman standing to the left; she wears a white short-sleeve shirt and a long black skirt, a black shoulder bag, her right hand raised to her forehead as she gazes into the distance. A vast blue sky with big cumulus clouds behind them, green shrubs and rocks, a grey vintage boombox on the ground at the bottom right. Bright daylight, youthful film-still atmosphere, horizontal composition.
- 色卡（脚本实测，旋转不改变像素色卡）：#545C6A 主色 24.2%；#181C1F 辅色 20.5%；#474D32 辅助色 17.5%；#7E808A 辅助色 15.7%；#6281AA 辅助色 14.0%；#C0BDBA 辅助色 8.1%。

## 例 19：风景，东京雨夜小巷与晴空塔（Pinterest Pin 971581319635983514，用户发链接，2026-11-24）

- 类型：landscape（城市雨夜街景；次类型 architecture 建筑与招牌）。2026-11-24 用户发 Pinterest 链接反推；首张夜景图。
- 元数据：图像类型为真人摄影（城市夜景摄影）；氛围怀旧、氛围感强、雨夜静谧；竖幅、巷子纵深透视、居酒屋在左前景、晴空塔在远景；光线为夜间灯火、灯笼暖橙光加远处蓝白光、湿路面反光；色彩为深蓝黑夜色为主，暖橙灯笼光点缀，粉色樱花一角，蓝橙对比；成像清晰锐利、湿路面倒影细腻、远景略带雾气；风格为东京夜景摄影、电影感；防错为避免把招牌文字写错、避免把路面画干。地貌地形为城市狭窄巷道、石板路；天气大气为雨夜、路面湿润反光、细雨；时间季节为深夜、春季（樱花）；景深层次为前景居酒屋与灯笼、中景湿巷与电线杆、远景晴空塔与高楼；自然元素细节为左上方垂落的樱花枝；人为元素为居酒屋（大灯笼"ラーメン"、竖招牌"居酒屋"、门帘"やきとり"、小黑板"中焼き"、小橙灯笼一排）、饮料自动售货机、右侧"ホテル"竖招牌、电线杆与密电线、自行车、黑色面包车、远处撑伞行人、东京晴空塔。
- 核验要点：确认招牌文字（ラーメン、居酒屋、やきとり、ホテル、中焼き）、确认晴空塔在远景、确认路面湿润有倒影、确认樱花在左上方、确认售货机在最左侧。
- 中文提示词：氛围感十足的东京雨夜小巷。竖幅画面，雨后深夜的狭窄巷子：左侧一家居酒屋亮着暖黄灯光，门口挂红色大灯笼写着"ラーメン"，一排小橙灯笼挂在屋檐下，竖招牌写着"居酒屋"，深色门帘上写"やきとり"，门口立着"中焼き"小黑板；最左侧一台亮着的饮料自动售货机，左上方樱花枝垂落。湿漉漉的石板路映着红橙灯光的倒影，右侧楼房挂着"ホテル"竖招牌，电线杆与密密的电线横过夜空；远处东京晴空塔亮着蓝白灯光，几个撑伞的行人走在巷子深处。深蓝夜色与暖橙灯火对比，雨夜氛围浓郁。避免把招牌文字写错、避免把路面画干。
- 英文提示词：Atmospheric Tokyo alley on a rainy night. A narrow lane after rain: on the left, an izakaya glows warm yellow, a large red paper lantern reading "ラーメン" by the door, a row of small orange lanterns under the eaves, a vertical sign reading "居酒屋", a dark noren curtain with "やきとり", a small chalkboard reading "中焼き" at the entrance; a lit drink vending machine at the far left, cherry blossom branches hanging from the top left. The wet stone street mirrors the red and orange lights; on the right, buildings with a vertical "ホテル" sign, utility poles and dense wires crossing the night sky; in the distance the Tokyo Skytree glows blue-white, a few pedestrians with umbrellas walk deep in the alley. Deep blue night against warm orange lantern light, rich rainy-night atmosphere, vertical composition.
- 色卡（脚本实测）：#1A1111 主色 36.1%；#333847 辅色 26.5%；#552A1F 辅助色 21.6%；#B2754E 辅助色 8.2%；#BD3F20 点缀色 4.2%；#858394 点缀色 3.4%。

## 例 20：海报，北海岸国际风筝节 2018（Pinterest Pin 602708362632086520，用户发链接，2026-11-24）

- 类型：poster（文字海报）。2026-11-24 用户发 Pinterest 链接反推；首张文字海报类图；海报层随后按扩展规则正式建层（见例 21）。
- 元数据：图像类型为平面设计（活动海报）；氛围清爽、有力、秋日海风感；竖幅、主标题斜向居中偏右、信息文字分置四角、留白大；光线为平面设计、无光影、仅标题带深蓝色投影；色彩为纯蓝底加白色文字，蓝白两色；成像清晰锐利、印刷质感；风格为现代中文手写字海报、极简；防错为避免把标题文字写错、避免加多余图形。主标题为"回到北岸自由放風吧"（白色手写毛笔大字、斜向排列、带深蓝色投影）；副标题为"北海岸國際風箏節 2018"（斜排小字，部分被主标题遮挡）；时间信息为左上角"THU 09.27 10:00—11:00 OPENING SHOW / TUE 10.02 10:00—20:00 TIME"；地点信息为右上角"BREEZY PARTY"与竖排"白沙灣—風箏公園"、"新北市石門區"；边缘竖排文字为左"北岸秋風折福祭"、左下"北海—風季—藍天"、右"貳零壹捌初秋"；底部信息为左下"北海岸國際風箏節 2018 www.ntpc-kite.com"、右下英文"NORTH COAST INTERNATIONAL KITE FESTIVAL"。
- 核验要点：确认主标题 9 字逐字（回到北岸自由放風吧）、确认日期与时间（09.27 开幕秀、10.02 全天）、确认网址（www.ntpc-kite.com）、确认蓝白两色、无其他图形。
- 中文提示词：简洁有力的活动海报设计。竖幅画面，纯蓝色背景，中央是白色手写毛笔大字"回到北岸自由放風吧"，斜向排列、带深蓝色投影；左上角白字写"THU 09.27 10:00—11:00 OPENING SHOW / TUE 10.02 10:00—20:00 TIME"，右上角"BREEZY PARTY"与竖排"白沙灣—風箏公園"；左下角"北海岸國際風箏節 2018 www.ntpc-kite.com"，右下角英文"NORTH COAST INTERNATIONAL KITE FESTIVAL"。蓝白两色，留白大，字体手写感强。避免把标题文字写错、避免加多余图形。
- 英文提示词：Bold minimalist event poster design. On a solid blue background, large white hand-lettered Chinese brush characters read "回到北岸自由放風吧", arranged diagonally with dark blue drop shadows; top left in white sans-serif: "THU 09.27 10:00—11:00 OPENING SHOW / TUE 10.02 10:00—20:00 TIME"; top right "BREEZY PARTY" with vertical text "白沙灣—風箏公園"; bottom left "北海岸國際風箏節 2018 www.ntpc-kite.com", bottom right "NORTH COAST INTERNATIONAL KITE FESTIVAL". Blue and white only, generous negative space, strong hand-lettered typography, vertical composition.
- 色卡（脚本实测）：#276AB3 主色 63.9%；#E8EDF3 辅色 15.5%；#1D548C 辅助色 8.8%；#AFC5D9 点缀色 4.3%；#4C7EB2 点缀色 3.8%；#799EC1 点缀色 3.7%。

## 例 21：海报，字体设计海报「你就是我的向往生活」（Pinterest Pin 593912269636521911，用户发链接，2026-11-24）

- 类型：poster。2026-11-24 用户发 Pinterest 链接反推；本例为第二张海报图，海报层已按扩展规则正式建层。另：下载工具首次失败（图钉页 og:image 为空且无 orig JSON，报 NO_DATA），后从页面内嵌 grep 到 736x 直链手动下载成功。
- 元数据：图像类型为平面设计（字体设计海报，照片底图加手写字）；氛围清新、浪漫、自由、夏日；竖幅、标题占天空上半幅、草坡与人物在下半幅、留白大；光线为明亮日光、晴朗；色彩为蓝天加绿草加白色文字，清新蓝绿；成像清晰锐利、照片底图真实；风格为字体设计海报、吉卜力般夏日感；防错为避免把标题文字写错、避免把两人画大。主标题为"你就是我的向往生活"（白色手写毛笔大字、分两行斜向排列、占天空中央）；信息文字为左上角"FONT DESIGN CHEN CHENG"（带下划线）、右上角"2023 / 04"、右下角小红书标志与"小红书号：cc6791"；版式布局为标题在上、画面在下、信息分置四角；背景画面为蓝天绿草照片（辽阔绿色草坡、晴朗蓝天、左下一小朵白云）；字体设计为手写毛笔字、笔触飞白、自由斜排；品牌标识为小红书 logo 与账号 cc6791。
- 核验要点：确认主标题 9 字逐字（你就是我的向往生活）、确认两人位置（男左女右、女撑浅绿伞）、确认左上署名与右上日期、确认右下小红书号（cc6791）。
- 中文提示词：清新浪漫的字体设计海报。竖幅画面，蓝天绿草的照片底图：下半幅是辽阔绿色草坡，一男一女两个小人在草坡上奔跑，女生撑一把浅绿色雨伞；上半幅是晴朗蓝天。天空中央是白色手写毛笔大字"你就是我的向往生活"，分两行斜向排列；左上角小字"FONT DESIGN CHEN CHENG"，右上角"2023 / 04"，右下角小红书标志与"小红书号：cc6791"。蓝绿清新，留白大，吉卜力般的夏日感。避免把标题文字写错、避免把两人画大。
- 英文提示词：Fresh romantic typography poster. A photo background of blue sky and green grass: the lower half is a vast green hillside with two tiny figures running, the woman holding a light green umbrella; the upper half is a clear blue sky. Large white hand-lettered Chinese brush characters read "你就是我的向往生活" across the sky in two lines; small text top left "FONT DESIGN CHEN CHENG", top right "2023 / 04", bottom right a Xiaohongshu logo with "小红书号：cc6791". Fresh blue and green, generous negative space, Ghibli-like summer feeling, vertical composition.
- 色卡（脚本实测，仅 4 色，相近色已合并）：#7CB3E0 主色 67.5%；#9DB684 辅色 25.2%；#B5D0E1 点缀色 4.1%；#EBF4F4 点缀色 3.2%。

## 例 22：海报，梵高沉浸式展览海报（Pinterest Pin 388013324145778125，用户发链接，2026-11-24）

- 类型：poster（展览海报）。2026-11-24 用户发 Pinterest 链接反推。
- 元数据：图像类型为平面设计（艺术展览海报）；氛围艺术感强、经典；竖幅、巨型字母三行居中、信息文字分置边缘、留白适中；光线为平面设计、无光影；色彩为白底，字母内梵高画作色彩（黄、蓝、绿、棕）；成像清晰锐利、印刷质感；风格为现代展览海报、字母填充画作；防错为避免把字母里的画作填错、避免把展览日期写错。主标题为"VAN GOGH INSIDE"（巨型无衬线英文字母、分三行、字母内部填充梵高名画：V 自画像、N 向日葵、G 与 O 杏花、C 与 H 罗纳河上的星空、INSIDE 一行麦田群鸦）；信息文字为字母下方英文"Van Gogh Inside : Festival of Light and Music"、左侧竖排"2016. 1. 8 — 4. 17"、右侧竖排"문화역서울 284 / Cultural Station 284"、底部韩文"반 고흐 인사이드 : 빛과 음악의 축제"与"문의 1522-1728 | www.vangoghinside.com"；版式布局为字母即画面、信息分置四边；背景画面为白色底、无底图、画作只在字母内；字体设计为无衬线大写英文字母、粗体；品牌标识为底部一排赞助商 logo（字迹不清）。
- 核验要点：确认主标题三行拼写（VAN / GOGH / INSIDE）、确认每字母内的画作对应关系、确认日期（2016. 1. 8 — 4. 17）、确认网址（www.vangoghinside.com）。
- 中文提示词：梵高沉浸式展览海报设计。竖幅画面，白色背景，巨大的无衬线英文字母"VAN GOGH INSIDE"分三行排列，字母内部填充梵高名画：V 是自画像、N 是向日葵、G 和 O 是杏花、C 和 H 是罗纳河上的星空、INSIDE 一行是麦田群鸦。字母下方小字英文"Van Gogh Inside : Festival of Light and Music"，左侧竖排"2016. 1. 8 — 4. 17"，右侧竖排"문화역서울 284 / Cultural Station 284"，底部一行韩文与网址"www.vangoghinside.com"。白底，字母即画面，艺术展海报。避免把字母里的画作填错、避免把展览日期写错。
- 英文提示词：Van Gogh immersive exhibition poster. On a white background, giant sans-serif letters "VAN GOGH INSIDE" in three lines, each letter filled with a Van Gogh painting: the V a self-portrait, the N sunflowers, G and O almond blossom, C and H Starry Night Over the Rhône, the INSIDE row a wheatfield with crows. Small text below reads "Van Gogh Inside : Festival of Light and Music"; vertical text on the left "2016. 1. 8 — 4. 17", on the right "문화역서울 284 / Cultural Station 284", Korean text and "www.vangoghinside.com" at the bottom. White background, letters as the image, art exhibition poster, vertical composition.
- 色卡（脚本实测）：#FAFAF9 主色 52.3%；#8D6C45 辅色 11.4%；#3B4241 辅助色 11.1%；#BCC0B2 辅助色 9.9%；#759999 辅助色 9.4%；#BFAF45 辅助色 6.0%。

## 例 23：人像（九人合影），低机位仰拍团体照（Pinterest Pin 915356693034523459，用户发链接，2026-11-24）

- 类型：portrait（多人合影）。2026-11-24 用户发 Pinterest 链接反推。
- 元数据：图像类型为真人摄影（团体合影）；氛围阳光、青春、活力；竖幅、极低机位仰拍、相机贴地面向上、九人围在镜头上方、上半幅为晴朗蓝天；光线为明亮日光、强光、阴影分明；色彩为蓝天加黑白服装加浅色牛仔裤，饱和度适中；成像清晰、略带胶片颗粒感；风格为青春团体写真、街头感；防错为避免把人数画错、避免把仰拍改成平拍。主体人物为九人（前排三女坐姿、后排六人站姿，青年、东亚面孔）；身形轮廓为前排屈膝坐、后排俯身向镜头；肤色肤调为自然肤色、日光下偏暖；动作表情为中间女生嘴巴微张、左女灿烂大笑、右女手搭帽檐、后排银色墨镜女生手指点唇、最右男生伸手指向镜头；微表情情绪为轻松活泼；发型妆容配饰为多人戴墨镜（黑、银、圆框）、一人戴黑棒球帽、一人戴白色有线耳机、一人戴眼镜；服装结构贴合为前排两女穿同款白底深条纹 T 恤加浅色阔腿牛仔裤、其余多为黑色上衣、最左男生黑白条纹衬衫；服装材质为棉质 T 恤、牛仔裤；皮肤光泽细节为日光下的真实肤质、强光阴影；场景背景为晴朗无云蓝天占上半幅、地面在最下方。
- 核验要点：确认共九人（前排 3、后排 6，含后排中间一位半张脸在阴影中）、确认极低机位仰拍、确认前排两女同款条纹 T 恤、确认最右男生指向镜头。
- 中文提示词：阳光灿烂的九人团体合影。竖幅画面，极低机位仰拍，相机贴在地面向上：九个年轻人围在镜头上方俯身看向镜头，上半幅是晴朗无云的蓝天。前排三位女生坐着：中间女生穿白底深条纹 T 恤、浅色阔腿牛仔裤，戴黑墨镜、白色耳机，嘴巴微张；左边女生戴黑墨镜灿烂大笑；右边女生戴黑棒球帽、手搭帽檐。后排六人站着：最左男生穿黑白条纹衬衫戴圆墨镜，中间女生戴银色椭圆墨镜、手指点唇，最右男生伸手指向镜头。明亮日光，胶片质感，青春活力。避免把人数画错、避免把仰拍改成平拍。
- 英文提示词：Sunny group photo of nine young people. Extreme low-angle shot, camera on the ground looking up: nine friends lean over the lens, the upper half a clear cloudless blue sky. Three women sit in front: the center one in a white T-shirt with dark stripes and light wide-leg jeans, black sunglasses, white earphones, mouth slightly open; the left one laughing in black sunglasses; the right one in a black baseball cap, hand on the brim. Six stand behind: a man in a black-and-white striped shirt with round sunglasses on the far left, a woman in silver oval sunglasses with a finger to her lips in the middle, a man pointing down at the camera on the far right. Bright sunlight, film-photo texture, youthful energy, vertical composition.
- 色卡（脚本实测，仅 5 色，相近色已合并）：#141515 主色 39.6%；#41657B 辅色 37.8%；#A9AFAA 辅助色 9.6%；#D5AE90 辅助色 7.0%；#614B3F 辅助色 6.0%。

## 例 24：品牌横幅，FOYEGE 社交账号条（用户直发图，2026-11-24）

- 类型：other（品牌横幅/Logo 标识；暂无专属层，按扩展规则需第二张同类图跑通后才建层）。2026-11-24 用户直发图反推；首张品牌标识类图。
- 元数据：图像类型为平面设计（品牌横幅）；氛围极简、干净、利落；超宽横条（约 4.75:1）、品牌名在左、社交账号行在下方、右侧大面积留黑；光线为平面设计、无光影；色彩为深黑底加白字，黑白两色；成像清晰锐利；风格为极简品牌视觉；防错为避免用衬线体、避免把 Instagram 和 X 的账号拆成两个、避免把账号写错。品牌名为"FOYEGE"（白色定制展示字体、笔画等粗的几何无衬线、每字母带斜切设计：O 为上下两段弧线、右上与左下各一道斜切缺口，F 顶横为斜切平行四边形、竖笔底部削成尖角，E 三横端部斜切，G 为几何开口圆环加横杠，位于左上）；社交账号为 Instagram 图标与 X 图标并排在前、共用"@foyege24"，YouTube 图标后"@Fo_yege1664"、TikTok 图标后"@foyege27"（逐字抄，YouTube 账号首字母大写 F）；背景为近黑色带淡淡暗绿纹理；图标为白色线条社交图标（Instagram、X、YouTube、TikTok）。
- 核验要点：确认品牌名拼写（FOYEGE）、确认三个账号逐字（@foyege24、@Fo_yege1664、@foyege27）、确认右侧留黑无内容。
- 中文提示词：极简的品牌横幅设计。超宽横条（约 4.75:1），深黑底色带淡淡暗绿纹理，左侧白色定制展示字体大写字母"FOYEGE"：笔画等粗的几何无衬线，但每个字母都带斜切设计——最特别的是字母 O，它不是闭合的圆环，而是由上下两段弧线组成，右上与左下各有一道斜切缺口，像被斜刀切开的圆；F 的顶横是斜切的平行四边形、竖笔底部削成尖角；E 的三横端部斜切；G 是几何开口圆环加横杠。整体锐角斜切、速度感强、科技感。字高约占画面三分之一，不要占满画面；下方一行小字社交账号：Instagram 图标与 X 图标并排在前、共用一个"@foyege24"，YouTube 图标后写"@Fo_yege1664"，TikTok 图标后写"@foyege27"。右侧大面积留黑，黑白两色，干净利落。避免用常规衬线体或常规无衬线体、避免把 O 画成闭合圆环、避免把字母画成普通字体、避免把账号写错、避免把 Instagram 和 X 的账号拆成两个。
- 英文提示词：Minimalist brand banner design. An ultra-wide horizontal strip (about 4.75:1) on a near-black background with a faint dark green texture; on the left, white custom display capitals "FOYEGE": monolinear geometric sans-serif with a diagonal-cut motif on every letter — most distinctively, the O is not a closed ring but two arcs separated by diagonal gaps at the upper right and lower left, as if sliced by a diagonal blade; the F has a slanted parallelogram top bar and a pointed blade-like stem bottom; the E's three bars end in diagonal cuts; the G is a geometric open ring with a horizontal bar. Sharp angular cuts throughout, fast and techy. Letter height about one third of the frame, not dominating the image; below, a row of small social media handles: Instagram and X icons side by side sharing one "@foyege24", YouTube icon followed by "@Fo_yege1664", TikTok icon followed by "@foyege27". The right side is empty black space. Black and white only, clean and sharp. Avoid conventional serif or sans-serif typefaces, avoid a closed-ring O, avoid ordinary letterforms, avoid splitting the Instagram and X handles into two.
- 色卡（脚本实测）：#070B0C 主色 31.9%；#212A22 辅色 28.3%；#3A4141 辅助色 19.0%；#515653 辅助色 8.5%；#909393 辅助色 7.1%；#F1F1F1 辅助色 5.2%。
- 订正（2026-11-24）：首版把字体误认作衬线体（原图仅 418×88，小图下误读），用户按提示词生成后指出字体不对；放大 3 倍核对确认原图为几何无衬线（笔画粗细均匀、端点斜切），提示词已按 v2 修正。同日用户再指出 v2 仍太常规；4 倍放大核对确认 O 为斜切断开的两段弧线、F 顶横为斜切平行四边形等定制细节，提示词已按 v3 修正。教训：小图的字体判断须放大核对，不能凭小图观感定字体类别；定制字标须逐字母拆解斜切、断口等特殊设计，不能只写字体大类。另：定制字标靠文字提示词只能接近、无法精确复现，精确复现需字体文件或矢量原稿。
