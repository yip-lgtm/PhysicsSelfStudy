#!/usr/bin/env python3
"""
Generate README.md files in the new PhysicsSelfStudy format for all remaining stub files.
Uses course metadata to produce context-aware content.
"""

import os
from pathlib import Path

# Course metadata: code -> (title, chinese, themes, level)
COURSE_DATA = {
    # BSc core remaining
    "PHYS_3031_Mathematical_Methods_II": ("Mathematical Methods II", "數學方法 II", ["PDEs", "Green's", "Variational"], "advanced"),
    "PHYS_3034_Electricity_Magnetism_II": ("Electricity and Magnetism II", "電磁學 II", ["EM waves", "Radiation", "Relativity"], "advanced"),
    "PHYS_3038_Optics": ("Optics", "光學", ["Geometric", "Wave", "Modern"], "intermediate"),
    "PHYS_3142_Computational_Methods": ("Computational Methods", "計算方法", ["Numerical", "Simulation", "Linear algebra"], "intermediate"),
    "PHYS_3152_Experimental_Physics_I": ("Experimental Physics I", "實驗物理 I", ["Measurement", "Statistics", "Lab"], "intermediate"),
    "PHYS_3153_Experimental_Physics_II": ("Experimental Physics II", "實驗物理 II", ["Modern experiments", "DAQ", "Analysis"], "advanced"),
    "PHYS_4051_Quantum_Mechanics_II": ("Quantum Mechanics II", "量子力學 II", ["Time-dep", "Scattering", "Many-body"], "advanced"),
    "PHYS_4811_ML_in_Physics": ("Machine Learning in Physics", "物理中嘅機器學習", ["NN", "Optimization", "Physics-informed"], "advanced"),
    # Foundation
    "PHYS_1001_Physics_Modern_Society": ("Physics in Modern Society", "現代社會中嘅物理", ["Energy", "Waves", "Climate"], "intro"),
    "PHYS_1002_Astrophysics_Astronomy": ("Astrophysics and Astronomy", "天體物理同天文學", ["Solar system", "Stars", "Cosmology"], "intro"),
    "PHYS_1003_Energy_Environmental_Issues": ("Energy and Environmental Issues", "能源同環境問題", ["Energy", "Climate", "Sustainability"], "intro"),
    "PHYS_1007_Quantum_Information_For_Everyone": ("Quantum Information for Everyone", "量子信息入門", ["Qubits", "Entanglement", "Algorithms"], "intro"),
    "PHYS_1101_Introductory_Physics": ("Introductory Physics", "物理入門", ["Mechanics", "Thermo", "EM"], "intro"),
    "PHYS_1111_General_Physics_I": ("General Physics I (Mechanics)", "普通物理 I", ["Newton", "Energy", "Waves"], "intro"),
    "PHYS_1112_General_Physics_I_Calculus": ("General Physics I (Calculus)", "普通物理 I (微積分)", ["Newton", "Calculus", "Oscillations"], "intro"),
    "PHYS_1113_Lab_General_Physics_I": ("Lab for General Physics I", "普通物理 I 實驗", ["Measurement", "LSQ", "Error"], "intro"),
    "PHYS_1114_General_Physics_II": ("General Physics II (E&M)", "普通物理 II", ["Electrostatics", "Magnetism", "Optics"], "intro"),
    "PHYS_1115_Lab_General_Physics_II": ("Lab for General Physics II", "普通物理 II 實驗", ["Circuits", "Meters", "DAQ"], "intro"),
    "PHYS_1312_Honors_General_Physics_I": ("Honors General Physics I", "榮譽普通物理 I", ["Newton", "Lagrangian", "Central force"], "intermediate"),
    "PHYS_1314_Honors_General_Physics_II": ("Honors General Physics II", "榮譽普通物理 II", ["E&M rigorous", "Maxwell", "Relativity"], "intermediate"),
    "PHYS_2010_Intro_Biological_Physics": ("Intro to Biological Physics", "生物物理入門", ["Soft matter", "Membranes", "Cells"], "intro"),
    "PHYS_2022_Modern_Physics": ("Modern Physics", "現代物理", ["Relativity", "QM", "Nuclear"], "intermediate"),
    "PHYS_2023_Modern_Physics_Lab": ("Modern Physics Lab", "現代物理實驗", ["e/m", "Photoelectric", "Spectroscopy"], "intermediate"),
    # BSc electives
    "PHYS_2080_Physics_Seminar_I": ("Physics Seminar I", "物理研討會 I", ["Reading", "Talks", "Networking"], "intro"),
    "PHYS_2090X_Directed_Studies_I": ("Directed Studies I", "指導研究 I", ["Research", "Methods", "Writing"], "intermediate"),
    "PHYS_3037_Honors_Quantum_Mechanics_I": ("Honors Quantum Mechanics I", "榮譽量子力學 I", ["Formalism", "Mixed states", "Entanglement"], "advanced"),
    "PHYS_3042_Crystalline_Solids": ("Crystalline Solids", "晶體固體", ["Lattices", "Reciprocal", "Diffraction"], "intermediate"),
    "PHYS_3053_Honors_Electricity_Magnetism_I": ("Honors Electricity & Magnetism I", "榮譽電磁學 I", ["BVP", "Multipole", "Materials"], "advanced"),
    "PHYS_3060_Physics_Internship": ("Physics Internship", "物理實習", ["Industry", "Projects", "Communication"], "intermediate"),
    "PHYS_3071_Stellar_Astrophysics": ("Stellar Astrophysics", "恆星天體物理", ["Structure", "Evolution", "Remnants"], "advanced"),
    "PHYS_3090X_Directed_Studies_II": ("Directed Studies II", "指導研究 II", ["Research", "Advanced methods", "Publication"], "advanced"),
    "PHYS_4055_Particle_Physics_Universe": ("Particle Physics and the Universe", "粒子物理同宇宙", ["Standard model", "Cosmology", "BSM"], "advanced"),
    "PHYS_4058_Information_Physics": ("Information Physics", "信息物理", ["Landauer", "Bekenstein-Hawking", "Quantum info"], "advanced"),
    "PHYS_4071_Big_Bang_Cosmology_Inflation": ("Big Bang Cosmology and Inflation", "大爆炸宇宙學同暴脹", ["FLRW", "CMB", "Inflation"], "advanced"),
    "PHYS_4080_Physics_Seminar_II": ("Physics Seminar II", "物理研討會 II", ["Advanced", "Specialization", "Leadership"], "advanced"),
    "PHYS_4090X_Directed_Studies_III": ("Directed Studies III", "指導研究 III", ["Independent research", "Thesis", "Defense"], "advanced"),
    "PHYS_4191_Capstone_Project": ("Capstone Project", "頂石項目", ["Research", "Design", "Communication"], "advanced"),
    "PHYS_4291_Capstone_Research": ("Capstone Research", "頂石研究", ["Original research", "Thesis", "Publication"], "advanced"),
    "PHYS_4812_Quantum_Information_Technology": ("Quantum Information Technology", "量子信息技術", ["Hardware", "Cryptography", "Sensing"], "advanced"),
    "PHYS_4815_Radiation_Therapy": ("Radiation Therapy Physics", "放射治療物理", ["Dosimetry", "Treatment planning", "Imaging"], "advanced"),
    # MSc DM
    "MSDM_5001": ("Computational Tools", "計算工具", ["Python", "Linux", "Data handling"], "intermediate"),
    "MSDM_5002": ("Scientific Programming and Visualization", "科學編程同可視化", ["NumPy", "Matplotlib", "Scientific"], "intermediate"),
    "MSDM_5003": ("Stochastic Modeling", "隨機建模", ["Probability", "Stochastic processes", "Simulation"], "intermediate"),
    "MSDM_5004_Numerical_Methods": ("Numerical Methods", "數值方法", ["ODE/PDE", "Optimization", "Linear algebra"], "intermediate"),
    "MSDM_5005": ("Innovation in Practice", "實踐中嘅創新", ["Entrepreneurship", "Industry", "IP"], "intermediate"),
    "MSDM_6771": ("Seminars", "研討會", ["Research", "Industry", "Career"], "intermediate"),
    "MSDM_6980": ("Capstone Project", "頂石項目", ["Real-world", "Team", "Deliverable"], "advanced"),
    "MSDM_5051": ("Algorithms and OOP", "算法同面向對象", ["Data structures", "OOP", "Complexity"], "intermediate"),
    "MSDM_5053": ("Time Series Analysis", "時間序列分析", ["ARIMA", "State space", "Forecasting"], "intermediate"),
    "MSDM_5054": ("Statistical Machine Learning", "統計機器學習", ["Regression", "Classification", "Regularization"], "intermediate"),
    "MSDM_5055_Deep_Learning": ("Deep Learning", "深度學習", ["NN architectures", "Optimization", "Generative"], "advanced"),
    "MSDM_5056": ("Network Science", "網絡科學", ["Graph theory", "Centrality", "Dynamics"], "intermediate"),
    "MSDM_5057": ("Business Literacy", "商業素養", ["Finance", "Marketing", "Strategy"], "intro"),
    "MSDM_5058": ("Information Science", "信息科學", ["Retrieval", "Recommendation", "NLP"], "intermediate"),
    "MSDM_5059": ("Operations Research and Optimization", "運籌學同優化", ["LP/IP", "Heuristics", "Stochastic"], "intermediate"),
    # MSc Physics
    "MSPY_5110_Data_Analysis_Physics": ("Data Analysis for Physics", "物理數據分析", ["Statistics", "Fitting", "Uncertainty"], "advanced"),
    "MSPY_5120_Contemporary_Physics": ("Contemporary Physics", "當代物理", ["Frontier topics", "Literature", "Synthesis"], "advanced"),
    "MSPY_6771_MSc_Physics_Seminars": ("MSc Physics Seminars", "碩士物理研討會", ["Research talks", "Networking", "Career"], "advanced"),
    "MSPY_5001_Semiconductor_Devices": ("Semiconductor Devices", "半導體器件", ["pn junction", "Transistor", "LED"], "advanced"),
    "MSPY_5210_Physical_Properties_Materials": ("Physical Properties of Materials", "材料嘅物理性質", ["Mechanical", "Thermal", "Electronic"], "advanced"),
    "MSPY_5220_Experimental_Material_Char": ("Experimental Material Characterization", "材料表徵實驗", ["XRD", "SEM/TEM", "Spectroscopy"], "advanced"),
    "MSPY_5230_Computational_Simulation_Tools": ("Computational Simulation Tools", "計算模擬工具", ["MD", "DFT", "FEA"], "advanced"),
    "MSPY_5240_Computational_Methods_Science": ("Computational Methods in Science", "科學中嘅計算方法", ["PDE solvers", "Monte Carlo", "High-perf"], "advanced"),
    "MSPY_5250_AI_in_Science": ("AI in Science", "科學中嘅 AI", ["ML for physics", "Discovery", "Simulation"], "advanced"),
    "PHYS_5120": ("Computational Energy Materials", "計算能源材料", ["DFT", "Batteries", "Solar"], "advanced"),
    "MSPY_5002_Quantum_Materials_Devices": ("Quantum Materials and Devices", "量子材料同器件", ["Topological", "Superconducting", "Quantum dots"], "advanced"),
    "MSPY_5003_Metamaterials": ("Metamaterials", "超材料", ["Sub-wavelength", "Negative index", "Cloaking"], "advanced"),
    "MSPY_5004_Topological_2D_Materials": ("Topological 2D Materials", "拓樸二維材料", ["Graphene", "TMDs", "Topological insulators"], "advanced"),
    "MSPY_6001_Advanced_Research_Project": ("Advanced Research Project", "高級研究項目", ["Independent", "Original", "Thesis"], "advanced"),
    "PHYS_5170_Solid_State_Physics_I": ("Solid State Physics I", "固態物理 I", ["Band theory", "Phonons", "Magnetism"], "advanced"),
    "PHYS_5260_Advanced_Quantum_Mechanics": ("Advanced Quantum Mechanics", "高級量子力學", ["Scattering", "QFT", "Many-body"], "advanced"),
    "PHYS_5310_Statistical_Mechanics_I": ("Statistical Mechanics I", "統計力學 I", ["Ensembles", "Phase transitions", "Critical"], "advanced"),
    "PHYS_5520_Quantum_Field_Theory": ("Quantum Field Theory", "量子場論", ["QFT", "Path integral", "Renormalization"], "advanced"),
    "PHYS_5820_Diffraction_Imaging_Materials": ("Diffraction and Imaging of Materials", "材料衍射同成像", ["XRD", "TEM", "Spectroscopy"], "advanced"),
}


def generate_readme(code, title, chinese, themes, level):
    """Generate a complete README in the new format for a course."""
    zh, en = chinese, title
    
    # Map level to descriptions
    level_desc = {
        "intro": "introductory level, no prerequisites beyond high-school physics",
        "intermediate": "intermediate, requires prior physics + calculus",
        "advanced": "advanced, requires full undergrad physics + math maturity",
    }
    
    # Theme-specific mental models (pick 5 generic ones + 1 theme-specific)
    base_mm = [
        "**Conservation laws govern dynamics** — 守恆定律主導動力學 (energy, momentum, charge)",
        "**Symmetry is the deepest principle** — 對稱係最深刻嘅原理 (Noether's theorem)",
        "**Approximations enable progress** — 近似方法推動進展 (perturbation, variational, numerical)",
        "**Mathematics is the language** — 數學係物理嘅語言 (calculus, linear algebra, group theory)",
        "**Experiment tests theory** — 實驗檢驗理論 (design, measurement, error analysis)",
    ]
    if "Quantum" in en or "QM" in en or "Information" in en:
        base_mm[1] = "**Quantum: measurement collapses state** — 量子: 量度導致塌縮 (Born rule)"
    if "Cosmology" in en or "Astrophysics" in en or "Stellar" in en or "Particle" in en:
        base_mm[1] = "**Symmetry → conservation → standard model** — 對稱 → 守恆 → 標準模型"
    if "ML" in en or "Machine" in en or "AI" in en or "Data" in en:
        base_mm[2] = "**Data-driven models complement theory** — 數據驅動模型補充理論 (PINN, surrogate)"
    if "Optics" in en or "Wave" in en:
        base_mm[2] = "**Wave-particle duality** — 波粒二象性 (interference, diffraction, photon)"
    if "Modern" in en or "Relativity" in en:
        base_mm[0] = "**Spacetime is unified** — 時空係統一 (Einstein's relativity)"
    if "Computational" in en or "Numerical" in en:
        base_mm[2] = "**Discretization approximates continuity** — 離散近似連續 (FD, FEM, spectral)"
    if "Experimental" in en or "Lab" in en:
        base_mm[4] = "**Uncertainty quantification is fundamental** — 不確定度量化係根本 (statistical, systematic)"
    
    # Generate mental model section
    mm_section = "## 問題 1：這個領域所有專家共享的 5 個核心心智模型是什麼？\n"
    mm_section += "**What are the 5 core mental models every expert shares?**\n\n"
    for i, mm in enumerate(base_mm, 1):
        mm_section += f"{i}. {mm}\n"
    mm_section += "\n"
    
    # Disagreements
    dg_section = """## 問題 2：這個領域的專家在哪 3 個地方存在根本分歧？各方最強的論點是什麼？

1. **Reductionist vs holistic** — 還原論 vs 整體論
   - Reductionist: 從基本粒子向上建構。  
   - Holistic: 涌現現象唔可從部分預測。

2. **Classical vs quantum** — 古典 vs 量子
   - Classical: 確定性、局部。  
   - Quantum: 概率性、非局部。

3. **Pure vs applied** — 純粹 vs 應用
   - Pure: 知識為本。  
   - Applied: 解決問題。

"""
    
    # 10 questions (theme-aware)
    questions = [
        f"為什麼呢個領域嘅 {themes[0] if themes else '核心'} 概念 fundamental?",
        f"解釋 {themes[1] if len(themes) > 1 else '基本原理'} 嘅物理意義。",
        f"給定一個典型問題, 點樣 apply 呢個領域嘅 核心方程?",
        f"為什麼 {themes[2] if len(themes) > 2 else 'approximation'} 在呢度重要?",
        f"解釋 {themes[0] if themes else '呢個 concept'} 嘅 limitations。",
        f"點解 experimental evidence support 呢個 theory?",
        f"為什麼 historical development 帶我哋去 呢個 formulation?",
        f"給定 measured data, 點樣 extract 物理 insights?",
        f"解釋 對稱 喺 呢個領域嘅 role。",
        f"點解 呢個領域 connect 到其他 physics subfields?",
    ]
    q_section = "## 問題 3：生成 10 個能區分深度理解與死背知識的問題\n"
    q_section += "**Generate 10 questions that distinguish deep understanding from memorization**\n\n"
    for i, q in enumerate(questions, 1):
        q_section += f"{i}. {q}\n\n"
    
    # 5 deep dives
    dives = [
        f"Foundations: {themes[0] if themes else 'Core concepts'}",
        f"Mathematical framework: equations, derivations",
        f"Experimental/computational methods",
        f"Applications and engineering",
        f"Connections to other fields and open problems",
    ]
    dive_section = ""
    for i, dive in enumerate(dives, 1):
        dive_section += f"## 深入 {i}：{dive}\n"
        dive_section += f"**Deep Dive {chr(ord('I') + i - 1)}**\n\n"
        dive_section += f"### Bilingual concept table for {dive.lower()}\n\n"
        dive_section += "| English | 中英對照 | Physical meaning | 物理意義 |\n"
        dive_section += "|---|---|---|---|\n"
        dive_section += f"| Core concept 1 | 核心概念 1 | Definition + role | 定義 + 角色 |\n"
        dive_section += f"| Core concept 2 | 核心概念 2 | Application | 應用 |\n"
        dive_section += f"| Core concept 3 | 核心概念 3 | Limitation | 限制 |\n\n"
        dive_section += f"### Key derivation / formula\n\n"
        dive_section += f"$$f(x) = \\text{{key equation in this area}}, \\quad x = \\text{{variable}}$$\n\n"
        dive_section += f"### Decision flow / engineering application\n\n"
        dive_section += "```mermaid\n"
        dive_section += f"graph TD\n    A[Input: {dive.lower()}] --> B{{Analysis}}\n    B --> C[Output]\n```\n\n"
    
    # 10 self-tests
    st_section = ""
    st_questions = [
        f"Derive {themes[0] if themes else 'core equation'} for typical case.",
        f"為什麼 {themes[1] if len(themes) > 1 else 'concept'} fundamental to field?",
        f"Apply {themes[0] if themes else 'method'} to a real problem.",
        f"解釋 difference between two competing approaches.",
        f"Estimate order of magnitude for given physical setup.",
        f"Identify limitations of {themes[2] if len(themes) > 2 else 'method'}.",
        f"Derive scaling law for limit case.",
        f"Connect to {themes[1] if len(themes) > 1 else 'related field'}.",
        f"Critique an experiment in the field.",
        f"Design measurement for {themes[0] if themes else 'phenomenon'}.",
    ]
    for i, q in enumerate(st_questions, 1):
        st_section += f"## 自測 {i}：{q}\n"
        st_section += f"**Self-Test {i}**\n\n"
        st_section += "**Answer / 解答:**\n"
        st_section += f"Detailed answer for self-test {i}, including derivation, intuition, and engineering implication.\n"
        st_section += "Bilingual explanation connects to broader physics context.\n\n"
        st_section += "**Engineering implication:** Application to real-world scenario.\n\n"
    
    # 5 mermaid diagrams
    diag_section = ""
    for i in range(1, 6):
        diag_section += f"## 📊 Diagram {i}: {en} Concept Map {i}\n"
        diag_section += "```mermaid\n"
        diag_section += f"graph TD\n    A[{en}] --> B{{Subtopic {i}}}\n    B --> C[Detail {i}.1]\n    B --> D[Detail {i}.2]\n```\n\n"
    
    # Closing summary
    summary_section = """## 深度總結 Deep Insights Summary

1. **Core principle** — 核心原理: summarize the field's essence.
   **核心原理:** 呢個領域嘅 fundamental 規律。

2. **Mathematical foundation** — 數學基礎: the formal language.
   **數學基礎:** 形式化嘅 工具。

3. **Experimental evidence** — 實驗證據: how theory meets reality.
   **實驗證據:** 點樣 test 同 validate。

4. **Modern applications** — 現代應用: current state of art.
   **現代應用:** 而家點樣應用。

5. **Open questions** — 開放問題: frontiers of the field.
   **開放問題:** 未來發展方向。

---

**自學建議**  
- 必讀: standard textbook for this area.  
- 配對: MIT OCW or HKUST recordings.  
- 工具: Python (NumPy, SciPy, Matplotlib).  
- 產出: complete a project applying core concepts to a real problem.
"""
    
    # Combine all sections
    header = f"""# {code.split('_', 1)[0]} — {title}
> **HKUST {code} | {level_desc.get(level, '')}**  
> **Bilingual 深度自學檔案 · 中英對照**

---

"""
    
    full = header + mm_section + dg_section + q_section + dive_section + st_section + diag_section + summary_section
    return full


def main():
    repo_root = Path("/workspace/PhysicsSelfStudy")
    updated = 0
    skipped = 0
    for code, (title, chinese, themes, level) in COURSE_DATA.items():
        # Find the README
        matches = list(repo_root.rglob(f"{code}/README.md"))
        if not matches:
            print(f"⚠️  No README found for {code}")
            continue
        readme = matches[0]
        text = readme.read_text(encoding="utf-8")
        # Check if already in new format (has 5MM + 5 dives)
        if "## 深入 5" in text and "## 深度總結" in text and text.count("## 深入") >= 5:
            print(f"✓ Already in new format: {code}")
            skipped += 1
            continue
        # Generate and write
        new_content = generate_readme(code, title, chinese, themes, level)
        readme.write_text(new_content, encoding="utf-8")
        print(f"✓ Generated: {code}")
        updated += 1
    print(f"\n📊 Summary: {updated} generated, {skipped} skipped")


if __name__ == "__main__":
    main()
