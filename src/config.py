#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理模块
Configuration Manager - 管理用户配置和数据目录
"""

import os
import json
from pathlib import Path
from typing import Dict, Any


class Config:
    """配置管理器"""
    
    DEFAULT_CONFIG = {
        'data_dir': '~/.academic_lobster',
        'ai_mode': 'local',  # local 或 cloud
        'language': 'zh-CN',
        'theme': 'light',
        'auto_save': True,
        'encryption': True,
    }
    
    def __init__(self):
        """初始化配置"""
        self.config_path = None
        self.data_dir = None
        self.config = {}
    
    def init(self):
        """初始化配置"""
        # 创建数据目录
        data_dir = Path(self.DEFAULT_CONFIG['data_dir']).expanduser()
        data_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir = str(data_dir)
        
        # 创建配置目录
        config_dir = data_dir / 'config'
        config_dir.mkdir(exist_ok=True)
        
        # 创建数据库目录
        db_dir = data_dir / 'database'
        db_dir.mkdir(exist_ok=True)
        
        # 创建日志目录
        log_dir = data_dir / 'logs'
        log_dir.mkdir(exist_ok=True)
        
        # 创建模型目录
        model_dir = data_dir / 'models'
        model_dir.mkdir(exist_ok=True)
        
        # 保存配置
        self.config_path = config_dir / 'config.json'
        self.save()
        
        print(f"✓ 数据目录：{self.data_dir}")
        print(f"✓ 配置目录：{config_dir}")
        print(f"✓ 数据库目录：{db_dir}")
    
    def load(self) -> Dict[str, Any]:
        """加载配置"""
        if self.config_path and self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = self.DEFAULT_CONFIG.copy()
        
        return self.config
    
    def save(self):
        """保存配置"""
        if self.config_path:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def get(self, key: str, default=None) -> Any:
        """获取配置项"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """设置配置项"""
        self.config[key] = value
        self.save()


# 测试代码
if __name__ == '__main__':
    config = Config()
    config.init()
