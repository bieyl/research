#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音交互模块
Voice Interface - 语音指令识别与执行
"""

import sys
from typing import Optional


class VoiceInterface:
    """语音交互接口"""
    
    # 支持指令
    COMMANDS = {
        '总结这篇论文': 'summarize',
        '生成实验日报': 'lablog',
        '导出参考文献': 'reference',
        '打开文献列表': 'papers',
        '退出': 'exit',
    }
    
    def __init__(self):
        """初始化接口"""
        self.recognizer = None
        self._init_recognizer()
    
    def _init_recognizer(self):
        """初始化语音识别器"""
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
        except ImportError:
            print("⚠️  speech_recognition 未安装，语音功能受限")
            self.recognizer = None
    
    def listen(self) -> Optional[str]:
        """
        监听语音输入
        
        Returns:
            识别的文本，失败返回 None
        """
        if self.recognizer is None:
            return None
        
        try:
            import speech_recognition as sr
            
            with sr.Microphone() as source:
                print("🎤 请说话...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, phrase_time_limit=5)
            
            # 使用 Google 识别
            text = self.recognizer.recognize_google(audio, language='zh-CN')
            return text
            
        except Exception as e:
            print(f"语音识别失败：{e}")
            return None
    
    def parse_command(self, text: str) -> Optional[str]:
        """
        解析语音指令
        
        Args:
            text: 识别的文本
            
        Returns:
            命令类型，未知返回 None
        """
        text = text.strip()
        
        for command, cmd_type in self.COMMANDS.items():
            if command in text:
                return cmd_type
        
        return None
    
    def execute_command(self, cmd_type: str):
        """
        执行命令
        
        Args:
            cmd_type: 命令类型
        """
        print(f"执行命令：{cmd_type}")
        
        if cmd_type == 'summarize':
            print("📚 请提供论文 PDF 文件路径...")
            # 实际项目中调用 summarizer
        
        elif cmd_type == 'lablog':
            print("📝 请说出实验数据...")
            # 实际项目中调用 lab_log
        
        elif cmd_type == 'reference':
            print("📖 请说出参考文献信息...")
            # 实际项目中调用 reference_formatter
        
        elif cmd_type == 'exit':
            print("👋 再见！")
            sys.exit(0)
    
    def listen_and_execute(self):
        """循环监听并执行命令"""
        print("\n" + "=" * 50)
        print("语音交互模式已启动")
        print("说'退出'结束程序")
        print("=" * 50 + "\n")
        
        while True:
            # 监听
            text = self.listen()
            
            if text:
                print(f"识别结果：{text}")
                
                # 解析命令
                cmd_type = self.parse_command(text)
                
                if cmd_type:
                    # 执行命令
                    self.execute_command(cmd_type)
                else:
                    print("❌ 未识别的指令，请重试")
            else:
                print("❌ 未听到声音，请重试")


# 测试代码
if __name__ == '__main__':
    interface = VoiceInterface()
    
    # 测试（需要麦克风）
    # interface.listen_and_execute()
    
    # 模拟测试
    print("语音交互模块测试")
    print("支持指令：")
    for cmd, cmd_type in interface.COMMANDS.items():
        print(f"  • '{cmd}' → {cmd_type}")
