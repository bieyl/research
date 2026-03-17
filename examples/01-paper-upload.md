# Example 1: Upload Papers and Build Knowledge Tree

**Scenario:** Graduate student uploads 5 papers to build initial knowledge base

---

## Input

**User Action:** Click "Add Paper" button and upload PDF

**Files Uploaded:**
1. `resnet-he-2016.pdf` - "Deep Residual Learning for Image Recognition"
2. `identity-mappings-he-2016.pdf` - "Identity Mappings in Deep Residual Networks"
3. `swin-transformer-liu-2021.pdf` - "Swin Transformer: Hierarchical Vision Transformer"
4. `vit-dosovitskiy-2020.pdf` - "An Image is Worth 16x16 Words: Transformers for Image Recognition"
5. `focal-loss-lin-2017.pdf` - "Focal Loss for Dense Object Detection"

---

## Processing

**System automatically:**
1. ✅ Parse PDF metadata (title, authors, year, venue)
2. ✅ Extract keywords using NLP (spaCy + jieba)
3. ✅ Build knowledge tree hierarchy
4. ✅ Store in SQLite database

**Processing Time:** 2.3 seconds (for 5 papers)

---

## Output

### Knowledge Tree Generated

```
Research Knowledge Tree
├── [Problem] Image Classification Accuracy
│   ├── [Method] Residual Connection
│   │   ├── 📄 ResNet (He et al., CVPR 2016)
│   │   └── 📄 Identity Mappings (He et al., ECCV 2016)
│   ├── [Method] Vision Transformer
│   │   ├── 📄 ViT (Dosovitskiy et al., ICLR 2021)
│   │   └── 📄 Swin Transformer (Liu et al., ICCV 2021)
│   └── [Method] Loss Function
│       └── 📄 Focal Loss (Lin et al., ICCV 2017)
```

### Metadata Extracted

| Paper | Title | Authors | Year | Venue | Keywords |
|-------|-------|---------|------|-------|----------|
| 1 | Deep Residual Learning... | He et al. | 2016 | CVPR | residual, deep learning, CNN |
| 2 | Identity Mappings... | He et al. | 2016 | ECCV | residual, identity mapping |
| 3 | Swin Transformer... | Liu et al. | 2021 | ICCV | transformer, attention, hierarchical |
| 4 | An Image is Worth 16x16... | Dosovitskiy et al. | 2021 | ICLR | transformer, attention, ViT |
| 5 | Focal Loss... | Lin et al. | 2017 | ICCV | loss function, object detection |

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Total Processing Time | 2.3s |
| Average per Paper | 0.46s |
| PDF Parsing | 1.2s |
| NLP Extraction | 0.8s |
| Tree Building | 0.3s |
| Memory Usage | 45MB |

---

## Screenshot

![Upload Papers Interface](../assets/screenshots/upload-papers.png)
*Figure: Paper upload interface showing 5 papers successfully added*

---

## Next Steps

After uploading papers, user can:
1. ✅ View knowledge tree in "Knowledge Tree" tab
2. ✅ Add experiments and link to papers
3. ✅ Get smart recommendations for new experiments
4. ✅ Generate PPT for lab meeting

---

**Try it yourself:**
```bash
# Start the application
cd academic-lobster
pip install -r requirements.txt
python3 src/web_app_v2.py

# Access: http://localhost:5001
# Navigate to "Add Paper" → Upload PDFs
```
