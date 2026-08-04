# MPhil 7610 — Open Science
> **MPhil/PhD Prep | HKUST MPhil 7610 | Open access, open data, open code, reproducibility, FAIR principles, research transparency**  
> **Bilingual 深度自學檔案 · 中英對照**

---

## 問題 1：5 個核心心智模型

1. **Open science accelerates discovery** — freely available research is built upon faster; PINQ experiment (Stodden 2010) showed reproducibility requires open code + data (Nosek et al. 2015, *Science*)

2. **Open access increases citation impact** — Eysenbach (2006, *PLOS Biology*): OA papers cited 1.5–2× more; effect replicated across fields (Piwowar et al. 2018)

3. **Code is a research output** — software is scholarship; cite it as you would a paper (Smith et al. 2016, *PeerJ*)

4. **Reproducibility is the minimum standard** — reproducibility: same data + methods → same results; replicability: new data + methods → same conclusions (NSF 2016)

5. **Open science is an ethical imperative** — publicly funded research should be publicly accessible; taxpayer funds → taxpayer access (EU Open Science Policy)

---

## 問題 2：3 個根本分歧

### 分歧 1：Preprints vs Registered Reports
| Aspect | Preprints | Registered Reports |
|--------|----------|-------------------|
| Timing | Before peer review | Before data collection |
| Priority | Establishes priority | Preregistration of study design |
| Review | Post-submission peer review | Peer review of study design only |
| Acceptance | Conditional on quality | Conditional on design quality only |

### 分歧 2：Open Data vs Protected Data
| Aspect | Full OA | Protected/restricted |
|--------|---------|--------------------|
| Reproducibility | Maximum | Limited |
| Privacy risk | High if human subjects | Protected |
| Commercial sensitivity | Unprotected | Protected |
| Funder mandates | All EU/Horizon funded | NIH requires sharing |

### 分歧 3：CC-BY vs CC0 vs All Rights Reserved
| License | Use case | Attribution | Commercial use |
|---------|---------|------------|----------------|
| CC-BY | Standard OA | Required | Allowed |
| CC0 | Public domain | Not required | Allowed |
| CC-BY-NC | Non-commercial only | Required | Prohibited |
| All Rights Reserved | Traditional | Full control | Prohibited |

---

## 問題 3：10 個深度問題

1. 給定 FAIR principles, 解釋每個 letter (Findable, Accessible, Interoperable, Reusable) 點樣 apply to physics data。

2. 為什麼 code licensing matters? 比較 MIT, GPL, Apache, CC licenses for research software。

3. 給定 dataset containing personal information, 點樣 apply GDPR/PDPO 點樣 apply?

4. 為什麼 registered reports (COS standard) 減少 publication bias?

5. 計算 arXiv citation advantage: 如果 OA paper gets 2× citations over 5 years, economic value of that vs $500 APC?

6. 解釋 DOI 和 metadata standards 點樣 make data findable。

7. 為什麼 GitHub repositories 需要 zenodo DOI for citations?

8. 給定 experimental physics data, 設計 data management plan (DMP)。

9. 為什麼 negative results 需要 published (journal of negative results)?

10. 解釋 ORCID 和它的 role in research attribution。

---

## 深入 1：Open Access Spectrum
**Deep Dive I**

### OA Publishing Models

| Model | Mechanism | Cost | Examples |
|-------|-----------|------|----------|
| Gold OA | Article in OA journal | APC | PLOS, Frontiers, SCOAP³ |
| Green OA | Preprint + repository | Free | arXiv, institutional repo |
| Hybrid | Subscription journal + OA option | APC | *Physical Review* hybrid |
| Diamond OA | Institutionally funded OA | Free | *SciPost*, *Atmos. Chem. Phys.* |

### Practical arXiv Workflow

```bash
# 1. Create account at arxiv.org
# 2. Prepare source files (.tex, .bbl, figures)
# 3. Use arxiv-latex-template on Overleaf
# 4. Upload source + compiled PDF
# 5. Select category: physics.gen-ph, cond-mat.mes-hall, etc.
# 6. Submit → 24-48h admin review → public
# 7. Share DOI link on social media/email
```

---

## 深入 2：Reproducible Research Pipeline
**Deep Dive II**

### Reproducibility Checklist

```python
# requirements.txt
# environment.yml
# Dockerfile or singularity image
# data: DOI via Zenodo/Figshare
# analysis: Jupyter notebook with seed = 42
# results: versioned with git tag v1.0
```

| Item | Standard | Example |
|------|---------|---------|
| Code | GitHub + Zenodo DOI | DOI: 10.5281/zenodo.123456 |
| Data | DOI via Zenodo | DOI: 10.5281/zenodo.234567 |
| Environment | Docker image | DOI: 10.5281/zenodo.345678 |
| Preregistration | OSF time-stamp | osf.io/abcde |

---

## 深入 3：Software Licensing
**Deep Dive III**

| License | Use | Attribution | Commercial | Modifications |
|---------|-----|-----------|-----------|--------------|
| MIT | Most permissive | Required | Allowed | Must keep license |
| Apache 2.0 | Industry projects | Required | Allowed | Must note changes |
| GPL 3 | Shared source | Required | Allowed | Must distribute source |
| CC0 | Public domain | Not required | Allowed | No restrictions |
| CC-BY | Publications | Required | Allowed | Must cite |
| CC-BY-NC | Non-commercial | Required | No | No commercial use |

---

## 自測 1：FAIR Principles Application
**Apply FAIR to a dataset of spectroscopic measurements.**

**Answer:**
**F (Findable):** Assign DOI via Zenodo. Include rich metadata: title, authors, date, instrument parameters, units, wavelength range, sample description.

**A (Accessible):** Store in public repository (Zenodo, figshare). Store in open format (CSV, HDF5). Access via HTTP with API.

**I (Interoperable):** Use standard formats (FITS, HDF5, CSV with units). Include vocabulary standards (UCUM units). Link to related datasets via metadata.

**R (Reusable):** CC-BY license. Include data dictionary (variable names + descriptions). Provide citation format: "Dataset by [Authors], DOI: xxxx."

---

## 📊 Diagram 1: Open Science Stack
```mermaid
mindmap
  root((Open Science))
    Open Access
      Preprints
      Gold OA
      Green OA
    Open Data
      FAIR principles
      Data repositories
      Metadata standards
    Open Code
      GitHub
      Zenodo DOI
      License
    Open Peer Review
      Registered reports
      Post-publication review
    Open Education
      OCW
      Open textbooks
```

## 深度總結

1. **Open access increases impact** — OA papers receive ~1.5–2× more citations; preprinting establishes priority.
2. **FAIR principles are the standard** — apply them to every dataset.
3. **Code is a research output** — license it, cite it, make it reproducible.
4. **Reproducibility requires infrastructure** — Docker, Git, DOIs, preregistration.
5. **Open science is increasingly mandated** — check your funder's OA policy.

---

**自學建議**
- 必讀: Wilkinson et al. (2016) FAIR principles; Nosek et al. (2015) *Science*
- 工具: arXiv, Zenodo, GitHub, OSF, Docker, conda
