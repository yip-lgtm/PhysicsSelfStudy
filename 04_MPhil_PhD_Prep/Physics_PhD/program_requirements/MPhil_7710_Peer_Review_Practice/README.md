# MPhil 7710 — Peer Review Practice
> **MPhil/PhD Prep | HKUST MPhil 7710 | Reviewing manuscripts, writing reviews, editorial process, journal metrics, reviewer etiquette**  
> **Bilingual 深度自學檔案 · 中英對照**

---

## 問題 1：5 個核心心智模型

1. **Peer review is the quality control of science** — it is imperfect but the best system we have; double-blind studies show reviewers can't detect all fraud, but they do catch major methodological flaws (Click et al. 2023, *PLOS Biology*)

2. **A good review improves the paper** — the goal is to help authors publish better science, not to reject; the best reviews are constructive, specific, and fair (COSE Peer Review Guidelines)

3. **Reviewer recognition is evolving** — Publons, ORCID, and mandatory reviewer acknowledgment are transforming reviewing from invisible labor to visible contribution (Nature Research 2019)

4. **Biases affect reviews** — confirmation bias, prestige bias, affiliation bias; acknowledging these helps mitigate them (Lee et al. 2013, *Science*)

5. **Editorial decisions weigh multiple factors** — reviewers recommend; editors decide; fit, space, balance, and strategic considerations influence final decisions (Council of Science Editors)

---

## 問題 2：3 個根本分歧

### 分歧 1：Single-blind vs Double-blind Review
| Aspect | Single-blind | Double-blind |
|--------|-------------|--------------|
| Reviewer knows author | Yes | No |
| Author knows reviewer | No | No |
| Reduces prestige bias | Partially | Better |
| Implementation | Standard | Difficult (author identifiability) |
| Evidence | Some bias detected | Reduces some bias |

### 分歧 2：Open vs Closed Peer Review
| Aspect | Open review | Closed review |
|--------|------------|---------------|
| Reviewer identity | Public | Anonymous |
| Transparency | High | Low |
| Quality | Mixed evidence | Standard |
| Adoption | Increasing | Still dominant |

### 分歧 3：Pre-Publication vs Post-Publication Review
| Aspect | Pre-publication | Post-publication |
|--------|----------------|-----------------|
| Timing | Before publication | After publication |
| Gatekeeping | Yes (filters) | No (all published) |
| Example | Traditional journals | F1000Research, PeerJ |

---

## 問題 3：10 個深度問題

1. 給定 paper you need to review, 設計 structure: summary → strengths → weaknesses → detailed comments → recommendation。

2. 為什麼 statistical review (statistician on review panel) 越來越被要求?

3. 給定 paper with flawed statistics (low N, p-hacking evidence), 點樣 write constructive review?

4. 為什麼 desk rejection 唔等於 quality judgment? 點樣 interpret?

5. 給定 revision with incomplete response to prior comments, 點樣 write second review?

6. 為什麼 conflict of interest (COI) disclosure 係 mandatory?

7. 解釋 editorial decision categories: accept, minor revision, major revision, reject, reject + resubmit。

8. 給定 paper you think should be accepted, 點樣 write a strong support review?

9. 為什麼 reviewer burnout 係 system-level problem?

10. 解釋 journal rejection rates 和 acceptance rates 點樣 calculate 和 interpret。

---

## 深入 1：Review Structure
**Deep Dive I**

### Standard Review Format

**Section 1: Summary (1 paragraph)**
> "The authors study [topic] using [methods]. They find [main result]. The paper is generally well-written and the experiments are carefully done. The main concern is [major issue]."

**Section 2: Major Issues (numbered)**
- Be specific: quote relevant sections
- Distinguish essential vs. nice-to-have changes
- Explain WHY each issue matters

**Section 3: Minor Issues (numbered)**
- Typos, figure quality, reference format
- Less critical suggestions

**Section 4: Recommendation**
- Accept / Minor Revision / Major Revision / Reject / Resubmit
- Justification

### Example Constructive Review

> **Major Issue 1:** The sample size of $n = 12$ per group is underpowered for detecting the expected effect size of $d = 0.4$. A power calculation indicates $n = 55$ per group is needed. Please either conduct additional experiments or justify the current sample size.

---

## 深入 2：Editorial Process
**Deep Dive II**

### Journal Workflow

```mermaid
graph TD
    A[Submission] --> B[Editor desk check]
    B -->|Desk reject| C[Return to author]
    B -->|Send to reviewers| D[2-3 reviewers]
    D --> E[Reviewer recommendations]
    E --> F[Editor decision]
    F --> G[Accept/Minor/Major/Reject]
    G --> H[Revision?]
    H -->|Yes| I[Review revision]
    I --> J{Accept?}
    J -->|Yes| K[Accept]
    J -->|No| L[More revisions]
    L --> I
    K --> M[Publication]
```

---

## 自測 1：Constructive Review Writing
**Review: Paper claims "quantum supremacy" but methodology has flaws. Write constructive review.**

**Answer:**
> **Summary:** The authors claim quantum supremacy using a photonic processor. While the goal is significant, I have concerns about the benchmarking methodology and claims of classical intractability.
>
> **Major Issue 1:** The classical simulation used for comparison (p. 8) is not the best available. Recent work (Smith et al. 2024) demonstrated classical simulation with 3× fewer qubits. The paper should benchmark against state-of-the-art classical methods.
>
> **Major Issue 2:** The claim of "quantum supremacy" requires demonstrating that no classical algorithm could perform the same task within the same time. The paper does not address this criterion explicitly. Please revise the framing or provide the required evidence.
>
> **Recommendation:** Major revision. The results are potentially significant, but the framing and benchmarking require substantial clarification.

---

## 📊 Diagram 1: Review Workflow
```mermaid
graph TD
    A[Paper arrives] --> B[Desk evaluation]
    B --> C[Send to 2-3 reviewers]
    C --> D[Review period 2-4 weeks]
    D --> E[Reviews received]
    E --> F[Editor weighs options]
    F --> G[Decision letter]
    G --> H[Revision or appeal]
```

## 深度總結

1. **A good review is constructive** — aim to help authors publish better science.
2. **Review structure matters** — summary, major issues, minor issues, recommendation.
3. **Be specific** — quote lines, pages, figures; vague reviews are unhelpful.
4. **Reviewer recognition is improving** — Publons, ORCID, and mandatory acknowledgment are standardizing credit.
5. **Reviewing develops your own writing** — reviewing teaches you to spot weaknesses.

---

**自學建議**
- 必讀: COSE Peer Review Guidelines; Nature Peer Review Credit; COPE Ethical Guidelines
- 工具: Publons, ORCID, PubMed peer review
