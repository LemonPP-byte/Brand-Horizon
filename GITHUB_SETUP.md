# 创建 GitHub 仓库并推送 - 操作指南

## 步骤 1: 在 GitHub 上创建仓库

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `brand-sites`
   - Description: `Daily DTC brand website inspiration, curated by AI`
   - Public 或 Private（推荐 Public）
   - ❌ 不要勾选 "Add a README file"
   - ❌ 不要勾选 "Add .gitignore"
   - ❌ 不要勾选 "Choose a license"
3. 点击 "Create repository"

## 步骤 2: 推送代码到 GitHub

创建完仓库后，GitHub 会显示推送命令。执行以下命令：

```bash
cd /Users/admin/BrandSites

# 添加远程仓库（替换 yourusername 为你的 GitHub 用户名）
git remote add origin https://github.com/yourusername/brand-sites.git

# 推送代码
git push -u origin main
```

## 步骤 3: 启用 GitHub Pages

1. 进入仓库页面
2. 点击 Settings（设置）
3. 左侧菜单找到 Pages
4. 在 "Build and deployment" 下：
   - Source: 选择 "Deploy from a branch"
   - Branch: 选择 `main`
   - Folder: 选择 `/docs`
5. 点击 Save

等待 1-2 分钟，网站将发布到：
`https://yourusername.github.io/brand-sites/`

## 步骤 4: 验证部署

访问你的网站 URL，应该能看到：
- 首页显示今天的 5 个品牌推荐
- 归档页面显示历史记录
- 点击日期可以查看完整文章

## 自动推送配置

如果你想让每日更新自动推送到 GitHub，需要：

1. 生成 GitHub Personal Access Token:
   - 访问 https://github.com/settings/tokens
   - Generate new token (classic)
   - 勾选 `repo` 权限
   - 复制 token

2. 配置 Git 使用 token:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/yourusername/brand-sites.git
```

3. 测试推送:
```bash
git push origin main
```

## 完成！

现在你的 Brand Sites 项目已经：
- ✅ 托管在 GitHub
- ✅ 发布到 GitHub Pages
- ✅ 可以通过 URL 访问
- ✅ 每次推送自动更新网站

---

**需要帮助？** 如果遇到问题，告诉我具体的错误信息。
