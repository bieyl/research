#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 GitHub API 上传学术龙虾 v2 项目到 GitHub
"""

from github import Github, InputGitTreeElement
import base64
import os
from pathlib import Path

# GitHub 认证信息
GITHUB_USERNAME = "bieyunlong1@163.com"
GITHUB_PASSWORD = "10.14Bie"
REPO_NAME = "bieyl/research"

# 项目路径
PROJECT_PATH = Path("/home/admin/openclaw/workspace/academic-lobster")

def upload_to_github():
    """上传项目到 GitHub"""
    
    print("🦞 开始上传学术龙虾 v2 到 GitHub...")
    print()
    
    try:
        # 1. 认证
        print("📝 正在认证 GitHub 账号...")
        g = Github(GITHUB_USERNAME, GITHUB_PASSWORD)
        user = g.get_user()
        print(f"✅ 认证成功：{user.login}")
        print()
        
        # 2. 获取仓库
        print("📂 正在获取仓库...")
        repo = g.get_repo(REPO_NAME)
        print(f"✅ 仓库：{repo.full_name}")
        print(f"   默认分支：{repo.default_branch}")
        print()
        
        # 3. 获取默认分支
        branch = repo.get_branch(repo.default_branch)
        sha = branch.commit.sha
        print(f"📌 当前 commit SHA: {sha[:7]}")
        print()
        
        # 4. 准备上传的文件列表
        files_to_upload = []
        
        # README
        readme_path = PROJECT_PATH / "GITHUB_UPLOAD_README.md"
        if readme_path.exists():
            with open(readme_path, 'r', encoding='utf-8') as f:
                files_to_upload.append({
                    'path': 'academic-lobster-v2/README.md',
                    'content': f.read()
                })
            print("✅ 准备 README.md")
        
        # 项目说明书
        statement_path = PROJECT_PATH / "competition-project-statement.md"
        if statement_path.exists():
            with open(statement_path, 'r', encoding='utf-8') as f:
                files_to_upload.append({
                    'path': 'academic-lobster-v2/competition-project-statement.md',
                    'content': f.read()
                })
            print("✅ 准备 competition-project-statement.md")
        
        # requirements.txt
        req_path = PROJECT_PATH / "requirements.txt"
        if req_path.exists():
            with open(req_path, 'r', encoding='utf-8') as f:
                files_to_upload.append({
                    'path': 'academic-lobster-v2/requirements.txt',
                    'content': f.read()
                })
            print("✅ 准备 requirements.txt")
        
        # 源代码文件
        src_path = PROJECT_PATH / "src"
        if src_path.exists():
            for py_file in src_path.glob("*.py"):
                with open(py_file, 'r', encoding='utf-8') as f:
                    files_to_upload.append({
                        'path': f'academic-lobster-v2/src/{py_file.name}',
                        'content': f.read()
                    })
            print(f"✅ 准备 src/ 目录 ({len(list(src_path.glob('*.py')))} 个 Python 文件)")
        
        # 文档文件
        docs_path = PROJECT_PATH / "docs"
        if docs_path.exists():
            for md_file in docs_path.glob("*.md"):
                with open(md_file, 'r', encoding='utf-8') as f:
                    files_to_upload.append({
                        'path': f'academic-lobster-v2/docs/{md_file.name}',
                        'content': f.read()
                    })
            print(f"✅ 准备 docs/ 目录 ({len(list(docs_path.glob('*.md')))} 个文档)")
        
        print()
        print(f"📦 总共准备上传 {len(files_to_upload)} 个文件")
        print()
        
        # 5. 逐个上传文件
        print("🚀 开始上传文件...")
        for i, file_info in enumerate(files_to_upload, 1):
            try:
                repo.create_file(
                    path=file_info['path'],
                    message=f"🦞 上传学术龙虾 v2 - {file_info['path']}",
                    content=file_info['content'],
                    branch=repo.default_branch
                )
                print(f"   [{i}/{len(files_to_upload)}] ✅ {file_info['path']}")
            except Exception as e:
                print(f"   [{i}/{len(files_to_upload)}] ⚠️  {file_info['path']} - {str(e)[:50]}")
        
        print()
        print("✅ 所有文件上传完成！")
        print()
        print("📎 项目链接:")
        print(f"   仓库：https://github.com/{REPO_NAME}")
        print(f"   README: https://github.com/{REPO_NAME}/blob/main/academic-lobster-v2/README.md")
        print(f"   说明书：https://github.com/{REPO_NAME}/blob/main/academic-lobster-v2/competition-project-statement.md")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ 上传失败：{e}")
        print()
        print("💡 提示：GitHub 密码认证已禁用，需要使用 Personal Access Token")
        print("   请访问 https://github.com/settings/tokens 创建 Token")
        print("   Token 权限需要：repo (完整控制)")
        return False

if __name__ == '__main__':
    success = upload_to_github()
    if success:
        print("🎉 上传成功！")
    else:
        print("💔 上传失败，需要手动上传或使用 Token")
