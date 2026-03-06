#!/bin/bash

# Brand Sites 自动运行脚本
# 每天早上 8 点运行，选择品牌并推送到 GitHub

# 设置工作目录
cd /Users/admin/BrandSites

# 设置 PATH
export PATH="$HOME/.local/bin:$PATH"

# 设置 API Keys (从环境变量读取)
export OPENAI_API_KEY="${OPENAI_API_KEY}"
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}"

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
