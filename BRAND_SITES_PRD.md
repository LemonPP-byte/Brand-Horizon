# 欧美品牌独立站每日推荐系统 PRD

## 1. 产品概述

### 1.1 产品定位
每日自动推荐 5 个欧美热门品牌独立站，帮助用户发现优秀的 DTC（Direct-to-Consumer）品牌和独立站设计案例。

### 1.2 目标用户
- 电商从业者
- 独立站运营者
- 品牌营销人员
- 设计师和开发者
- 跨境电商创业者

### 1.3 核心价值
- 每日精选 5 个优质品牌独立站
- AI 分析品牌特点、设计亮点、营销策略
- 自动化推送到 GitHub Pages
- 提供品牌分类、行业标签、流量估算

## 2. 功能需求

### 2.1 数据源
**品牌独立站数据库**
- 手动维护的品牌列表（初始 100-200 个）
- 数据字段：
  - 品牌名称
  - 网站 URL
  - 行业分类（Fashion, Beauty, Home, Tech, Food, etc.）
  - 地区（US, UK, EU）
  - 成立年份
  - 特色标签（DTC, Sustainable, Minimalist, etc.）
  - 流量估算（可选，通过 API 获取）

**外部数据源（可选）**
- SimilarWeb API（流量数据）
- BuiltWith API（技术栈）
- 社交媒体数据（Instagram, TikTok 粉丝数）

### 2.2 推荐算法
**每日选择逻辑**
- 从数据库中随机选择 5 个品牌
- 确保不重复推荐（30 天内）
- 行业分类平衡（不同类别轮换）
- 优先级权重：
  - 未推荐过的品牌（高优先级）
  - 最近更新的品牌（中优先级）
  - 热门品牌（定期重复推荐）

### 2.3 AI 分析
**每个品牌生成内容**
- 品牌简介（1-2 句话）
- 设计亮点（UI/UX 特色）
- 营销策略（独特卖点）
- 目标受众
- 值得学习的地方
- 评分（设计、用户体验、创新性）

### 2.4 输出格式
**Markdown 文件**
```markdown
---
layout: default
title: "Brand Sites Digest: 2026-03-06"
date: 2026-03-06
---

> 5 curated brand sites selected from our database

---

1. [Brand Name](#brand-1) ⭐️ 8.5/10
2. [Brand Name](#brand-2) ⭐️ 9.0/10
...

---

<a id="brand-1"></a>
## [Brand Name](https://example.com) ⭐️ 8.5/10

Brief description...

**Category**: Fashion | **Region**: US | **Founded**: 2020

**Design Highlights**: ...
**Marketing Strategy**: ...
**Target Audience**: ...

**Tags**: `#DTC`, `#Sustainable`, `#Minimalist`

---
```

## 3. 技术架构

### 3.1 项目结构
```
brand-sites/
├── data/
│   ├── brands.json          # 品牌数据库
│   ├── history.json         # 推荐历史
│   └── summaries/           # 生成的摘要
├── docs/
│   ├── _posts/              # Jekyll 文章
│   ├── _layouts/            # 页面布局
│   ├── assets/              # CSS/JS
│   └── index.md             # 首页
├── src/
│   ├── selector.py          # 品牌选择逻辑
│   ├── analyzer.py          # AI 分析
│   ├── generator.py         # Markdown 生成
│   └── config.py            # 配置文件
├── run-brand-sites.sh       # 定时任务脚本
└── README.md
```

### 3.2 技术栈
- **语言**: Python 3.10+
- **AI**: OpenAI API / Claude API
- **网站**: GitHub Pages + Jekyll
- **定时任务**: Cron / GitHub Actions
- **数据存储**: JSON 文件

### 3.3 核心模块

**1. Brand Selector (selector.py)**
- 从 brands.json 读取品牌列表
- 应用推荐算法选择 5 个品牌
- 更新 history.json 避免重复

**2. AI Analyzer (analyzer.py)**
- 调用 AI API 分析品牌网站
- 生成品牌简介、设计亮点等
- 评分（设计、体验、创新）

**3. Content Generator (generator.py)**
- 生成 Markdown 文件
- 复制到 docs/_posts/
- 格式化输出

**4. Automation Script (run-brand-sites.sh)**
- 每日自动运行
- Git commit & push
- 错误日志记录

## 4. 数据结构

### 4.1 brands.json
```json
{
  "brands": [
    {
      "id": "allbirds",
      "name": "Allbirds",
      "url": "https://www.allbirds.com",
      "category": "Fashion",
      "subcategory": "Footwear",
      "region": "US",
      "founded": 2016,
      "tags": ["DTC", "Sustainable", "Minimalist"],
      "description": "Sustainable footwear brand",
      "last_recommended": null,
      "recommendation_count": 0,
      "priority": "high"
    }
  ]
}
```

### 4.2 history.json
```json
{
  "recommendations": [
    {
      "date": "2026-03-06",
      "brands": ["allbirds", "glossier", "warby-parker", "casper", "away"]
    }
  ]
}
```

## 5. 网站设计

### 5.1 首页布局
- **Hero 区域**: 简洁导航栏
- **今日推荐**: 显示今天的 5 个品牌（可展开）
- **归档**: 按日期浏览历史推荐
- **分类筛选**: 按行业、地区筛选品牌

### 5.2 品牌详情页
- 品牌截图（可选）
- 完整分析内容
- 相关品牌推荐
- 外部链接

## 6. 实施计划

### Phase 1: MVP（1-2 周）
- [ ] 创建品牌数据库（50 个品牌）
- [ ] 实现随机选择算法
- [ ] AI 分析集成
- [ ] 基础网站搭建
- [ ] 手动运行测试

### Phase 2: 自动化（1 周）
- [ ] 定时任务配置
- [ ] GitHub Actions 集成
- [ ] 错误处理和日志
- [ ] 邮件通知（可选）

### Phase 3: 优化（持续）
- [ ] 扩充品牌数据库（200+）
- [ ] 添加流量数据
- [ ] 改进推荐算法
- [ ] 用户反馈收集
- [ ] SEO 优化

## 7. 成功指标

- 每日成功推送率 > 95%
- 品牌数据库规模 > 200
- 网站访问量增长
- 用户停留时间 > 2 分钟
- 社交媒体分享数

## 8. 风险与挑战

### 8.1 数据质量
- **风险**: 品牌信息过时、网站失效
- **解决**: 定期验证链接、更新数据

### 8.2 AI 分析准确性
- **风险**: AI 生成内容质量不稳定
- **解决**: Prompt 优化、人工审核

### 8.3 版权问题
- **风险**: 品牌截图使用权限
- **解决**: 仅使用文字描述，或获取授权

## 9. 未来扩展

- 用户投票功能
- 品牌提交表单
- 邮件订阅推送
- 移动端 App
- 品牌对比工具
- 设计趋势分析报告

---

**文档版本**: v1.0
**创建日期**: 2026-03-06
**负责人**: Product Team
