# Brand Sites - Quick Start Guide

## 🚀 快速开始

### 1. 安装依赖

```bash
cd /Users/admin/BrandSites
pip3 install -r requirements.txt
```

### 2. 设置 API Key

选择一个 AI 提供商（OpenAI 或 Anthropic）：

**使用 OpenAI:**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**使用 Anthropic:**
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

编辑 `src/config.py` 设置提供商：
```python
AI_PROVIDER = "openai"  # 或 "anthropic"
```

### 3. 测试运行

```bash
python3 main.py
```

这将：
- 选择 5 个品牌
- 使用 AI 分析每个品牌
- 生成 Markdown 文件到 `docs/_posts/`
- 更新推荐历史

### 4. 查看结果

生成的文件位于：
- `docs/_posts/YYYY-MM-DD-brand-sites.md` - Jekyll 文章
- `data/summaries/brands-YYYY-MM-DD.md` - 备份

### 5. 本地预览网站

```bash
cd docs
bundle install
bundle exec jekyll serve
```

访问 http://localhost:4000

### 6. 推送到 GitHub

```bash
# 创建 GitHub 仓库
# 然后：
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/brand-sites.git
git push -u origin main
```

### 7. 启用 GitHub Pages

1. 进入仓库 Settings → Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: /docs
5. Save

网站将发布到：`https://yourusername.github.io/brand-sites/`

### 8. 设置自动化（可选）

编辑 crontab：
```bash
crontab -e
```

添加：
```
0 8 * * * /Users/admin/BrandSites/run-brand-sites.sh >> /Users/admin/BrandSites/logs/cron.log 2>&1
```

这将每天早上 8 点自动运行。

## 📝 添加更多品牌

编辑 `data/brands.json`，添加新品牌：

```json
{
  "id": "unique-slug",
  "name": "Brand Name",
  "url": "https://www.example.com",
  "category": "Fashion",
  "subcategory": "Apparel",
  "region": "US",
  "founded": 2020,
  "tags": ["DTC", "Sustainable"],
  "description": "Brief description",
  "last_recommended": null,
  "recommendation_count": 0,
  "priority": "high"
}
```

## 🎨 自定义网站

编辑以下文件：
- `docs/_config.yml` - 网站配置
- `docs/assets/css/style.scss` - 样式
- `docs/_layouts/home.html` - 首页布局
- `docs/_layouts/default.html` - 文章布局

## 🔧 配置选项

编辑 `src/config.py`：

```python
# 每日推荐数量
DAILY_BRAND_COUNT = 5

# 重复推荐间隔（天）
REPEAT_THRESHOLD_DAYS = 30

# AI 提供商
AI_PROVIDER = "openai"  # 或 "anthropic"

# 评分权重
SCORE_WEIGHTS = {
    "design": 0.4,
    "user_experience": 0.3,
    "innovation": 0.3
}
```

## 🐛 故障排除

### API Key 错误
确保环境变量已设置：
```bash
echo $OPENAI_API_KEY
```

### 没有生成文件
检查日志：
```bash
python3 main.py
```

### Git 推送失败
确保已设置远程仓库：
```bash
git remote -v
```

## 📊 数据结构

### brands.json
存储所有品牌信息和推荐历史

### history.json
记录每日推荐的品牌 ID

### docs/_posts/
Jekyll 文章，按日期命名

## 🎯 下一步

1. 扩充品牌数据库（目标 100+ 品牌）
2. 优化 AI 分析提示词
3. 添加品牌截图
4. 集成流量数据 API
5. 添加用户反馈功能

## 💡 提示

- 定期更新品牌数据库
- 检查失效的品牌链接
- 调整 AI 提示词以获得更好的分析
- 监控 API 使用量和成本

---

**需要帮助？** 查看 README.md 或提交 Issue
