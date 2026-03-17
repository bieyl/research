#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 v2 - 演示视频自动截图脚本

功能：自动操作浏览器，截取每个功能模块的截图
用途：用于合成演示视频或制作 GIF
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import json


def create_screenshots():
    """自动生成演示截图"""
    
    print("=" * 60)
    print("🦞 学术龙虾 v2 - 自动截图")
    print("=" * 60)
    
    # 配置 Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # 截图保存目录
    output_dir = Path("/tmp/lobster_demo_screenshots")
    output_dir.mkdir(exist_ok=True)
    
    try:
        # 1. 首页
        print("\n【截图 1】首页...")
        driver.get("http://localhost:5001")
        time.sleep(2)
        driver.save_screenshot(str(output_dir / "01_home.png"))
        
        # 2. 添加论文弹窗
        print("\n【截图 2】添加论文...")
        add_paper_btn = driver.find_element(By.XPATH, "//button[contains(text(), '添加论文')]")
        add_paper_btn.click()
        time.sleep(1)
        driver.save_screenshot(str(output_dir / "02_add_paper.png"))
        
        # 3. 知识图谱视图
        print("\n【截图 3】知识图谱...")
        # 先添加一些数据
        import requests
        paper_data = {
            "title": "Deep Residual Learning for Image Recognition",
            "authors": ["He K", "Zhang X", "Ren S", "Sun J"],
            "year": 2016,
            "research_question": "深层网络训练退化问题",
            "method": "残差连接",
            "conclusion": "可训练 152 层网络",
            "keywords": ["深度学习", "残差学习", "图像分类"],
            "category": "计算机视觉"
        }
        requests.post("http://localhost:5001/api/kg/paper", json=paper_data)
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        driver.save_screenshot(str(output_dir / "03_knowledge_graph.png"))
        
        # 4. 智能推荐
        print("\n【截图 4】智能推荐...")
        textarea = driver.find_element(By.XPATH, "//textarea[contains(@placeholder, '实验描述')]")
        textarea.send_keys("使用注意力机制改进 ResNet 图像分类")
        time.sleep(1)
        recommend_btn = driver.find_element(By.XPATH, "//button[contains(text(), '获取推荐')]")
        recommend_btn.click()
        time.sleep(3)
        driver.save_screenshot(str(output_dir / "04_recommendation.png"))
        
        # 5. 文献摘要
        print("\n【截图 5】文献摘要...")
        summary_textarea = driver.find_element(By.XPATH, "//textarea[contains(@placeholder, '论文标题')]")
        summary_textarea.send_keys("ResNet")
        time.sleep(1)
        summary_btn = driver.find_element(By.XPATH, "//button[contains(text(), '生成摘要')]")
        summary_btn.click()
        time.sleep(3)
        driver.save_screenshot(str(output_dir / "05_summary.png"))
        
        # 6. 实验日志
        print("\n【截图 6】实验日志...")
        lablog_textarea = driver.find_element(By.XPATH, "//textarea[contains(@placeholder, '实验数据')]")
        lablog_textarea.send_keys("温度 60/70/80 度，收率 45%/62%/38%")
        time.sleep(1)
        lablog_btn = driver.find_element(By.XPATH, "//button[contains(text(), '生成报告')]")
        lablog_btn.click()
        time.sleep(3)
        driver.save_screenshot(str(output_dir / "06_lablog.png"))
        
        # 7. 统计卡片
        print("\n【截图 7】统计卡片...")
        driver.refresh()
        time.sleep(2)
        driver.save_screenshot(str(output_dir / "07_stats.png"))
        
        print("\n" + "=" * 60)
        print(f"✅ 截图完成！共 7 张")
        print(f"📁 保存目录：{output_dir}")
        print("=" * 60)
        
        # 生成 FFmpeg 合成命令
        print("\n🎬 使用 FFmpeg 合成视频:")
        print(f"""
cd {output_dir}
ffmpeg -framerate 1/3 -i screenshot_%02d.png -c:v libx264 -pix_fmt yuv420p -vf "scale=1920:1080" demo_video.mp4
        """)
        
        # 保存截图列表
        screenshot_list = [
            "01_home.png - 首页展示",
            "02_add_paper.png - 添加论文",
            "03_knowledge_graph.png - 知识图谱",
            "04_recommendation.png - 智能推荐",
            "05_summary.png - 文献摘要",
            "06_lablog.png - 实验日志",
            "07_stats.png - 统计卡片"
        ]
        
        with open(output_dir / "README.txt", "w", encoding="utf-8") as f:
            f.write("学术龙虾 v2 - 演示视频截图\n\n")
            f.write("\n".join(screenshot_list))
        
        print(f"\n📄 截图列表已保存：{output_dir / 'README.txt'}")
        
    except Exception as e:
        print(f"\n❌ 错误：{e}")
        import traceback
        traceback.print_exc()
    
    finally:
        driver.quit()


if __name__ == '__main__':
    create_screenshots()
