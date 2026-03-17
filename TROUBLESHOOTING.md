# Troubleshooting & FAQ - Academic Lobster v2

**Version:** 2.0.0  
**Last Updated:** March 17, 2026

---

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Runtime Issues](#runtime-issues)
- [Performance Issues](#performance-issues)
- [Feature-Specific Issues](#feature-specific-issues)
- [Common Errors](#common-errors)
- [FAQ](#faq)

---

## 🔧 Installation Issues

### Issue: pip install fails

**Error:**
```
ERROR: Could not find a version that satisfies the requirement spacy>=3.5.0
```

**Solution:**
```bash
# Upgrade pip first
pip install --upgrade pip

# Then install dependencies
pip install -r requirements.txt

# If still fails, install individually
pip install spacy==3.5.0
pip install flask==2.3.0
pip install pandas==1.5.0
```

---

### Issue: spaCy model download fails

**Error:**
```
ERROR: Could not find a suitable version for en_core_web_sm
```

**Solution:**
```bash
# Method 1: Direct download
python -m spacy download en_core_web_sm

# Method 2: Manual download
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0-py3-none-any.whl

# Method 3: Use alternative mirror
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple spacy
python -m spacy download en_core_web_sm
```

---

### Issue: Docker build fails

**Error:**
```
ERROR: failed to solve: failed to compute cache key: "/requirements.txt" not found
```

**Solution:**
```bash
# Check file paths
ls -la academic-lobster/

# Ensure you're in the right directory
cd academic-lobster

# Rebuild Docker image
docker build -t academic-lobster .

# If still fails, try without cache
docker build --no-cache -t academic-lobster .
```

---

## ⚠️ Runtime Issues

### Issue: Application won't start

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Verify installation
pip list | grep flask

# Reinstall if missing
pip install flask

# Check Python version
python --version  # Should be 3.9+

# Start application
python3 src/web_app_v2.py
```

---

### Issue: Port 5001 already in use

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solution:**
```bash
# Find process using port 5001
lsof -i :5001

# Kill the process
kill -9 <PID>

# Or use different port
python3 src/web_app_v2.py --port 5002
```

---

### Issue: Database locked

**Error:**
```
sqlite3.OperationalError: database is locked
```

**Solution:**
```bash
# Find and kill processes holding database
lsof data/papers.db

# Or wait for other processes to finish

# If persistent, backup and recreate
cp data/papers.db data/papers.db.backup
rm data/papers.db

# Restart application
python3 src/web_app_v2.py
```

---

## 🐌 Performance Issues

### Issue: Slow search performance

**Symptoms:** Search takes > 1 second

**Solution:**
```bash
# Check database size
du -h data/papers.db

# If > 500MB, consider archiving old papers
# Or optimize database
sqlite3 data/papers.db "VACUUM;"

# Enable query profiling
python3 src/web_app_v2.py --profile

# Check system resources
top  # CPU usage
free -h  # Memory usage
```

---

### Issue: High memory usage

**Symptoms:** Application uses > 1GB RAM

**Solution:**
```python
# In config.py, reduce batch size
SEARCH_BATCH_SIZE = 50  # Default: 100
RECOMMENDATION_LIMIT = 5  # Default: 10
```

```bash
# Restart application
pkill -f web_app_v2.py
python3 src/web_app_v2.py
```

---

## 🎯 Feature-Specific Issues

### Issue: PDF upload fails

**Error:**
```
Error parsing PDF: File not found
```

**Solution:**
```bash
# Check file permissions
ls -la /path/to/paper.pdf

# Ensure file is readable
chmod 644 /path/to/paper.pdf

# Check file format
file /path/to/paper.pdf  # Should be PDF

# Try manual metadata entry if PDF parsing fails
```

---

### Issue: Knowledge tree not building

**Symptoms:** Tree shows empty after uploading papers

**Solution:**
```python
# Check if papers were added successfully
import sqlite3
conn = sqlite3.connect('data/papers.db')
papers = conn.execute("SELECT * FROM papers").fetchall()
print(f"Total papers: {len(papers)}")

# If papers exist but tree is empty, rebuild tree
from src.knowledge_graph import KnowledgeGraph
kg = KnowledgeGraph('data/papers.db')
tree = kg.build_tree()
print(tree)
```

---

### Issue: Recommendations not showing

**Symptoms:** No recommendations returned

**Solution:**
```bash
# Check if you have enough papers
# Minimum 5 papers recommended for good recommendations

# Verify experiment has keywords
# Check logs for errors
tail -f logs/app.log

# Try advanced mode (includes web scraping)
```

---

### Issue: PPT generation fails

**Error:**
```
Error generating PPT: No experiments selected
```

**Solution:**
```bash
# Ensure you have at least 1 experiment
# Check if experiments are linked to papers

# Verify ppt-outline is installed
pip install python-pptx

# Try regenerating
```

---

## ❌ Common Errors

### Error: "NLP model not found"

**Cause:** spaCy model not downloaded

**Solution:**
```bash
python -m spacy download en_core_web_sm
```

---

### Error: "Database schema mismatch"

**Cause:** Database from older version

**Solution:**
```bash
# Backup old database
cp data/papers.db data/papers.db.old

# Run migration
python3 scripts/migrate_database.py

# Or recreate database
rm data/papers.db
python3 src/web_app_v2.py  # Will create new database
```

---

### Error: "ImportError: No module named 'jieba'"

**Cause:** Chinese NLP package not installed

**Solution:**
```bash
pip install jieba
```

---

### Error: "CORS error" in browser

**Cause:** Cross-origin request blocked

**Solution:**
```python
# In web_app_v2.py, add CORS support
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

---

## ❓ FAQ

### Q: How many papers can Academic Lobster handle?

**A:** Tested up to 50,000 papers with <10% performance degradation. Recommended: 10,000 papers for optimal performance.

---

### Q: Can I use it offline?

**A:** Yes! Academic Lobster is 100% local by default. Only the "Advanced" recommendation mode requires internet access.

---

### Q: Is my data private?

**A:** Yes! All data stays on your device. No cloud uploads, no telemetry, no tracking.

---

### Q: Can I export my data?

**A:** Yes! Export to BibTeX, RIS, EndNote, CSV, or JSON. See [Export Guide](docs/user-guide.md#export).

---

### Q: How do I backup my data?

**A:** Simply copy the `data/` directory:
```bash
cp -r data/ /backup/location/
```

---

### Q: Can multiple users share the same database?

**A:** Not recommended for SQLite. For multi-user setups, use PostgreSQL (coming in v2.1).

---

### Q: How do I update to a new version?

**A:**
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt

# Restart application
pkill -f web_app_v2.py
python3 src/web_app_v2.py
```

---

### Q: Where are logs stored?

**A:** `logs/` directory:
- `logs/app.log` - Application logs
- `logs/audit.log` - Audit logs
- `logs/error.log` - Error logs

---

### Q: How do I report a bug?

**A:** Create an issue on GitHub: https://github.com/bieyl/research/issues

Include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (OS, Python version, etc.)

---

### Q: How do I request a feature?

**A:** Create an issue on GitHub with the "feature request" label.

---

## 🆘 Still Need Help?

### Resources

- **Documentation:** https://github.com/bieyl/research/tree/main/academic-lobster/docs
- **GitHub Issues:** https://github.com/bieyl/research/issues
- **Email:** bieyunlong1@163.com

### Before Asking for Help

1. ✅ Search existing issues
2. ✅ Check documentation
3. ✅ Review this troubleshooting guide
4. ✅ Collect error messages and logs
5. ✅ Note your environment details

### Providing Debug Information

When asking for help, include:

```markdown
## Environment
- OS: [e.g., macOS 14.0]
- Python: [e.g., 3.11]
- Academic Lobster: [e.g., 2.0.0]

## Issue Description
[Describe the problem]

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Error Messages
[Paste error messages]

## Logs
[Paste relevant log entries]

## What I've Tried
[List troubleshooting steps you've taken]
```

---

**Happy researching!** 🦞
