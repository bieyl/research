# Example 5: Export Knowledge Tree for Literature Review

**Scenario:** Graduate student exports knowledge tree for thesis literature review chapter

---

## Input

**User Action:** Click "Export" → Select "Literature Review" format

**Export Options:**
- ✅ Format: Markdown / BibTeX / EndNote / RIS
- ✅ Scope: Full knowledge tree / Selected branches
- ✅ Include: Abstracts / Keywords / Notes
- ✅ Citation Style: APA / MLA / Chicago / IEEE

**Selected Branch:**
```
├── [Method] Vision Transformer
│   ├── 📄 ViT (Dosovitskiy et al., 2021)
│   ├── 📄 Swin Transformer (Liu et al., 2021)
│   ├── 📄 DeiT (Touvron et al., 2021)
│   └── 📄 CaiT (Touvron et al., 2021)
```

---

## Processing

**System automatically:**
1. ✅ Traverse selected knowledge tree branch
2. ✅ Gather all papers and metadata
3. ✅ Sort by year / relevance / citation
4. ✅ Generate literature review outline
5. ✅ Export citations in selected format
6. ✅ Include knowledge structure as figure

**Processing Time:** 85ms

---

## Output

### Literature Review Outline (Markdown)

```markdown
# Literature Review: Vision Transformers for Image Classification

## Overview
This section reviews the evolution of vision transformers, from the original 
Vision Transformer (ViT) to recent hierarchical and efficient variants.

## Timeline
```
2020: Vision Transformer (ViT) - First application of transformers to vision
2021: DeiT - Data-efficient training without large datasets
2021: Swin Transformer - Hierarchical architecture with shifted windows
2021: CaiT - Going deeper with image transformers
```

## Key Papers

### 1. Vision Transformer (ViT)
**Citation:** Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., 
Unterthiner, T., ... & Houlsby, N. (2021). An image is worth 16x16 words: 
Transformers for image recognition at scale. ICLR.

**Abstract:** We propose the Vision Transformer (ViT), which applies the 
transformer architecture to image classification by splitting images into 
patches and treating them as sequences...

**Key Contributions:**
- First to apply pure transformer to image classification
- Achieves SOTA when pretrained on large datasets
- Requires substantial computational resources

**My Notes:** Foundation model for all subsequent ViT variants. Must cite in introduction.

---

### 2. Swin Transformer
**Citation:** Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., ... & Guo, B. (2021). 
Swin transformer: Hierarchical vision transformer using shifted windows. ICCV.

**Abstract:** We present Swin Transformer, which builds a hierarchical 
representation from image patches...

**Key Contributions:**
- Hierarchical architecture with shifted windows
- Linear computational complexity w.r.t. image size
- SOTA on multiple vision benchmarks

**My Notes:** Most relevant to my work. Use as primary baseline.

---

### 3. DeiT (Data-efficient Image Transformers)
**Citation:** Touvron, H., Cord, M., Douze, M., Massa, F., Sablayrolles, A., & Jégou, H. (2021). 
Training data-efficient image transformers & distillation through attention. ICML.

**Abstract:** We train a transformer model without convolutions from scratch 
on ImageNet classification task...

**Key Contributions:**
- Training strategy for data-efficient ViT
- Knowledge distillation from CNN to transformer
- Competitive results without large-scale pretraining

**My Notes:** Useful for my limited dataset scenario.

---

## Synthesis

The evolution of vision transformers shows a clear trend:
1. **ViT (2021)** established the foundation but required massive datasets
2. **DeiT (2021)** improved data efficiency through distillation
3. **Swin (2021)** introduced hierarchical structure for better scalability
4. **CaiT (2021)** pushed depth limits with layer-scale and class attention

My work builds on Swin Transformer by [your contribution here].

## References

[1] Dosovitskiy, A., et al. (2021). ICLR.
[2] Liu, Z., et al. (2021). ICCV.
[3] Touvron, H., et al. (2021). ICML.
[4] Touvron, H., et al. (2021). ICCV.
```

### BibTeX Export

```bibtex
@inproceedings{dosovitskiy2021image,
  title={An image is worth 16x16 words: Transformers for image recognition at scale},
  author={Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and others},
  booktitle={ICLR},
  year={2021}
}

@inproceedings{liu2021swin,
  title={Swin transformer: Hierarchical vision transformer using shifted windows},
  author={Liu, Ze and Lin, Yutong and Cao, Yue and others},
  booktitle={ICCV},
  year={2021}
}

@inproceedings{touvron2021training,
  title={Training data-efficient image transformers \& distillation through attention},
  author={Touvron, Hugo and Cord, Matthieu and Douze, Matthijs and others},
  booktitle={ICML},
  year={2021}
}
```

### Knowledge Tree Figure (TikZ for LaTeX)

```latex
\begin{tikzpicture}[
  node distance=1.5cm,
  every node/.style={rectangle, draw, rounded corners, fill=blue!10}
]
\node (problem) {Image Classification};
\node (method) [below of=problem] {Vision Transformer};
\node (vit) [below left of=method, xshift=-2cm] {ViT (2021)};
\node (swin) [below of=method] {Swin (2021)};
\node (deit) [below right of=method, xshift=2cm] {DeiT (2021)};
\node (cait) [below of=swin] {CaiT (2021)};

\draw (problem) -- (method);
\draw (method) -- (vit);
\draw (method) -- (swin);
\draw (method) -- (deit);
\draw (swin) -- (cait);
\end{tikzpicture}
```

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Export Time | 85ms |
| Papers Exported | 4 |
| Output Size | 5.2KB (Markdown) |
| Citations Generated | 4 (BibTeX) |
| Time Saved | 1-2 hours (manual compilation) |

---

## Screenshot

![Export Interface](../assets/screenshots/export.png)
*Figure: Export dialog showing format options and preview*

---

## Supported Export Formats

| Format | Use Case | Tools |
|--------|----------|-------|
| **Markdown** | Literature review, notes | Obsidian, Notion, Typora |
| **BibTeX** | LaTeX papers | Overleaf, TeXShop |
| **EndNote** | Manuscript preparation | EndNote Desktop |
| **RIS** | Reference managers | Zotero, Mendeley, RefWorks |
| **CSV** | Data analysis | Excel, pandas |
| **JSON** | Programmatic access | Custom scripts |

---

**Try it yourself:**
1. Build knowledge tree with 10+ papers
2. Select a research branch
3. Click "Export" → "Literature Review"
4. Choose format and citation style
5. Copy to your thesis document
