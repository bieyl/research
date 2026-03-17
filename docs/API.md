# API 文档
# Academic Lobster v2 API Reference

## 基础信息

**Base URL:** `http://localhost:5001`

**Content-Type:** `application/json`

---

## 健康检查

### GET /health

检查服务是否正常运行。

**响应:**
```json
{
  "status": "healthy",
  "version": "2.0.0",
  "timestamp": "2026-03-12T10:00:00Z"
}
```

---

## 知识图谱

### POST /api/graph/paper

添加论文到知识图谱。

**请求体:**
```json
{
  "title": "Deep Residual Learning",
  "authors": ["He K", "Zhang X", "Ren S", "Sun J"],
  "year": 2016,
  "research_question": "深层网络训练退化问题",
  "method": "残差连接",
  "conclusion": "可训练 152 层网络",
  "keywords": ["深度学习", "残差学习", "图像分类"],
  "category": "计算机视觉"
}
```

**响应:**
```json
{
  "success": true,
  "node_id": "paper_001",
  "message": "论文添加成功"
}
```

### POST /api/graph/experiment

添加实验到知识图谱。

**请求体:**
```json
{
  "title": "ResNet-50 图像分类实验",
  "purpose": "验证残差连接的有效性",
  "method": "使用 PyTorch 实现 ResNet-50",
  "results": "Top-1 准确率 76.0%",
  "tags": ["ResNet", "图像分类", "PyTorch"]
}
```

**响应:**
```json
{
  "success": true,
  "node_id": "exp_001",
  "message": "实验添加成功"
}
```

### GET /api/graph/tree

获取树状知识图谱。

**响应:**
```json
{
  "success": true,
  "tree": "🌳 科研知识图谱\n【研究问题】深层网络训练退化问题\n├─【方法】残差连接\n│ ├─📄 ResNet (He et al., 2016)\n│ └─📄 Identity Mappings (He et al., 2016)\n└─🧪 你的实验 (2026-03-12)"
}
```

---

## 智能推荐

### POST /api/recommend/papers

为实验推荐相关论文。

**请求体:**
```json
{
  "experiment_text": "使用 ResNet 进行图像分类实验",
  "top_n": 5
}
```

**响应:**
```json
{
  "success": true,
  "recommendations": [
    {
      "paper": {...},
      "score": 95,
      "reason": "匹配关键词：ResNet, 图像分类"
    }
  ]
}
```

### POST /api/recommend/arxiv

从 arXiv 获取实时推荐。

**请求体:**
```json
{
  "keywords": "ResNet image classification",
  "mode": "recent",
  "top_n": 5
}
```

**响应:**
```json
{
  "success": true,
  "papers": [
    {
      "title": "...",
      "authors": [...],
      "year": 2024,
      "arxiv_id": "2401.xxxxx",
      "tag": "🌐 arXiv 实时"
    }
  ]
}
```

---

## 文献摘要

### POST /api/summarize

生成文献摘要。

**请求体:**
```json
{
  "text": "论文全文或摘要内容...",
  "max_length": 500
}
```

**响应:**
```json
{
  "success": true,
  "summary": {
    "research_question": "...",
    "method": "...",
    "conclusion": "...",
    "keywords": [...]
  }
}
```

---

## 实验日志

### POST /api/lablog/generate

生成实验日志。

**请求体:**
```json
{
  "title": "实验标题",
  "purpose": "实验目的",
  "method": "实验方法",
  "results": "实验结果",
  "conclusion": "实验结论"
}
```

**响应:**
```json
{
  "success": true,
  "log": "# 实验报告\n\n## 实验标题\n\n### 目的\n...\n\n### 方法\n...\n\n### 结果\n...\n\n### 结论\n..."
}
```

---

## PPT 大纲

### POST /api/ppt/generate

生成 PPT 大纲。

**请求体:**
```json
{
  "papers": [...],
  "experiment": {...}
}
```

**响应:**
```json
{
  "success": true,
  "outline": {
    "title": "组会汇报",
    "slides": [
      {
        "slide_number": 1,
        "title": "研究背景",
        "content": "...",
        "speaker_notes": "..."
      }
    ]
  }
}
```

---

## 参考文献格式化

### POST /api/reference/format

格式化参考文献。

**请求体:**
```json
{
  "papers": [
    {
      "title": "Deep Residual Learning",
      "authors": ["He K", "Zhang X", "Ren S", "Sun J"],
      "year": 2016,
      "journal": "CVPR"
    }
  ],
  "style": "gb"
}
```

**响应:**
```json
{
  "success": true,
  "formatted": [
    "He K, Zhang X, Ren S, et al. Deep Residual Learning[C]//CVPR, 2016."
  ]
}
```

---

## 错误响应

所有 API 错误返回统一格式：

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "错误描述"
  }
}
```

**常见错误码:**
- `INVALID_INPUT` - 输入参数无效
- `NOT_FOUND` - 资源不存在
- `INTERNAL_ERROR` - 服务器内部错误
- `ARXIV_ERROR` - arXiv API 调用失败

---

## 速率限制

- 本地 API：无限制
- arXiv API：受 arXiv 官方限制（建议间隔 3 秒）

---

## 认证

当前版本无需认证（本地部署）。

未来版本可能支持 API Key 认证。
