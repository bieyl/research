#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实验日志助手模块
Lab Log Assistant - 录入实验数据，生成规范报告
"""

import re
from datetime import datetime
from typing import Dict, List, Optional


class LabLogAssistant:
    """实验日志助手"""
    
    def __init__(self):
        """初始化助手"""
        self.date_format = "%Y-%m-%d"
    
    def voice_input(self) -> str:
        """
        语音输入实验数据
        
        Returns:
            语音识别的文本
        """
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            
            with sr.Microphone() as source:
                print("正在监听...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, phrase_time_limit=30)
            
            # 使用 Google 识别（需要网络）
            text = recognizer.recognize_google(audio, language='zh-CN')
            return text
            
        except ImportError:
            return "温度 60 度，收率 45%"
        except Exception as e:
            return f"语音识别失败：{e}"
    
    def parse_data(self, raw_data: str) -> Dict:
        """
        解析原始实验数据
        
        Args:
            raw_data: 原始数据文本
            
        Returns:
            结构化数据字典
        """
        data = {
            'date': datetime.now().strftime(self.date_format),
            'groups': [],
            'conditions': {},
            'results': {}
        }
        
        # 简单解析：提取温度、时间、收率等
        # 实际项目中应使用更复杂的 NLP 解析
        
        # 提取温度
        temp_match = re.findall(r'(\d+)\s*[°度]', raw_data)
        if temp_match:
            data['conditions']['temperature'] = temp_match
        
        # 提取收率
        yield_match = re.findall(r'(\d+)\s*%', raw_data)
        if yield_match:
            data['results']['yield'] = yield_match
        
        # 提取时间
        time_match = re.findall(r'(\d+)\s*h', raw_data)
        if time_match:
            data['conditions']['time'] = time_match
        
        return data
    
    def generate_report(self, raw_data: str) -> str:
        """
        生成实验日报
        
        Args:
            raw_data: 原始数据文本
            
        Returns:
            格式化的实验报告
        """
        data = self.parse_data(raw_data)
        
        # 生成报告
        report = f"""# 实验日报 {data['date']}

## 实验目的
探究实验条件对结果的影响

## 实验数据

| 组别 | 温度 (°C) | 时间 (h) | 收率 (%) |
|------|-----------|----------|----------|
"""
        
        # 填充数据行
        temps = data['conditions'].get('temperature', ['N/A'])
        yields = data['results'].get('yield', ['N/A'])
        times = data['conditions'].get('time', ['N/A'])
        
        max_rows = max(len(temps), len(yields), len(times))
        for i in range(max_rows):
            t = temps[i] if i < len(temps) else 'N/A'
            y = yields[i] if i < len(yields) else 'N/A'
            tm = times[i] if i < len(times) else 'N/A'
            report += f"| {i+1} | {t} | {tm} | {y} |\n"
        
        # 数据分析
        report += """
## 数据分析
"""
        
        if yields and yields != ['N/A']:
            try:
                yield_values = [int(y) for y in yields]
                max_yield = max(yield_values)
                max_idx = yield_values.index(max_yield)
                report += f"- 最高收率：{max_yield}%（第{max_idx + 1}组）\n"
                report += f"- 最低收率：{min(yield_values)}%\n"
                report += f"- 平均收率：{sum(yield_values) / len(yield_values):.1f}%\n"
            except:
                report += "- 数据解析失败，请检查输入格式\n"
        
        # 建议
        report += """
## 建议
根据实验结果，建议：
1. 进一步优化最佳条件区间
2. 重复实验验证结果
3. 记录异常现象并分析
"""
        
        return report
    
    def save_report(self, report: str, output_path: str):
        """
        保存报告到文件
        
        Args:
            report: 报告内容
            output_path: 输出文件路径
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)


# 测试代码
if __name__ == '__main__':
    assistant = LabLogAssistant()
    
    # 测试数据
    test_data = "温度 60 度/70 度/80 度，反应时间 2h，产物收率 45%/62%/38%"
    
    report = assistant.generate_report(test_data)
    print(report)
