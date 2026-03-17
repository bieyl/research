# Academic Lobster v2

> **Local-First Research Knowledge Brain for Graduate Students and Research Groups**

[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/bieyl/research)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.3+-red?logo=flask)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/sqlite-3.x-blue)](https://www.sqlite.org/)
[![Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen)]()
[![Status](https://img.shields.io/badge/status-competition%20ready-brightgreen)]()

[![Competition](https://img.shields.io/badge/competition-zhongguancun%20beiwei%20lobster%20contest-orange)]()
[![Track](https://img.shields.io/badge/track-academic-brightgreen)]()

---

## 📖 Table of Contents

- [What is Academic Lobster?](#-what-is-academic-lobster)
- [Core Features](#-core-features)
- [Quick Start](#-quick-start)
- [Examples](#-examples)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Competition Materials](#-competition-materials)
- [Security & Compliance](#-security--compliance)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)

---

## 🦞 What is Academic Lobster?

**Academic Lobster v2** is a **local-first research knowledge brain** designed for graduate students and research groups.

Unlike generic literature management tools, it automatically builds a hierarchical knowledge tree connecting **research problems → methods → papers → experiments**, enabling intelligent association between your experiments and relevant literature.

### Key Value

| Feature | Description |
|---------|-------------|
| 🌳 **Knowledge Tree** | Automatically builds hierarchical "problem→method→paper→experiment" structure |
| 💡 **Smart Association** | Links experiments with relevant literature (local + compliant web dual mode) |
| 📊 **PPT Generation** | One-click generation of lab meeting presentations with speaker notes |
| 🔒 **Local-First** | 100% local storage, optional compliant web scraping for public abstracts |

---

## ✨ Core Features

### 1. Research Knowledge Tree

Build structured knowledge hierarchies from your papers and experiments:

```
Research Knowledge Tree

[Research Problem] Deep Network Training Degradation
├─[Method] Residual Connection
│  ├─📄 ResNet (He et al., 2016)
│  └─📄 Identity Mappings (He et al., 2016)
└─[Method] Improved Residual Block
   └─🧪 Your Experiment (2026-03-12)
```

### 2. Smart Literature Recommendation

**Dual-Mode Recommendation System:**

| Mode | Description | Privacy |
|------|-------------|---------|
| **Local** | Matches against your local knowledge base | 🔒 100% private |
| **Advanced** | Fetches public abstracts from arXiv/PubMed/CNKI | ⚠️ User-triggered, auto-cleanup |

**Example Output:**
```
Smart Recommendations for: Swin Transformer Fine-tuning

1. Swin Transformer Original Paper ⭐⭐⭐⭐⭐
   Relevance: 95/100 | Source: Local

2. Vision Transformer ⭐⭐⭐⭐
   Relevance: 88/100 | Source: Local

3. ConViT: Improving Vision Transformers ⭐⭐⭐
   Relevance: 75/100 | Source: arXiv (public abstract)
```

### 3. Lab Meeting PPT Generator

Generate presentation outlines with ready-to-read speaker notes:

**Input:** Weekly experiments + related papers

**Output:**
- 5-slide presentation structure
- Speaker notes for each slide
- Markdown format (copy to PowerPoint)

### 4. Security Sandbox

| Principle | Implementation |
|-----------|----------------|
| Local Storage | All private data stays on your device |
| No Cloud Uploads | Zero external API dependencies |
| Compliant Scraping | Only public abstracts, with clear attribution |
| Audit Trail | Full operation logging |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip
- Modern browser (Chrome/Firefox/Edge)

### Installation

```bash
# Clone repository
git clone https://github.com/bieyl/research.git
cd research/academic-lobster

# Install dependencies
pip install -r requirements.txt

# Start web application
python3 src/web_app_v2.py
```

**Access:** http://localhost:5001

### Docker (Optional)

```bash
# Build image
docker build -t academic-lobster .

# Run container
docker run -p 5001:5001 academic-lobster
```

---

## 📸 Examples

### Knowledge Tree Example

```
Research Knowledge Tree

[Research Problem] Image Classification Accuracy
├─[Method] Data Augmentation
│  ├─📄 AutoAugment (Cubuk et al., 2019)
│  └─🧪 RandAugment Comparison (2026-03-10)
├─[Method] Model Architecture
│  ├─📄 Vision Transformer (Dosovitskiy et al., 2020)
│  ├─📄 Swin Transformer (Liu et al., 2021)
│  └─🧪 Swin-T Fine-tuning (2026-03-11)
└─[Method] Loss Function
   ├─📄 Focal Loss (Lin et al., 2017)
   └─🧪 Focal Loss vs CrossEntropy (2026-03-12)
```

### Recommendation Example

```
💡 Smart Recommendations

Current Experiment: Swin Transformer Fine-tuning

1. Swin Transformer (Liu et al., 2021) [95/100]
   Match: Direct architecture reference
   Source: Local knowledge base

2. Vision Transformer (Dosovitskiy et al., 2020) [88/100]
   Match: Foundation architecture
   Source: Local knowledge base

3. ConViT (d'Ascoli et al., 2021) [75/100]
   Match: Improvement direction
   Source: arXiv (public abstract)
```

### PPT Output Example

```markdown
# Lab Meeting: Week 12 Progress

## Slide 1: Overview
- Completed Swin-T fine-tuning
- Compared 3 augmentation strategies
- Preparing CVPR submission

[Speaker Notes] Good morning, this week I completed...

## Slide 2: Results
- Top-1 Accuracy: 78.5% (+2.3%)
- Training Time: 12 hours
- Best Strategy: Mixup

[Speaker Notes] Results show that...
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface Layer                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Web UI     │  │  CLI        │  │  API (REST) │     │
│  │  (Flask)    │  │             │  │             │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                   Business Logic Layer                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ Knowledge│ │ Smart    │ │ PPT      │ │ Lab Log  │  │
│  │ Graph    │ │ Recommend│ │ Generator│ │ Engine   │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                    Data Storage Layer                    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  SQLite     │  │  JSON Files │  │  YAML Config│     │
│  │  (Metadata) │  │  (Trees)    │  │  (System)   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
```

**Data Flow:**
```
Upload Papers → Parse Metadata → Build Knowledge Tree → 
Store → Add Experiments → Smart Matching → Return Recommendations → 
(Optional) Generate PPT
```

See [ARCHITECTURE.md](academic-lobster/ARCHITECTURE.md) for detailed documentation.

---

## 🛠️ Technology Stack

| Category | Technology | Version |
|----------|------------|---------|
| **Backend** | Python | 3.9+ |
| **Web Framework** | Flask | 2.3+ |
| **Database** | SQLite | 3.x |
| **Data Processing** | Pandas, NumPy | Latest |
| **NLP** | spaCy, jieba | Latest |
| **PPT Generation** | python-pptx | 0.6+ |
| **Deployment** | Docker | Optional |

### Core Dependencies

```
flask>=2.3.0
pandas>=1.5.0
numpy>=1.21.0
spacy>=3.5.0
jieba>=0.42.0
python-pptx>=0.6.21
requests>=2.28.0
beautifulsoup4>=4.11.0
```

---

## 📁 Project Structure

```
research/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
├── academic-lobster/
│   ├── src/                    # Source code
│   │   ├── web_app_v2.py       # Web interface
│   │   ├── knowledge_graph.py  # Knowledge graph core
│   │   ├── smart_recommend.py  # Recommendation engine
│   │   ├── ppt_outline.py      # PPT generation
│   │   └── ...
│   ├── docs/                   # Documentation
│   ├── tests/                  # Tests
│   └── assets/                 # Resources
└── requirements.txt            # Dependencies
```

---

## 🏆 Competition Materials

**Competition:** Zhongguancun Beiwei Lobster Contest - Academic Track

| Material | Link | Status |
|----------|------|--------|
| **GitHub Repository** | https://github.com/bieyl/research | ✅ Complete |
| **Project Statement** | [COMPETITION-SUBMISSION.md](academic-lobster/COMPETITION-SUBMISSION.md) | ✅ Complete |
| **Project Poster** | [assets/PROJECT-POSTER.md](academic-lobster/assets/PROJECT-POSTER.md) | ✅ Complete |
| **Demo Video** | [Pending Bilibili upload] | ⏳ In Progress |
| **Safety Compliance** | [docs/SAFETY-COMPLIANCE-PLEDGE.md](academic-lobster/docs/SAFETY-COMPLIANCE-PLEDGE.md) | ✅ Complete |

### Product Description (150 words)

Academic Lobster v2 is a local research knowledge brain for graduate students. Core features: Knowledge Tree (auto-builds "problem→method→paper→experiment" hierarchy), Experiment-Literature Smart Association (local + compliant web dual mode), Lab Meeting PPT Generation (one-click outline + speaker notes). All private data stored locally; web scraping only fetches public abstracts with auto-cleanup. Goal: transform fragmented research knowledge into structured systems, automate repetitive tasks, enable researchers to focus on innovation.

### 30-Second Pitch

**Pain Point:** Graduate students read papers for years but knowledge remains fragmented.

**Solution:** Academic Lobster v2 builds knowledge trees, connects experiments with literature, generates presentations automatically.

**Value:** Local-first for security, compliant web scraping, equal research intelligence for every researcher.

---

## 🔒 Security & Compliance

### Data Security

| Principle | Implementation |
|-----------|----------------|
| Local Storage | 100% data on your device |
| No Cloud | Zero external API dependencies |
| Encryption | Optional database encryption |
| Audit Trail | Full operation logging |

### Intellectual Property

| Commitment | Details |
|------------|---------|
| Public Abstracts Only | No paywalled content |
| Clear Attribution | All sources labeled |
| Temporary Cache | Auto-cleanup after session |
| Compliance | Respects platform ToS |

See [SECURITY.md](academic-lobster/SECURITY.md) for complete security documentation.

---

## 🤝 Contributing

We welcome contributions!

### How to Contribute

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m 'Add your feature'`
4. Push: `git push origin feature/your-feature`
5. Open Pull Request

### Development Setup

```bash
git clone https://github.com/bieyl/research.git
cd research/academic-lobster
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Run Tests

```bash
python -m pytest tests/
```

See [CONTRIBUTING.md](academic-lobster/CONTRIBUTING.md) for detailed guidelines.

---

## 📚 Citation

If you use Academic Lobster v2 in your research:

### BibTeX

```bibtex
@software{academic_lobster_v2,
  title = {Academic Lobster v2: Local-First Research Knowledge Brain},
  author = {Bie Yunlong and Academic Lobster Team},
  year = {2026},
  url = {https://github.com/bieyl/research},
  version = {2.0.0}
}
```

### APA

Bie, Y. (2026). Academic Lobster v2: Local-First Research Knowledge Brain (Version 2.0.0) [Computer Software]. https://github.com/bieyl/research

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 📞 Contact

- **Issues:** https://github.com/bieyl/research/issues
- **Email:** bieyunlong1@163.com
- **Affiliation:** Beijing Zhongguancun Institute

---

**Academic Lobster v2 - Connecting Knowledge, Simplifying Innovation**

*Serving Every Serious Researcher*

---

*Last updated: March 17, 2026*
