# PhysicsSelfStudy — Repository Structure

> **Detailed folder structure for the 4-phase Physics Self-Study Project**

---

## 🎯 4 Phases Overview

| # | Phase | Duration | Target |
|---|-------|----------|--------|
| 1 | BSc Physics Foundation | Year 1-2 (24 months) | BSc equivalent |
| 2 | MSc Data-Driven Modeling | Year 2-3 (12 months) | MSc equivalent |
| 3 | MSc Physics @ HKUST | Year 3-4 (12 months) | MSc Physics |
| 4 | MPhil/PhD Prep | Year 4+ (ongoing) | PhD application |

---

## 📂 Top-Level Folders

### `01_BSc_Physics/`
**Purpose:** Phase 1 — BSc Physics Foundation
**Subfolders:**
- `core_courses/` — Main BSc courses (PHYS 2124, 2125, 2126, 2127, etc.)
- `math_support/` — Math prerequisites, problem sets
- `simulations/` — BSc-level physics simulations
- `notes/` — General notes, summaries

### `02_MSc_DataDriven_Modeling/`
**Purpose:** Phase 2 — MSc in Data-Driven Modeling
**Subfolders:**
- `core_courses/` — Core ML/stats courses
- `electives/` — Elective courses
- `projects/` — Course projects
- `notes/` — General notes

### `03_MSc_Physics/`
**Purpose:** Phase 3 — MSc Physics @ HKUST
**Subfolders:**
- `scientific_computing_concentration/` — Computational physics focus
- `advanced_materials_concentration/` — Materials science focus
- `electives/`
- `projects/`
- `notes/`

### `04_MPhil_PhD_Prep/`
**Purpose:** Phase 4 — MPhil/PhD Preparation (HKUST)
**Subfolders:**
- `Physics_PhD/` — HKUST Physics PhD application materials
- `Nano_Science_Technology_PhD/` — HKUST Nano Sci & Tech PhD
- `qualifying_exam_practice/` — QE prep
- `mock_research_proposals/` — Practice research proposals
- `literature_reviews/` — Key papers by topic
- **Top-level:** `04_MPhil_PhD_Prep/README.md` — Phase overview + 4-year timeline

### `portfolio_projects/`
**Purpose:** Showcase projects for CV/portfolio
**Subfolders:**
- `simulations/` — Physics simulations
- `notebooks/` — Jupyter notebooks
- `visualizations/` — Charts, plots
- `open_source_physics/` — Community contributions
- `mit_ocw/` — MIT OCW solutions
- `community/` — Community projects

### `resources/`
**Purpose:** Curated learning resources
**Subfolders:**
- `curricula/` — HKUST and other uni curricula
- `MIT_OCW_links.md` — MIT OCW links
- `textbooks.md` — Recommended textbooks
- `python_env_setup.md` — Python environment

### `Anki_decks/`
**Purpose:** Spaced repetition decks for each course

### `weekly_reflections/`
**Purpose:** Weekly reflection notes (Sat night / Sun evening)

---

## 📄 Top-Level Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, quick start |
| `STRUCTURE.md` | This file — detailed folder structure |
| `progress_log.md` | Daily/weekly progress tracker |
| `cron_examples.md` | OpenClaw cron examples |
| `openclaw_skill.json` | OpenClaw Skill definition |
| `SETUP.md` | OpenClaw + Python env setup |
| `ROADMAP.md` | 24+ month BSc → MSc → PhD roadmap |
| `LICENSE` | MIT License |
| `.gitignore` | Ignore Python/Jupyter/Obsidian |

---

## 🗂️ Naming Conventions

### Course Folders
- Format: `PHYS_<code>_<Name>` (e.g., `PHYS_2124_Math_Methods_I`)
- Use underscore `_` for spaces
- Use Roman numerals for parts (I, II, III)

### Project Folders
- Format: `<month>_<topic>` (e.g., `06_Quantum_Tunneling`)
- Or: `<week>_<project>` (e.g., `Week01_Vector_Calculator`)

### Notes
- Format: `<course>_<topic>_notes.md`
- Or: `<date>_<topic>.md`

### Commits
- Format: `Week X: <topic>`
- Examples:
  - `Week 1: Vector Calculus Toolkit`
  - `Week 2: ODE Solvers (Euler, RK4)`
  - `Week 3: Cross product visualization`

---

## 🛠️ How to Use This Repo

### Day-to-Day
1. **Saturday Theory Block** → write notes to `01_BSc_Physics/core_courses/<course>/notes.md`
2. **Sunday Computational Sprint** → write code to `01_BSc_Physics/simulations/` or `portfolio_projects/notebooks/`
3. **Sunday Review** → write reflection to `weekly_reflections/Week_<N>.md`
4. **End of day** → update `progress_log.md`
5. **End of week** → commit + push

### Monthly
- First Sunday: Monthly Milestone Review → update `ROADMAP.md` if needed

### Per Course
- Course README in each course folder
- Problems in `/problems/` subfolder
- Notes in `/notes.md`
- Simulations in `01_BSc_Physics/simulations/`

---

## 🎯 Open Source Workflow

When contributing:
1. **Fork** repo
2. **Create branch** for your improvement
3. **Make changes** in your forked repo
4. **Submit PR** with clear description
5. **Tag** relevant Phase (1, 2, 3, 4) in PR

---

*Last updated: 2026-06-07*
