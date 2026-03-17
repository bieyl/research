# API Reference - Academic Lobster v2

**Base URL:** `http://localhost:5001/api`  
**Version:** 2.0.0  
**Last Updated:** March 17, 2026

---

## 📋 Table of Contents

- [Authentication](#authentication)
- [Papers](#papers)
- [Experiments](#experiments)
- [Recommendations](#recommendations)
- [Knowledge Tree](#knowledge-tree)
- [PPT Generation](#ppt-generation)
- [Search](#search)
- [Export](#export)
- [Error Handling](#error-handling)

---

## 🔐 Authentication

### API Key Authentication (Production)

**Header:**
```
X-API-Key: your-api-key-here
```

---

## 📄 Papers

### Add Paper

**POST** `/api/papers`

Add a new paper to the knowledge base.

**Request:**
```json
{
  "title": "Deep Residual Learning for Image Recognition",
  "authors": ["He, Kaiming", "Zhang, Xiangyu", "Ren, Shaoqing", "Sun, Jian"],
  "year": 2016,
  "venue": "CVPR",
  "abstract": "Deep residual networks have emerged as...",
  "keywords": ["residual", "deep learning", "CNN"],
  "pdf_path": "/path/to/paper.pdf"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Paper added successfully",
  "data": {
    "paper_id": 123,
    "title": "Deep Residual Learning for Image Recognition",
    "created_at": "2026-03-17T14:30:00Z"
  }
}
```

**Error Response:**
```json
{
  "status": "error",
  "message": "Invalid paper data",
  "errors": [
    "Title is required",
    "Year must be between 1900 and 2100"
  ]
}
```

---

### Get All Papers

**GET** `/api/papers`

Retrieve all papers with pagination.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | int | 10 | Number of papers per page |
| `offset` | int | 0 | Offset for pagination |
| `year` | int | - | Filter by year |
| `venue` | string | - | Filter by venue |

**Request:**
```
GET /api/papers?limit=10&offset=0&year=2021
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "papers": [
      {
        "paper_id": 123,
        "title": "Deep Residual Learning...",
        "authors": ["He, Kaiming", "..."],
        "year": 2016,
        "venue": "CVPR",
        "keywords": ["residual", "deep learning"]
      }
    ],
    "total": 150,
    "limit": 10,
    "offset": 0
  }
}
```

---

### Get Paper by ID

**GET** `/api/papers/:id`

Retrieve a specific paper.

**Request:**
```
GET /api/papers/123
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "paper_id": 123,
    "title": "Deep Residual Learning...",
    "authors": ["He, Kaiming", "..."],
    "year": 2016,
    "venue": "CVPR",
    "abstract": "Deep residual networks...",
    "keywords": ["residual", "deep learning"],
    "pdf_path": "/path/to/paper.pdf",
    "created_at": "2026-03-17T14:30:00Z"
  }
}
```

---

### Delete Paper

**DELETE** `/api/papers/:id`

Delete a paper from the knowledge base.

**Request:**
```
DELETE /api/papers/123
```

**Response:**
```json
{
  "status": "success",
  "message": "Paper deleted successfully"
}
```

---

## 🧪 Experiments

### Add Experiment

**POST** `/api/experiments`

Add a new experiment record.

**Request:**
```json
{
  "name": "Swin-T Fine-tuning on ImageNet",
  "date": "2026-03-11",
  "research_problem": "Image Classification Accuracy",
  "method": "Vision Transformer",
  "description": "Fine-tuned Swin-Tiny on ImageNet with Mixup",
  "results": {
    "top1_accuracy": 78.5,
    "top5_accuracy": 94.2,
    "training_time_hours": 12
  },
  "linked_papers": [123, 124]
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Experiment added successfully",
  "data": {
    "experiment_id": 456,
    "name": "Swin-T Fine-tuning on ImageNet",
    "created_at": "2026-03-17T14:30:00Z"
  }
}
```

---

### Get Experiments

**GET** `/api/experiments`

Retrieve experiments with filters.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `method` | string | - | Filter by method |
| `date_from` | date | - | Filter by date range |
| `date_to` | date | - | Filter by date range |

**Response:**
```json
{
  "status": "success",
  "data": {
    "experiments": [
      {
        "experiment_id": 456,
        "name": "Swin-T Fine-tuning...",
        "method": "Vision Transformer",
        "date": "2026-03-11",
        "results": {
          "top1_accuracy": 78.5
        }
      }
    ],
    "total": 25
  }
}
```

---

### Link Paper to Experiment

**POST** `/api/experiments/:id/link-paper`

Link a paper to an experiment.

**Request:**
```
POST /api/experiments/456/link-paper
Content-Type: application/json

{
  "paper_id": 123
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Paper linked successfully"
}
```

---

## 💡 Recommendations

### Get Recommendations

**POST** `/api/recommendations`

Get paper recommendations for an experiment.

**Request:**
```json
{
  "experiment_id": 456,
  "mode": "local"  // or "advanced"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "experiment": {
      "experiment_id": 456,
      "name": "Swin-T Fine-tuning..."
    },
    "recommendations": [
      {
        "rank": 1,
        "paper_id": 123,
        "title": "Swin Transformer",
        "authors": ["Liu, Ze", "..."],
        "year": 2021,
        "relevance_score": 95,
        "source": "Local",
        "match_reasons": [
          "Direct architecture reference",
          "Same method family"
        ]
      },
      {
        "rank": 2,
        "paper_id": 124,
        "title": "Vision Transformer",
        "relevance_score": 88,
        "source": "Local"
      }
    ],
    "processing_time_ms": 45
  }
}
```

---

## 🌳 Knowledge Tree

### Get Knowledge Tree

**GET** `/api/knowledge-tree`

Retrieve the complete knowledge tree.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `format` | string | json | Output format (json, text) |
| `depth` | int | - | Limit tree depth |

**Response:**
```json
{
  "status": "success",
  "data": {
    "tree": {
      "Image Classification Accuracy": {
        "Residual Connection": {
          "papers": [
            {
              "paper_id": 123,
              "title": "ResNet",
              "year": 2016
            }
          ]
        },
        "Vision Transformer": {
          "papers": [
            {
              "paper_id": 124,
              "title": "Swin Transformer",
              "year": 2021
            }
          ]
        }
      }
    }
  }
}
```

---

## 📊 PPT Generation

### Generate PPT

**POST** `/api/ppt/generate`

Generate presentation from experiments.

**Request:**
```json
{
  "experiment_ids": [456, 457, 458],
  "include_speaker_notes": true,
  "format": "markdown"  // or "json"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "presentation": {
      "title": "Lab Meeting: Week 12 Progress",
      "slides": [
        {
          "slide_number": 1,
          "title": "Overview",
          "content": [
            "Completed Swin-T fine-tuning",
            "Compared 3 augmentation strategies"
          ],
          "speaker_notes": "Good morning everyone, this week..."
        }
      ],
      "total_slides": 5
    },
    "processing_time_ms": 120
  }
}
```

---

### Export PPT

**POST** `/api/ppt/export`

Export presentation to file.

**Request:**
```json
{
  "presentation_id": "abc123",
  "format": "markdown",  // or "pptx", "pdf"
  "citation_style": "APA"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "file_url": "/downloads/presentation.md",
    "file_size_bytes": 3200,
    "format": "markdown"
  }
}
```

---

## 🔍 Search

### Search Papers

**GET** `/api/search`

Search papers by query.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `q` | string | - | Search query |
| `fields` | string | all | Fields to search (title,abstract,keywords) |
| `year_from` | int | - | Filter by year range |
| `year_to` | int | - | Filter by year range |
| `limit` | int | 10 | Number of results |

**Request:**
```
GET /api/search?q=transformer+attention&fields=title,abstract&limit=10
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "query": "transformer attention",
    "results": [
      {
        "paper_id": 124,
        "title": "Attention Is All You Need",
        "relevance_score": 98,
        "highlight": "<em>Attention</em> Is All You Need"
      }
    ],
    "total": 15,
    "processing_time_ms": 35
  }
}
```

---

## 📤 Export

### Export Papers

**POST** `/api/export`

Export papers to various formats.

**Request:**
```json
{
  "paper_ids": [123, 124, 125],
  "format": "bibtex",  // or "ris", "endnote", "csv"
  "citation_style": "APA"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "file_url": "/downloads/export.bib",
    "file_size_bytes": 1024,
    "format": "bibtex",
    "papers_exported": 3
  }
}
```

---

## ❌ Error Handling

### Error Response Format

All errors follow this format:

```json
{
  "status": "error",
  "message": "Human-readable error message",
  "errors": [
    "Specific validation error 1",
    "Specific validation error 2"
  ],
  "code": "ERROR_CODE"
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_INPUT` | 400 | Invalid request data |
| `NOT_FOUND` | 404 | Resource not found |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `CONFLICT` | 409 | Resource conflict |
| `SERVER_ERROR` | 500 | Internal server error |

### Example Error Responses

**400 Bad Request:**
```json
{
  "status": "error",
  "message": "Invalid paper data",
  "errors": [
    "Title is required",
    "Year must be between 1900 and 2100"
  ],
  "code": "INVALID_INPUT"
}
```

**404 Not Found:**
```json
{
  "status": "error",
  "message": "Paper not found",
  "code": "NOT_FOUND"
}
```

**500 Internal Server Error:**
```json
{
  "status": "error",
  "message": "An unexpected error occurred",
  "code": "SERVER_ERROR"
}
```

---

## 📊 Rate Limiting

**Default Limits:**
- 100 requests per minute (authenticated)
- 20 requests per minute (unauthenticated)

**Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1647532800
```

**Rate Limit Exceeded:**
```json
{
  "status": "error",
  "message": "Rate limit exceeded",
  "code": "RATE_LIMIT_EXCEEDED",
  "retry_after": 60
}
```

---

## 🧪 Testing

### Using curl

```bash
# Add paper
curl -X POST http://localhost:5001/api/papers \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Paper",
    "year": 2026
  }'

# Get recommendations
curl -X POST http://localhost:5001/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "experiment_id": 456,
    "mode": "local"
  }'
```

### Using Python

```python
import requests

BASE_URL = "http://localhost:5001/api"

# Add paper
response = requests.post(f"{BASE_URL}/papers", json={
    "title": "Test Paper",
    "year": 2026
})
print(response.json())

# Get recommendations
response = requests.post(f"{BASE_URL}/recommendations", json={
    "experiment_id": 456,
    "mode": "local"
})
print(response.json())
```

---

**Complete API documentation with interactive examples:**  
[Swagger UI](http://localhost:5001/api/docs) (when enabled)
