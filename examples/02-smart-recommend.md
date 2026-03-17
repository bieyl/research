# Example 2: Add Experiment and Get Smart Recommendations

**Scenario:** Graduate student adds a new experiment and gets relevant literature recommendations

---

## Input

**User Action:** Click "Add Experiment" and fill form

**Experiment Details:**
```
Experiment Name: Swin-T Fine-tuning on ImageNet
Date: 2026-03-11
Research Problem: Image Classification Accuracy
Method: Vision Transformer (Swin Transformer)
Description: Fine-tuned Swin-Tiny on ImageNet dataset with Mixup augmentation
Results: Top-1 Accuracy: 78.5%, Training Time: 12 hours
```

**Linked Papers:**
- 📄 Swin Transformer (Liu et al., 2021)
- 📄 Vision Transformer (Dosovitskiy et al., 2021)

---

## Processing

**System automatically:**
1. ✅ Save experiment to database
2. ✅ Extract keywords from experiment description
3. ✅ Match against local knowledge base (Local Mode)
4. ✅ Fetch public abstracts from arXiv (Advanced Mode, user-triggered)
5. ✅ Calculate relevance scores (keyword 40% + method 30% + domain 20% + recency 10%)
6. ✅ Return ranked recommendations

**Processing Time:**
- Local Mode: 45ms
- Advanced Mode: 250ms

---

## Output

### Smart Recommendations

**For Experiment:** Swin Transformer Fine-tuning

| Rank | Paper | Relevance | Source | Match Reason |
|------|-------|-----------|--------|--------------|
| 1 | ⭐⭐⭐⭐⭐ Swin Transformer (Liu et al., 2021) | 95/100 | Local | Direct architecture reference |
| 2 | ⭐⭐⭐⭐ Vision Transformer (Dosovitskiy et al., 2021) | 88/100 | Local | Foundation architecture |
| 3 | ⭐⭐⭐ ConViT: Improving Vision Transformers (d'Ascoli et al., 2021) | 75/100 | arXiv | Improvement direction |
| 4 | ⭐⭐⭐ CaiT: Going Deeper with Image Transformers (Touvron et al., 2021) | 68/100 | arXiv | Related architecture |
| 5 | ⭐⭐ DeiT: Training Data-efficient Image Transformers (Touvron et al., 2021) | 62/100 | Local | Training strategy |

### Recommendation Details

**#1: Swin Transformer (95/100)**
```
Match Breakdown:
- Keyword Match (40%): 38/40 - "Swin", "Transformer", "fine-tuning"
- Method Similarity (30%): 28/30 - Same architecture family
- Domain Relevance (20%): 19/20 - Image classification
- Recency (10%): 10/10 - Published within 5 years

Key Insights:
- This is the original paper for your method
- Contains architecture details and hyperparameters
- Recommended baseline for comparison
```

**#2: Vision Transformer (88/100)**
```
Match Breakdown:
- Keyword Match (40%): 35/40 - "Transformer", "ImageNet"
- Method Similarity (30%): 25/30 - Foundation architecture
- Domain Relevance (20%): 18/20 - Image classification
- Recency (10%): 10/10 - Recent work

Key Insights:
- First application of transformers to vision
- Important background for understanding Swin
- Patch-based approach inspired Swin
```

---

## Performance Comparison

| Mode | Latency | Privacy | Results |
|------|---------|---------|---------|
| **Local** | 45ms | 🔒 100% private | 3 papers from your library |
| **Advanced** | 250ms | ⚠️ Public abstracts | 5 papers (3 local + 2 arXiv) |

---

## Screenshot

![Smart Recommendations](../assets/screenshots/smart-recommend.png)
*Figure: Smart recommendation results showing relevance scores and match reasons*

---

## Algorithm Details

**Relevance Score Calculation:**
```python
def calculate_relevance(experiment, paper):
    keyword_score = keyword_matching(experiment.keywords, paper.keywords) * 0.40
    method_score = method_similarity(experiment.method, paper.method) * 0.30
    domain_score = domain_relevance(experiment.domain, paper.domain) * 0.20
    recency_score = recency_factor(paper.year) * 0.10
    
    total = keyword_score + method_score + domain_score + recency_score
    return total * 100  # Scale to 0-100
```

---

**Try it yourself:**
1. Add an experiment in the Web UI
2. Link to relevant papers
3. Click "Get Recommendations"
4. Review suggested papers with relevance scores
