# Security Model - Academic Lobster v2

**Version:** 2.0.0  
**Last Updated:** March 17, 2026

---

## 🔒 Security Principles

Academic Lobster v2 is built on a **local-first, privacy-by-design** architecture.

| Principle | Implementation | Verification |
|-----------|----------------|--------------|
| **Local Storage** | All private data stays on your device | No network calls by default |
| **No Cloud Uploads** | Zero external API dependencies | All processing local |
| **Compliant Scraping** | Only public abstracts, with clear attribution | Auto-cleanup after session |
| **Audit Trail** | Full operation logging | `logs/audit.log` |

---

## 🛡️ Threat Model

### Potential Threats

#### 1. Malicious Input

**Threat:** User uploads malicious PDF with embedded scripts

**Mitigation:**
- ✅ PDF parsing in sandboxed process
- ✅ No JavaScript execution
- ✅ Input validation on all metadata fields
- ✅ File type verification (magic bytes)

**Residual Risk:** Low

---

#### 2. Data Leakage

**Threat:** Sensitive research data accidentally uploaded to cloud

**Mitigation:**
- ✅ 100% local storage (SQLite on device)
- ✅ No cloud sync by default
- ✅ Network calls only for optional web scraping
- ✅ Clear user consent for web features

**Residual Risk:** Very Low

---

#### 3. Unauthorized Access

**Threat:** Unauthorized user accesses local database

**Mitigation:**
- ✅ File permissions (600 for database files)
- ✅ Optional database encryption (AES-256)
- ✅ API key authentication for production deployment
- ✅ Audit logging of all access

**Residual Risk:** Low

---

#### 4. Injection Attacks

**Threat:** SQL injection via search queries

**Mitigation:**
- ✅ Parameterized queries (no string concatenation)
- ✅ Input sanitization
- ✅ ORM with built-in protection
- ✅ Regular security audits

**Residual Risk:** Very Low

---

## 🔐 Security Implementation

### 1. Container Isolation (Optional)

```bash
# Run in Docker container
docker run -p 5001:5001 \
  -v academic-lobster-data:/app/data \
  --read-only \
  --cap-drop=ALL \
  academic-lobster:latest
```

**Benefits:**
- Filesystem isolation
- Network isolation
- Process isolation
- Non-root user

---

### 2. Access Control (Production)

```python
# API key authentication
@app.before_request
def check_auth():
    if request.endpoint and not requires_auth(request.endpoint):
        return None
    
    api_key = request.headers.get('X-API-Key')
    if not api_key or api_key != current_app.config['API_KEY']:
        return jsonify({'error': 'Unauthorized'}), 401
```

**Configuration:**
```yaml
# config.yaml
security:
  api_key: "your-secret-key-here"
  rate_limit: 100  # requests per minute
  cors_origins:
    - "https://your-domain.com"
```

---

### 3. Input Validation

```python
from marshmallow import Schema, fields, validate

class PaperSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(max=500))
    authors = fields.List(fields.Str(), validate=validate.Length(max=50))
    year = fields.Int(validate=validate.Range(min=1900, max=2100))
    venue = fields.Str(validate=validate.Length(max=200))
    abstract = fields.Str(validate=validate.Length(max=10000))
```

---

### 4. Audit Logging

```python
import logging
from datetime import datetime

# Configure audit logger
audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)
audit_handler = logging.FileHandler('logs/audit.log')
audit_logger.addHandler(audit_handler)

# Log all operations
def log_operation(operation: str, user: str, details: dict):
    audit_logger.info({
        'timestamp': datetime.utcnow().isoformat(),
        'operation': operation,
        'user': user,
        'details': details
    })
```

**Sample Log:**
```json
{
  "timestamp": "2026-03-17T14:30:00Z",
  "operation": "paper_upload",
  "user": "admin",
  "details": {
    "paper_id": 123,
    "title": "ResNet Paper",
    "file_size": 1024000
  }
}
```

---

### 5. Database Encryption (Optional)

```python
from cryptography.fernet import Fernet

class EncryptedDatabase:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)
    
    def encrypt(self, plaintext: str) -> bytes:
        return self.cipher.encrypt(plaintext.encode())
    
    def decrypt(self, ciphertext: bytes) -> str:
        return self.cipher.decrypt(ciphertext).decode()
```

**Configuration:**
```bash
# Generate encryption key
python -m cryptography.fernet generate-key

# Store in environment variable
export ACADEMIC_LOBSTER_DB_KEY="your-key-here"
```

---

## 📋 Security Checklist

### Deployment Security

- [ ] Change default API key
- [ ] Enable HTTPS (production)
- [ ] Configure firewall rules
- [ ] Set up rate limiting
- [ ] Enable audit logging
- [ ] Regular security updates
- [ ] Backup encryption keys securely

### Development Security

- [ ] Use parameterized queries
- [ ] Validate all inputs
- [ ] Sanitize outputs
- [ ] Implement access control
- [ ] Log security events
- [ ] Regular dependency updates
- [ ] Security code review

### User Security

- [ ] Strong passwords (if authentication enabled)
- [ ] Regular backups
- [ ] Secure backup storage
- [ ] Review audit logs periodically
- [ ] Keep software updated

---

## 🔍 Security Testing

### Automated Tests

```bash
# Run security tests
pytest tests/security/ -v

# Dependency audit
pip-audit

# Static analysis
bandit -r src/
```

### Manual Testing

1. **Penetration Testing**
   - Test SQL injection
   - Test XSS vulnerabilities
   - Test CSRF protection
   - Test authentication bypass

2. **Code Review**
   - Review all user inputs
   - Review database queries
   - Review authentication logic
   - Review file handling

3. **Configuration Review**
   - Check default passwords
   - Check API keys
   - Check file permissions
   - Check network exposure

---

## 🚨 Incident Response

### Security Incident Types

| Type | Severity | Response Time |
|------|----------|---------------|
| Data Breach | Critical | Immediate |
| Unauthorized Access | High | < 1 hour |
| Malware Detection | High | < 1 hour |
| Vulnerability Disclosure | Medium | < 24 hours |
| Policy Violation | Low | < 1 week |

### Response Procedure

1. **Detection**
   - Monitor audit logs
   - Review alerts
   - User reports

2. **Containment**
   - Isolate affected systems
   - Revoke compromised credentials
   - Block malicious IPs

3. **Investigation**
   - Collect evidence
   - Analyze logs
   - Determine scope

4. **Remediation**
   - Patch vulnerabilities
   - Reset credentials
   - Update security policies

5. **Recovery**
   - Restore from backup
   - Verify system integrity
   - Resume normal operations

6. **Lessons Learned**
   - Document incident
   - Update procedures
   - Train staff

---

## 📚 Compliance

### GDPR Compliance

- ✅ Data minimization (only collect necessary data)
- ✅ Purpose limitation (use data only for stated purposes)
- ✅ Storage limitation (auto-cleanup after session)
- ✅ Accuracy (users can update their data)
- ✅ Integrity and confidentiality (encryption, access control)
- ✅ Accountability (audit logging)

### Academic Integrity

- ✅ Proper citation of all sources
- ✅ No paywalled content scraping
- ✅ Clear attribution for all recommendations
- ✅ Respect platform Terms of Service

---

## 🎓 Security Best Practices

### For Users

1. **Keep Software Updated**
   ```bash
   # Check for updates
   git pull origin main
   
   # Update dependencies
   pip install --upgrade -r requirements.txt
   ```

2. **Secure Backups**
   ```bash
   # Backup database
   cp data/papers.db backups/papers-$(date +%Y%m%d).db
   
   # Encrypt backup
   gpg -c backups/papers-$(date +%Y%m%d).db
   ```

3. **Review Audit Logs**
   ```bash
   # Check recent activity
   tail -f logs/audit.log
   
   # Search for specific operation
   grep "paper_upload" logs/audit.log
   ```

### For Developers

1. **Security Code Review**
   - Review all user inputs
   - Check for SQL injection
   - Verify access control
   - Test error handling

2. **Dependency Management**
   ```bash
   # Check for vulnerabilities
   pip-audit
   
   # Update dependencies
   pip-review --auto
   ```

3. **Security Testing**
   ```bash
   # Run security tests
   pytest tests/security/ -v
   
   # Static analysis
   bandit -r src/
   
   # Fuzzing
   pytest tests/fuzz/ -v
   ```

---

## 📞 Security Contact

**Report Security Issues:** bieyunlong1@163.com

**PGP Key:** [To be added]

**Response Time:** < 24 hours

---

## 📖 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [GDPR Guidelines](https://gdpr.eu/)

---

**Last Security Audit:** March 17, 2026  
**Next Scheduled Audit:** June 17, 2026  
**Security Status:** ✅ All Clear
