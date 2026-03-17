#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图形用户界面模块
GUI - PyQt6 图形界面
"""

import sys
from pathlib import Path

try:
    from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QPushButton, QLabel, QTextEdit, QFileDialog, QTabWidget,
        QGroupBox, QFormLayout, QLineEdit, QMessageBox
    )
    from PyQt6.QtCore import Qt
    from PyQt6.QtGui import QFont
    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False


class MainWindow(QMainWindow):
    """主窗口"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle('🦞 学术龙虾 - 科研全流程 AI 助手')
        self.setGeometry(100, 100, 1200, 800)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 标题
        title = QLabel('🦞 学术龙虾 Academic Lobster')
        title.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)
        
        # 副标题
        subtitle = QLabel('让每一位研究者，都拥有平等的科研智能支持')
        subtitle.setFont(QFont('Arial', 12))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtitle)
        
        # 创建标签页
        tabs = QTabWidget()
        main_layout.addWidget(tabs)
        
        # 添加功能标签页
        tabs.addTab(self.create_summarizer_tab(), '📚 文献摘要')
        tabs.addTab(self.create_lablog_tab(), '📝 实验日志')
        tabs.addTab(self.create_ppt_tab(), '📄 PPT 大纲')
        tabs.addTab(self.create_reference_tab(), '📖 参考文献')
        tabs.addTab(self.create_settings_tab(), '⚙️ 设置')
    
    def create_summarizer_tab(self) -> QWidget:
        """创建文献摘要标签页"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # 文件选择
        file_group = QGroupBox('选择论文 PDF')
        file_layout = QHBoxLayout()
        
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText('拖入 PDF 文件或点击浏览...')
        
        browse_btn = QPushButton('浏览...')
        browse_btn.clicked.connect(self.browse_file)
        
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(browse_btn)
        file_group.setLayout(file_layout)
        
        # 操作按钮
        summarize_btn = QPushButton('生成摘要')
        summarize_btn.clicked.connect(self.generate_summary)
        
        # 结果显示
        self.summary_result = QTextEdit()
        self.summary_result.setPlaceholderText('摘要将显示在这里...')
        self.summary_result.setReadOnly(True)
        
        layout.addWidget(file_group)
        layout.addWidget(summarize_btn)
        layout.addWidget(self.summary_result)
        
        widget.setLayout(layout)
        return widget
    
    def create_lablog_tab(self) -> QWidget:
        """创建实验日志标签页"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # 数据输入
        input_group = QGroupBox('输入实验数据')
        input_layout = QVBoxLayout()
        
        self.lablog_input = QTextEdit()
        self.lablog_input.setPlaceholderText('示例：温度 60°C/70°C/80°C，反应时间 2h，产物收率 45%/62%/38%')
        
        input_layout.addWidget(self.lablog_input)
        input_group.setLayout(input_layout)
        
        # 操作按钮
        generate_btn = QPushButton('生成实验日报')
        generate_btn.clicked.connect(self.generate_lablog)
        
        # 结果显示
        self.lablog_result = QTextEdit()
        self.lablog_result.setPlaceholderText('实验报告将显示在这里...')
        self.lablog_result.setReadOnly(True)
        
        layout.addWidget(input_group)
        layout.addWidget(generate_btn)
        layout.addWidget(self.lablog_result)
        
        widget.setLayout(layout)
        return widget
    
    def create_ppt_tab(self) -> QWidget:
        """创建 PPT 大纲标签页"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # 进展输入
        progress_group = QGroupBox('输入研究进展')
        progress_layout = QVBoxLayout()
        
        self.progress_input = QTextEdit()
        self.progress_input.setPlaceholderText('示例：本周完成了 ResNet-50 在自定义数据集上的迁移学习，准确率 87%，遇到小样本过拟合问题')
        
        progress_layout.addWidget(self.progress_input)
        progress_group.setLayout(progress_layout)
        
        # 操作按钮
        generate_btn = QPushButton('生成 PPT 大纲')
        generate_btn.clicked.connect(self.generate_ppt)
        
        # 结果显示
        self.ppt_result = QTextEdit()
        self.ppt_result.setPlaceholderText('PPT 大纲将显示在这里...')
        self.ppt_result.setReadOnly(True)
        
        layout.addWidget(progress_group)
        layout.addWidget(generate_btn)
        layout.addWidget(self.ppt_result)
        
        widget.setLayout(layout)
        return widget
    
    def create_reference_tab(self) -> QWidget:
        """创建参考文献标签页"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # 文献输入
        ref_group = QGroupBox('输入参考文献')
        ref_layout = QVBoxLayout()
        
        self.ref_input = QTextEdit()
        self.ref_input.setPlaceholderText('示例：He K, Zhang X, Ren S, Sun J. Deep Residual Learning for Image Recognition. CVPR 2016.')
        
        ref_layout.addWidget(self.ref_input)
        ref_group.setLayout(ref_layout)
        
        # 操作按钮
        format_btn = QPushButton('格式化')
        format_btn.clicked.connect(self.format_reference)
        
        # 结果显示
        self.ref_result = QTextEdit()
        self.ref_result.setPlaceholderText('格式化结果将显示在这里...')
        self.ref_result.setReadOnly(True)
        
        layout.addWidget(ref_group)
        layout.addWidget(format_btn)
        layout.addWidget(self.ref_result)
        
        widget.setLayout(layout)
        return widget
    
    def create_settings_tab(self) -> QWidget:
        """创建设置标签页"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # AI 模式选择
        ai_group = QGroupBox('AI 模式')
        ai_layout = QFormLayout()
        
        self.ai_mode = QLineEdit('local')
        self.ai_mode.setPlaceholderText('local 或 cloud')
        ai_layout.addRow('AI 模式:', self.ai_mode)
        
        ai_group.setLayout(ai_layout)
        
        # 数据目录
        data_group = QGroupBox('数据目录')
        data_layout = QFormLayout()
        
        self.data_dir = QLineEdit('~/.academic_lobster')
        data_layout.addRow('数据目录:', self.data_dir)
        
        data_group.setLayout(data_layout)
        
        # 保存按钮
        save_btn = QPushButton('保存设置')
        save_btn.clicked.connect(self.save_settings)
        
        layout.addWidget(ai_group)
        layout.addWidget(data_group)
        layout.addWidget(save_btn)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    # 槽函数
    def browse_file(self):
        """浏览文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, '选择 PDF 文件', '', 'PDF Files (*.pdf)'
        )
        if file_path:
            self.file_path.setText(file_path)
    
    def generate_summary(self):
        """生成摘要"""
        file_path = self.file_path.text()
        if not file_path:
            QMessageBox.warning(self, '警告', '请先选择 PDF 文件')
            return
        
        # 调用摘要模块
        from summarizer import PaperSummarizer
        summarizer = PaperSummarizer()
        summary = summarizer.generate_summary(file_path)
        
        # 显示结果
        result = f"""【研究问题】{summary.get('research_question', 'N/A')}
【研究方法】{summary.get('method', 'N/A')}
【核心结论】{summary.get('conclusion', 'N/A')}
【创新点】{summary.get('innovation', 'N/A')}
【关键词】{', '.join(summary.get('keywords', []))}
"""
        self.summary_result.setText(result)
    
    def generate_lablog(self):
        """生成实验日志"""
        raw_data = self.lablog_input.toPlainText()
        if not raw_data:
            QMessageBox.warning(self, '警告', '请输入实验数据')
            return
        
        # 调用实验日志模块
        from lab_log import LabLogAssistant
        assistant = LabLogAssistant()
        report = assistant.generate_report(raw_data)
        
        self.lablog_result.setText(report)
    
    def generate_ppt(self):
        """生成 PPT 大纲"""
        progress = self.progress_input.toPlainText()
        if not progress:
            QMessageBox.warning(self, '警告', '请输入研究进展')
            return
        
        # 调用 PPT 大纲模块
        from ppt_outline import PPTOutliner
        outliner = PPTOutliner()
        outline = outliner.generate(progress)
        
        # 格式化显示
        result = ""
        for slide in outline['slides']:
            result += f"P{slide['page']} {slide['title']}\n"
            for point in slide['points']:
                result += f"   • {point}\n"
            result += "\n"
        
        self.ppt_result.setText(result)
    
    def format_reference(self):
        """格式化参考文献"""
        ref = self.ref_input.toPlainText()
        if not ref:
            QMessageBox.warning(self, '警告', '请输入参考文献')
            return
        
        # 调用参考文献模块
        from reference_formatter import ReferenceFormatter
        formatter = ReferenceFormatter()
        result_dict = formatter.format(ref)
        
        # 显示结果
        result = ""
        for fmt, formatted in result_dict.items():
            result += f"【{fmt}】{formatted}\n\n"
        
        self.ref_result.setText(result)
    
    def save_settings(self):
        """保存设置"""
        from config import Config
        config = Config()
        config.set('ai_mode', self.ai_mode.text())
        config.set('data_dir', self.data_dir.text())
        
        QMessageBox.information(self, '成功', '设置已保存')


# 测试代码
if __name__ == '__main__':
    if not PYQT_AVAILABLE:
        print("❌ PyQt6 未安装，请运行：pip install PyQt6")
        sys.exit(1)
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
