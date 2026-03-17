#!/bin/bash

# 学术龙虾 v2 - GitHub 推送脚本
# 使用方法：./push-to-github.sh

set -e

echo "🦞 学术龙虾 v2 - GitHub 推送脚本"
echo "================================"
echo ""

# 检查是否在正确的目录
if [ ! -f "README.md" ]; then
    echo "❌ 错误：请在 research 目录下运行此脚本"
    exit 1
fi

# 检查 git 状态
echo "📊 检查 Git 状态..."
git status
echo ""

# 询问推送方式
echo "请选择推送方式："
echo "1) 使用 Personal Access Token"
echo "2) 使用 SSH"
echo "3) 仅本地提交，稍后手动推送"
echo ""
read -p "请输入选项 (1/2/3): " choice

case $choice in
    1)
        read -p "请输入你的 GitHub Personal Access Token: " -s token
        echo ""
        
        # 设置 remote URL（包含 token）
        git remote set-url origin https://$token@github.com/bieyl/research.git
        
        echo "🚀 推送到 GitHub..."
        git push origin main
        
        echo ""
        echo "✅ 推送成功！"
        echo "📱 请移除 token 以保安全..."
        git remote set-url origin https://github.com/bieyl/research.git
        ;;
        
    2)
        # 检查 SSH key
        if [ ! -f ~/.ssh/id_ed25519.pub ] && [ ! -f ~/.ssh/id_rsa.pub ]; then
            echo "❌ 未找到 SSH key，请先创建："
            echo "   ssh-keygen -t ed25519 -C 'your_email@example.com'"
            echo "   然后添加到 GitHub: https://github.com/settings/keys"
            exit 1
        fi
        
        # 切换为 SSH remote
        git remote set-url origin git@github.com:bieyl/research.git
        
        echo "🚀 推送到 GitHub..."
        git push origin main
        
        echo ""
        echo "✅ 推送成功！"
        ;;
        
    3)
        echo "ℹ️  已保存本地提交"
        echo ""
        echo "稍后手动推送的方法："
        echo ""
        echo "方式 1 - 使用 Token:"
        echo "  git remote set-url origin https://<YOUR_TOKEN>@github.com/bieyl/research.git"
        echo "  git push origin main"
        echo ""
        echo "方式 2 - 使用 SSH:"
        echo "  git remote set-url origin git@github.com:bieyl/research.git"
        echo "  git push origin main"
        echo ""
        echo "方式 3 - GitHub Desktop:"
        echo "  1. 下载 GitHub Desktop: https://desktop.github.com/"
        echo "  2. 克隆仓库到本地"
        echo "  3. 将更改的文件复制过去"
        echo "  4. 在 GitHub Desktop 中 commit 并 push"
        ;;
        
    *)
        echo "❌ 无效选项"
        exit 1
        ;;
esac

echo ""
echo "🎉 完成！"
echo ""
echo "📋 下一步："
echo "1. 访问 https://github.com/bieyl/research 确认更新"
echo "2. 检查 README.md 和 README_zh.md 是否正确显示"
echo "3. 回复组委会正确的链接（见下方）"
echo ""
echo "📧 回复组委会模板："
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "尊敬的组委会："
echo ""
echo "感谢您对参赛材料的审核！我已确认并修复所有链接问题，以下是正确的参赛材料链接："
echo ""
echo "【项目说明书】"
echo "链接：https://github.com/bieyl/research"
echo "说明：仓库主页，包含完整的中英文 README 和文档"
echo ""
echo "【代码仓库】"
echo "链接：https://github.com/bieyl/research"
echo "说明：公开仓库，所有源代码、文档和测试用例"
echo ""
echo "【项目海报】"
echo "链接：https://github.com/bieyl/research/blob/main/assets/PROJECT-POSTER.md"
echo "说明：海报 Markdown 源文件（可渲染预览）"
echo ""
echo "【演示视频】"
echo "状态：正在准备，稍后提供 B 站链接"
echo "备选：https://github.com/bieyl/research/blob/main/assets/demo-presentation.html"
echo ""
echo "仓库已确认为 Public 状态，评委可直接访问。"
echo "如有其他问题，请随时告知。"
echo ""
echo "参赛者：别云龙"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
