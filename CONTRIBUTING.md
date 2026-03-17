# Contributing to Academic Lobster v2

**Thank you for your interest in contributing!** 🎉

This document provides guidelines and instructions for contributing to Academic Lobster v2.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Guidelines](#documentation-guidelines)
- [Module Development](#module-development)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

---

## 🤝 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

Examples of behavior that contributes to creating a positive environment:

- ✅ Using welcoming and inclusive language
- ✅ Being respectful of differing viewpoints
- ✅ Gracefully accepting constructive criticism
- ✅ Focusing on what is best for the community
- ✅ Showing empathy towards other community members

Examples of unacceptable behavior:

- ❌ The use of sexualized language or imagery
- ❌ Trolling, insulting/derogatory comments
- ❌ Public or private harassment
- ❌ Publishing others' private information
- ❌ Other conduct which could reasonably be considered inappropriate

---

## 🚀 Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/research.git
cd research/academic-lobster
```

### 2. Set Up Development Environment

```bash
# Install Python dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Download NLP models
python -m spacy download en_core_web_sm

# Verify installation
python -m pytest tests/ -v
```

### 3. Create a Branch

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or bug fix branch
git checkout -b fix/issue-123
```

---

## 💻 Development Setup

### Required Tools

- Python 3.9+
- pip
- git
- pytest (for testing)
- black (for code formatting)
- flake8 (for linting)

### Optional Tools

- VS Code with Python extension
- Docker (for containerized testing)
- Postman (for API testing)

### IDE Configuration

**VS Code Settings:**
```json
{
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "editor.formatOnSave": true,
  "editor.rulers": [88]
}
```

---

## 🔧 Making Changes

### 1. Understand the Issue

- Read the issue description carefully
- Ask questions if anything is unclear
- Confirm the expected behavior

### 2. Plan Your Changes

- Identify affected files
- Consider edge cases
- Plan tests needed

### 3. Implement Changes

```bash
# Make your changes
# Then format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Run tests
pytest tests/ -v

# Check coverage
pytest --cov=src tests/
```

### 4. Write Tests

**Test File Structure:**
```python
# tests/test_your_module.py

import pytest
from src.your_module import your_function

def test_your_function_success():
    """Test successful execution"""
    result = your_function(input_data)
    assert result == expected_output

def test_your_function_failure():
    """Test error handling"""
    with pytest.raises(ValueError):
        your_function(invalid_input)
```

---

## 📤 Pull Request Process

### 1. Before Submitting

- [ ] Code is formatted (black)
- [ ] Code passes linting (flake8)
- [ ] All tests pass
- [ ] Test coverage >= 85%
- [ ] Documentation updated
- [ ] Commit messages are clear

### 2. Create Pull Request

```bash
# Commit changes
git add .
git commit -m "feat: add your feature description"

# Push to GitHub
git push origin feature/your-feature-name

# Open PR on GitHub
# - Title: Clear and descriptive
# - Description: Explain what and why
# - Link related issues
```

### 3. PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Coverage maintained

## Checklist
- [ ] Code formatted
- [ ] Code linted
- [ ] Documentation updated
- [ ] Examples tested
```

### 4. Code Review

- Respond to reviewer comments
- Make requested changes
- Request re-review when ready

### 5. Merge

- PR approved by maintainer
- All CI checks pass
- Squash and merge

---

## 📝 Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.readthedocs.io/) with these specifics:

**Line Length:** 88 characters (black default)

**Imports:**
```python
# Standard library
import os
import sys

# Third-party
import flask
import spacy

# Local imports
from src.knowledge_graph import KnowledgeGraph
from src.models import Paper
```

**Functions:**
```python
def add_paper(paper: Paper) -> int:
    """
    Add paper to knowledge graph
    
    Args:
        paper: Paper object with metadata
        
    Returns:
        paper_id: Assigned database ID
        
    Raises:
        ValueError: If paper is invalid
    """
    # Implementation...
```

**Classes:**
```python
class KnowledgeGraph:
    """Knowledge graph engine for research papers"""
    
    def __init__(self, db_path: str):
        """Initialize knowledge graph"""
        self.db_path = db_path
        self.db = sqlite3.connect(db_path)
```

### Naming Conventions

- **Variables:** `snake_case` (e.g., `paper_id`)
- **Functions:** `snake_case` (e.g., `add_paper()`)
- **Classes:** `PascalCase` (e.g., `KnowledgeGraph`)
- **Constants:** `UPPER_CASE` (e.g., `MAX_PAPERS`)
- **Private:** `_prefix` (e.g., `_internal_method()`)

---

## 🧪 Testing Guidelines

### Test Categories

**Unit Tests:**
```python
def test_add_paper():
    """Test paper addition"""
    kg = KnowledgeGraph(":memory:")
    paper = Paper(title="Test", year=2026)
    paper_id = kg.add_paper(paper)
    assert paper_id > 0
```

**Integration Tests:**
```python
def test_full_workflow():
    """Test complete workflow"""
    # Upload paper → Build tree → Get recommendations
```

**Performance Tests:**
```python
def test_search_performance(benchmark):
    """Test search latency"""
    result = benchmark(kg.search, "transformer")
    assert len(result) > 0
```

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific file
pytest tests/test_knowledge_graph.py -v

# With coverage
pytest --cov=src tests/

# Performance tests
pytest tests/benchmarks/ -v
```

### Coverage Requirements

- **Overall:** >= 85%
- **Core modules:** >= 90%
- **New code:** >= 90%

---

## 📚 Documentation Guidelines

### Code Comments

```python
# Bad: Obvious comment
i += 1  # Increment i

# Good: Why comment
i += 1  # Skip header row
```

### Docstrings

```python
def calculate_relevance(experiment, paper):
    """
    Calculate relevance score (0-100)
    
    Scoring breakdown:
    - Keyword matching: 40%
    - Method similarity: 30%
    - Domain relevance: 20%
    - Recency: 10%
    
    Args:
        experiment: Experiment object
        paper: Paper object
        
    Returns:
        float: Relevance score (0-100)
    """
```

### Documentation Files

**Location:** `docs/` directory

**Format:** Markdown

**Structure:**
```markdown
# Module Name

## Overview
Brief description

## Usage
Code examples

## API Reference
Function signatures

## Examples
Real-world use cases

## Troubleshooting
Common issues and solutions
```

---

## 🧩 Module Development

### Adding a New Module

**1. Create Module File:**
```python
# src/new_module.py

class NewModule:
    """New module description"""
    
    def __init__(self):
        """Initialize module"""
        pass
    
    def main_function(self, input_data):
        """
        Main function description
        
        Args:
            input_data: Input data
            
        Returns:
            Output data
        """
        # Implementation
        return output
```

**2. Add Tests:**
```python
# tests/test_new_module.py

def test_new_module():
    """Test new module"""
    module = NewModule()
    result = module.main_function(test_input)
    assert result == expected
```

**3. Add to Web App:**
```python
# src/web_app_v2.py

from src.new_module import NewModule

@app.route('/api/new-endpoint', methods=['POST'])
def new_endpoint():
    """New API endpoint"""
    module = NewModule()
    result = module.main_function(request.json)
    return jsonify(result)
```

**4. Update Documentation:**
- Add to `docs/MODULES.md`
- Add examples to `examples/`
- Update `README.md` if needed

---

## 🐛 Bug Reports

### How to Report a Bug

**1. Check Existing Issues**
- Search for similar issues
- Avoid duplicates

**2. Create New Issue**
- Use bug report template
- Provide clear title
- Include steps to reproduce

**3. Bug Report Template:**
```markdown
## Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., macOS 14.0]
- Python: [e.g., 3.11]
- Version: [e.g., 2.0.0]

## Screenshots
If applicable

## Additional Context
Any other relevant information
```

---

## 💡 Feature Requests

### How to Request a Feature

**1. Check Existing Issues**
- Search for similar requests
- Avoid duplicates

**2. Create New Issue**
- Use feature request template
- Explain use case
- Describe expected behavior

**3. Feature Request Template:**
```markdown
## Problem Statement
What problem does this solve?

## Proposed Solution
How should it work?

## Use Cases
Who will use this and how?

## Alternatives Considered
What other solutions exist?

## Additional Context
Any other relevant information
```

---

## 🎓 Learning Resources

### Python

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.readthedocs.io/)
- [Real Python](https://realpython.com/)

### Flask

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Testing

- [pytest Documentation](https://docs.pytest.org/)
- [Test-Driven Development with Python](https://www.obeythetestinggoat.com/)

### Git

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

---

## 📞 Getting Help

- **GitHub Issues:** https://github.com/bieyl/research/issues
- **Email:** bieyunlong1@163.com
- **Discussions:** https://github.com/bieyl/research/discussions

---

## 🙏 Thank You!

Every contribution, no matter how small, makes Academic Lobster v2 better for everyone.

**Happy coding!** 🦞
