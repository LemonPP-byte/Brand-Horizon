#!/bin/bash

# Brand Sites 自动运行脚本
# 每天早上 8 点运行，选择品牌并推送到 GitHub

# 设置工作目录
cd /Users/admin/BrandSites

# 激活虚拟环境
source venv/bin/activate

# 设置 API Keys (从环境变量读取)
export DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY:-sk-0438686478f34f54aca3e27cee5c4a0a}"

# 运行主程序
echo "$(date): Starting Brand Sites selection..."
python3 main.py

# 检查是否成功
if [ $? -eq 0 ]; then
    echo "$(date): Selection completed successfully"

    # 推送到 GitHub
    git add docs/_posts/*.md data/*.json
    git commit -m "Daily brand sites update - $(date +%Y-%m-%d)

Co-Authored-By: Claude Sonnet 4.6 (1M context) <noreply@anthropic.com>"
    git push origin main

    echo "$(date): Pushed to GitHub"
else
    echo "$(date): Selection failed"
    exit 1
fi
