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
- [Documentation](#-documentation)
- [Architecture](#-architecture)
- [Performance](#-performance)
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

### The Problem We Solve

Graduate students spend years reading papers, but knowledge remains:
- ❌ **Fragmented** - Papers stored in isolated PDFs
- ❌ **Disconnected** - No link between experiments and literature
- ❌ **Hard to recall** - "I know I read this somewhere..."
- ❌ **Repetitive work** - Same literature review for every lab meeting

### Our Solution

Academic Lobster v2 transforms fragmented knowledge into:
- ✅ **Structured** - Hierarchical knowledge trees
- ✅ **Connected** - Smart experiment-literature association
- ✅ **Searchable** - Full-text search across all knowledge
- ✅ **Automated** - One-click presentation generation

### Key Value

| Feature | Description | Benefit |
|---------|-------------|---------|
| 🌳 **Knowledge Tree** | Automatically builds "problem→method→paper→experiment" hierarchy | See the big picture |
| 💡 **Smart Association** | Links experiments with relevant literature (local + web dual mode) | Never miss related work |
| 📊 **PPT Generation** | One-click lab meeting presentations with speaker notes | Save 2+ hours per week |
| 🔒 **Local-First** | 100% local storage, optional compliant web scraping | Complete privacy |

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

**Benefits:**
- Visualize research landscape
- Track evolution of methods
- Connect theory with experiments

[Learn more →](docs/CORE_MODULES.md#1-knowledge-graph-engine)

---

### 2. Smart Literature Recommendation

**Dual-Mode Recommendation System:**

| Mode | Description | Privacy | Speed |
|------|-------------|---------|-------|
| **Local** | Matches against your local knowledge base | 🔒 100% private | ~45ms |
| **Advanced** | Fetches public abstracts from arXiv/PubMed/CNKI | ⚠️ User-triggered | ~250ms |

**Example Output:**
```
Smart Recommendations for: Swin Transformer Fine-tuning

1. Swin Transformer Original Paper ⭐⭐⭐⭐⭐
   Relevance: 95/100 | Source: Local
   Match: Direct architecture reference

2. Vision Transformer ⭐⭐⭐⭐
   Relevance: 88/100 | Source: Local
   Match: Foundation architecture

3. ConViT: Improving Vision Transformers ⭐⭐⭐
   Relevance: 75/100 | Source: arXiv
   Match: Improvement direction
```

**Algorithm:**
- Keyword matching (40%)
- Method similarity (30%)
- Domain relevance (20%)
- Recency (10%)

[Learn more →](docs/CORE_MODULES.md#2-smart-recommendation-engine)

---

### 3. Lab Meeting PPT Generator

Generate presentation outlines with ready-to-read speaker notes:

**Input:** Weekly experiments + related papers

**Output:**
- 5-slide presentation structure
- Speaker notes for each slide
- Markdown format (copy to PowerPoint)

**Example:**
```markdown
# Lab Meeting: Week 12 Progress

## Slide 1: Overview
- Completed Swin-T fine-tuning
- Compared 3 augmentation strategies

[Speaker Notes] Good morning, this week I completed...

## Slide 2: Results
- Top-1 Accuracy: 78.5% (+2.3%)
- Training Time: 12 hours

[Speaker Notes] Results show that...
```

**Time Savings:** 2-3 hours per week per researcher

[Learn more →](docs/CORE_MODULES.md#3-ppt-generator)

---

### 4. Security Sandbox

| Principle | Implementation | Benefit |
|-----------|----------------|---------|
| Local Storage | All private data stays on your device | Zero cloud dependency |
| No Cloud Uploads | Zero external API dependencies | Complete privacy |
| Compliant Scraping | Only public abstracts, with clear attribution | Legal compliance |
| Audit Trail | Full operation logging | Accountability |

[Security details →](docs/SECURITY_MODEL.md)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip
- Modern browser (Chrome/Firefox/Edge)

### Installation (5 minutes)

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

### First Use

1. **Upload Papers** (3-5 papers to start)
   - Click "Add Paper"
   - Upload PDF or enter metadata manually

2. **Add Experiment**
   - Click "Add Experiment"
   - Enter experiment details
   - Link to related papers

3. **View Knowledge Tree**
   - Navigate to "Knowledge Tree"
   - See your research landscape

4. **Get Recommendations**
   - Select an experiment
   - Click "Get Recommendations"
   - Review suggested papers

5. **Generate PPT**
   - Select experiments for this week
   - Click "Generate PPT"
   - Copy to PowerPoint

### Docker (Optional)

```bash
# Build image
docker build -t academic-lobster .

# Run container
docker run -p 5001:5001 -v academic-lobster-data:/app/data academic-lobster
```

### Production Deployment

For production deployment with Nginx, Gunicorn, and monitoring:

[See Deployment Guide →](docs/DEPLOYMENT.md)

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

[Speaker Notes] Good morning everyone, this week I completed...

## Slide 2: Results
- Top-1 Accuracy: 78.5% (+2.3%)
- Training Time: 12 hours
- Best Strategy: Mixup

[Speaker Notes] Results show that Mixup provides the best improvement...

## Slide 3: Analysis
- Mixup improves generalization
- CutMix shows similar performance
- Augmentation combination needs more study

[Speaker Notes] From the results we can see that...
```

---

## 📚 Documentation

### Core Documentation

| Document | Description | Link |
|----------|-------------|------|
| **Quick Start** | Get started in 5 minutes | [README](#-quick-start) |
| **Core Modules** | Detailed module documentation | [View →](docs/CORE_MODULES.md) |
| **API Reference** | Complete REST API documentation | [View →](docs/API_REFERENCE.md) |
| **Architecture** | System design and data flow | [View →](ARCHITECTURE.md) |
| **Security Model** | Security principles and implementation | [View →](SECURITY_MODEL.md) |

### Guides

| Guide | Description | Link |
|-------|-------------|------|
| **Deployment** | Production deployment guide | [View →](docs/DEPLOYMENT.md) |
| **Troubleshooting** | Common issues and solutions | [View →](TROUBLESHOOTING.md) |
| **Contributing** | How to contribute | [View →](CONTRIBUTING.md) |
| **Performance** | Performance benchmarks | [View →](docs/PERFORMANCE.md) |

### FAQ

[See Troubleshooting & FAQ →](TROUBLESHOOTING.md#faq)

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

[Detailed architecture →](ARCHITECTURE.md)

---

## ⚡ Performance

Academic Lobster v2 is optimized for speed and efficiency.

### Response Times (P50/P95)

| Operation | P50 | P95 | Throughput |
|-----------|-----|-----|------------|
| Paper Lookup | 8ms | 15ms | 1,250 req/s |
| Search (10 results) | 35ms | 68ms | 420 req/s |
| Recommendations (Local) | 45ms | 85ms | 280 req/s |
| Knowledge Tree Build | 85ms | 180ms | 520 req/s |
| PPT Generation (5 slides) | 120ms | 220ms | 85 req/s |

### Scalability

| Metric | Capacity | Recommendation |
|--------|----------|----------------|
| Papers | Up to 10,000 | Use PostgreSQL for >10K |
| Concurrent Users | Up to 100 | Use load balancer for >100 |
| Database Size | Up to 500MB | Archive old data |
| Memory Usage | < 600MB typical | Configure swap if needed |

[Full benchmarks →](docs/PERFORMANCE.md)

---

## 🛠️ Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Backend** | Python | 3.9+ | Main language |
| **Web Framework** | Flask | 2.3+ | Web server |
| **Database** | SQLite | 3.x | Local storage |
| **Data Processing** | Pandas, NumPy | Latest | Data manipulation |
| **NLP (English)** | spaCy | 3.5+ | Text processing |
| **NLP (Chinese)** | jieba | 0.42+ | Chinese text processing |
| **PPT Generation** | python-pptx | 0.6+ | Presentation output |
| **Deployment** | Docker | Optional | Containerization |
| **Production Server** | Gunicorn | 21.2+ | WSGI server |
| **Reverse Proxy** | Nginx | Latest | Load balancing |

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

[All dependencies →](requirements.txt)

---

## 📁 Project Structure

```
research/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
├── academic-lobster/
│   ├── src/                    # Source code (~3,350 lines)
│   │   ├── web_app_v2.py       # Web interface & API (1,200 lines)
│   │   ├── knowledge_graph.py  # Knowledge graph core (800 lines)
│   │   ├── smart_recommend.py  # Recommendation engine (600 lines)
│   │   ├── ppt_outline.py      # PPT generation (400 lines)
│   │   ├── lab_log.py          # Experiment logging (350 lines)
│   │   └── ...
│   ├── docs/                   # Documentation
│   │   ├── CORE_MODULES.md     # Module documentation
│   │   ├── API_REFERENCE.md    # API documentation
│   │   ├── DEPLOYMENT.md       # Deployment guide
│   │   ├── PERFORMANCE.md      # Performance benchmarks
│   │   └── ...
│   ├── tests/                  # Unit tests (85% coverage)
│   ├── assets/                 # Resources
│   └── TROUBLESHOOTING.md      # Troubleshooting & FAQ
└── requirements.txt            # Dependencies
```

---

## 🏆 Competition Materials

**Competition:** Zhongguancun Beiwei Lobster Contest - Academic Track

### Submission Package

| Material | Status | Link |
|----------|--------|------|
| **GitHub Repository** | ✅ Complete | [View →](https://github.com/bieyl/research) |
| **Project Statement** | ✅ Complete | [View →](COMPETITION-SUBMISSION.md) |
| **Project Poster** | ✅ Complete | [View →](assets/PROJECT-POSTER.md) |
| **Demo Video** | ⏳ In Progress | [Pending Bilibili upload] |
| **Safety Compliance** | ✅ Complete | [View →](docs/SAFETY-COMPLIANCE-PLEDGE.md) |
| **Technical Documentation** | ✅ Complete | [View →](docs/) |

### Product Description (150 words)

Academic Lobster v2 is a local research knowledge brain for graduate students. Core features: Knowledge Tree (auto-builds "problem→method→paper→experiment" hierarchy), Experiment-Literature Smart Association (local + compliant web dual mode), Lab Meeting PPT Generation (one-click outline + speaker notes). All private data stored locally; web scraping only fetches public abstracts with auto-cleanup. Goal: transform fragmented research knowledge into structured systems, automate repetitive tasks, enable researchers to focus on innovation.

### 30-Second Pitch

**Pain Point:** Graduate students read papers for years but knowledge remains fragmented.

**Solution:** Academic Lobster v2 builds knowledge trees, connects experiments with literature, generates presentations automatically.

**Value:** Local-first for security, compliant web scraping, equal research intelligence for every researcher.

### 5-Minute Demo Flow

| Time | Section | Content |
|------|---------|---------|
| 0:00-0:30 | Opening | Pain point + positioning |
| 0:30-2:00 | Feature 1 | Knowledge Tree (add 2 papers + 1 experiment) |
| 2:00-3:00 | Feature 2 | Smart Recommendation (local + web mode) |
| 3:00-4:00 | Feature 3 | One-click PPT generation |
| 4:00-5:00 | Summary | Value + Q&A |

---

## 🔒 Security & Compliance

### Data Security

| Principle | Implementation | Verification |
|-----------|----------------|--------------|
| Local Storage | 100% data on your device | No network calls by default |
| No Cloud | Zero external API dependencies | All processing local |
| Encryption | Optional database encryption | AES-256 available |
| Audit Trail | Full operation logging | logs/audit.log |

### Intellectual Property

| Commitment | Details |
|------------|---------|
| Public Abstracts Only | No paywalled content scraping |
| Clear Attribution | All sources labeled |
| Temporary Cache | Auto-cleanup after session |
| Compliance | Respects platform ToS |

### Security Architecture

- **Container Isolation:** Optional Docker deployment
- **Access Control:** API key authentication for production
- **Input Validation:** All user inputs sanitized
- **Error Handling:** No sensitive data in error messages

[Complete security model →](SECURITY_MODEL.md)

---

## 🤝 Contributing

We welcome contributions of all kinds!

### How to Contribute

1. **Fork** the repository
2. **Create** feature branch: `git checkout -b feature/your-feature`
3. **Commit** changes: `git commit -m 'Add your feature'`
4. **Push** to branch: `git push origin feature/your-feature`
5. **Open** Pull Request

### Development Setup

```bash
git clone https://github.com/bieyl/research.git
cd research/academic-lobster
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

### Running Tests

```bash
# All tests
pytest tests/

# With coverage
pytest --cov=src tests/

# Specific test file
pytest tests/test_knowledge_graph.py
```

### Contribution Areas

- 🐛 **Bug Reports** - Found a bug? Create an issue
- 💡 **Feature Requests** - Have an idea? Suggest it
- 📝 **Documentation** - Improve docs
- 💻 **Code** - Fix bugs or add features
- 🧪 **Testing** - Add test coverage
- 🌍 **Translation** - Translate to other languages

[Detailed guidelines →](CONTRIBUTING.md)

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

### APA Format

Bie, Y. (2026). Academic Lobster v2: Local-First Research Knowledge Brain (Version 2.0.0) [Computer Software]. https://github.com/bieyl/research

### Citation Metrics

- **Preferred:** BibTeX for LaTeX papers
- **Alternative:** APA format for social sciences
- **Software Citation:** Follow [FORCE11 Software Citation Principles](https://force11.org/info/software-citation-principles/)

[Citation file →](CITATION.cff)

---

## 📄 License

**MIT License** - Free for personal and commercial use

**Permissions:**
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**Conditions:**
- ℹ️ License and copyright notice required

**Limitations:**
- ⚠️ No liability
- ⚠️ No warranty

[Full license →](LICENSE)

---

## 📞 Contact

### Support

- **GitHub Issues:** https://github.com/bieyl/research/issues
- **Email:** bieyunlong1@163.com
- **Documentation:** https://github.com/bieyl/research/tree/main/academic-lobster/docs

### Affiliation

**Beijing Zhongguancun Institute**

### Acknowledgments

Thanks to:
- Zhongguancun Beiwei Lobster Contest Committee
- All graduate students and faculty who participated in testing
- The open source community for excellent projects

---

## 🎯 Roadmap

### v2.1 (Q2 2026)

- [ ] Zotero/Mendeley integration
- [ ] Mobile-responsive UI
- [ ] Multi-language support (Chinese, Spanish, French)
- [ ] Improved Chinese NLP

### v2.2 (Q3 2026)

- [ ] Multi-user collaboration
- [ ] Real-time sync
- [ ] Advanced search (facets, filters)
- [ ] Export to BibTeX, EndNote

### v2.3 (Q4 2026)

- [ ] AI-assisted tagging
- [ ] Automatic keyword extraction
- [ ] Integration with Overleaf
- [ ] Browser extension for quick save

### Future Considerations

- [ ] Desktop application (Electron)
- [ ] Mobile apps (iOS/Android)
- [ ] Cloud sync option (encrypted)
- [ ] Plugin system

---

**Academic Lobster v2 - Connecting Knowledge, Simplifying Innovation**

*Serving Every Serious Researcher*

---

*Last updated: March 17, 2026*

**Version:** 2.0.0  
**Status:** Competition Ready  
**Code Quality:** 85% Test Coverage
