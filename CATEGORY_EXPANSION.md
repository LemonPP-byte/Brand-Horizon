# Brand-Horizon Category Expansion

## Overview
扩展了品牌搜索范围，从原来的 8 个基础类别扩展到覆盖所有消费品类别，并准备了 70 个精准的搜索关键词。

## 扩展的类别层级

### 1. Fashion & Apparel (时尚服饰)
- Footwear (鞋类)
- Activewear & Sportswear (运动服饰)
- Denim & Casual Wear (牛仔休闲装)
- Outerwear & Jackets (外套夹克)
- Underwear & Intimates (内衣)
- Accessories & Jewelry (配饰珠宝)
- Eyewear (眼镜)
- Watches (手表)
- Bags & Luggage (包袋行李箱)
- Sustainable Fashion (可持续时尚)

### 2. Beauty & Personal Care (美妆个护)
- Skincare (护肤)
- Makeup & Cosmetics (彩妆)
- Haircare (护发)
- Fragrance (香水)
- Men's Grooming (男士理容)
- Clean Beauty (清洁美妆)
- K-Beauty & J-Beauty (韩妆日妆)
- Nail Care (美甲)
- Bath & Body (沐浴身体护理)

### 3. Home & Living (家居生活)
- Furniture (家具)
- Bedding & Linens (床品)
- Mattresses & Sleep (床垫睡眠)
- Home Decor (家居装饰)
- Kitchenware & Cookware (厨具餐具)
- Lighting (灯具)
- Storage & Organization (收纳整理)
- Smart Home (智能家居)
- Plants & Gardening (植物园艺)

### 4. Food & Beverage (食品饮料)
- Snacks & Chips (零食薯片)
- Coffee & Tea (咖啡茶饮)
- Meal Kits & Prepared Foods (预制食品)
- Protein & Nutrition (蛋白营养)
- Chocolate & Candy (巧克力糖果)
- Beverages & Drinks (饮料)
- Alcohol & Wine (酒类)
- Specialty Foods (特色食品)
- Baby Food & Formula (婴儿食品)

### 5. Health & Wellness (健康养生)
- Vitamins & Supplements (维生素补剂)
- Fitness Equipment (健身器材)
- Sexual Wellness (性健康)
- Mental Health & Meditation (心理健康冥想)
- Sleep & Recovery (睡眠恢复)
- Women's Health (女性健康)
- Men's Health (男性健康)
- CBD & Hemp Products (CBD 大麻产品)
- Medical Devices (医疗器械)

### 6. Baby & Kids (母婴儿童)
- Baby Gear & Strollers (婴儿用品推车)
- Diapers & Wipes (尿布湿巾)
- Baby Clothing (婴儿服装)
- Toys & Games (玩具游戏)
- Kids Furniture (儿童家具)
- Educational Products (教育产品)
- Baby Food & Feeding (婴儿食品喂养)

### 7. Pet Care (宠物护理)
- Pet Food (宠物食品)
- Pet Toys & Accessories (宠物玩具配件)
- Pet Health & Wellness (宠物健康)
- Pet Furniture & Beds (宠物家具床)

### 8. Electronics & Tech (电子科技)
- Audio & Headphones (音频耳机)
- Wearables & Smartwatches (可穿戴设备)
- Phone Accessories (手机配件)
- Cameras & Photography (相机摄影)
- Gaming Accessories (游戏配件)
- Smart Devices (智能设备)

### 9. Outdoor & Sports (户外运动)
- Camping & Hiking (露营徒步)
- Cycling (骑行)
- Water Sports (水上运动)
- Fitness & Yoga (健身瑜伽)
- Golf (高尔夫)
- Running (跑步)

### 10. Personal Electronics (个人电子产品)
- E-readers & Tablets (电子阅读器平板)
- Laptops & Computers (笔记本电脑)
- Phone Cases & Protection (手机壳保护)

## 70 个搜索关键词

### Fashion & Apparel (15 个)
1. sustainable fashion brand
2. direct-to-consumer shoes
3. minimalist clothing brand
4. activewear brand
5. denim brand
6. luxury accessories
7. eyewear brand
8. watch brand
9. jewelry brand
10. luggage brand
11. underwear brand
12. outerwear brand
13. sustainable footwear

### Beauty & Personal Care (11 个)
14. clean beauty brand
15. skincare brand
16. makeup brand
17. haircare brand
18. men's grooming
19. fragrance brand
20. k-beauty brand
21. natural cosmetics
22. vegan beauty
23. anti-aging skincare
24. organic beauty

### Home & Living (10 个)
25. modern furniture brand
26. mattress brand
27. bedding brand
28. home decor brand
29. kitchenware brand
30. smart home brand
31. lighting brand
32. sustainable furniture
33. luxury linens
34. cookware brand

### Food & Beverage (10 个)
35. healthy snacks brand
36. coffee brand
37. meal kit delivery
38. protein bar brand
39. craft beverage
40. specialty food brand
41. organic food brand
42. chocolate brand
43. tea brand
44. nutrition brand

### Health & Wellness (10 个)
45. vitamin brand
46. supplement brand
47. fitness equipment
48. wellness brand
49. meditation app
50. sexual wellness
51. women's health
52. cbd brand
53. sleep aid brand
54. mental health app

### Baby & Kids (5 个)
55. baby products brand
56. kids toys brand
57. baby gear brand
58. children's furniture
59. baby food brand

### Pet Care (4 个)
60. pet food brand
61. dog toys brand
62. pet wellness
63. pet accessories

### Electronics & Tech (4 个)
64. headphones brand
65. smartwatch brand
66. audio brand
67. wearable tech

### Outdoor & Sports (3 个)
68. outdoor gear brand
69. yoga brand
70. camping equipment

## 技术实现

### 新增文件
1. `src/categories_extended.py` - 扩展的类别定义和 70 个搜索关键词
2. `src/brand_discovery.py` - 品牌发现工具，用于组织和管理搜索计划
3. `data/search_plan.json` - 生成的搜索计划，包含关键词到类别的映射

### 更新文件
1. `src/config.py` - 更新了类别列表，导入扩展的类别定义

## 使用方法

### 生成搜索计划
```bash
cd /Users/admin/Brand-Horizon
python3 src/brand_discovery.py
```

### 查看搜索计划
搜索计划保存在 `data/search_plan.json`，包含：
- 总关键词数量
- 按类别组织的关键词
- 每个关键词对应的类别和子类别

## 下一步

1. **品牌数据收集** - 使用这 70 个关键词搜索和收集品牌数据
2. **数据库扩充** - 将发现的品牌添加到 `data/brands.json`
3. **自动化搜索** - 开发自动化工具定期搜索新品牌
4. **质量评估** - 对收集的品牌进行设计和用户体验评分

## 覆盖范围

- **10 个主要类别**
- **60+ 个子类别**
- **70 个精准搜索关键词**
- **覆盖所有主流消费品领域**

这次扩展大大增加了品牌发现的广度和深度，为每日推荐提供了更丰富的品牌池。
