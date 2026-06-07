# PhysicsSelfStudy — Setup Automation Prompt (Final Canonical Version)

> **Canonical, reusable automation prompt for setting up a Physics Self-Study project from scratch**
> **Status: Already applied to https://github.com/yip-lgtm/PhysicsSelfStudy ✅**
> **HKUST course catalog aligned: 2026-06-07**

---

## 🎯 Final Prompt (Yip's Refined Version)

```text
You are the PhysicsSelfStudy Project Manager, also a high-automation project
initialization expert.

The user wants to automatically set up a Physics Self-Study Project's Git
Repository, with a complete initial file structure.

Use terminal commands to complete the following tasks as automatically as
possible. Minimize user prompts. Only pause for the GitHub Repo URL at the end.

Tasks:
1. Auto-create the full folder structure (4 phases):
   - 01_BSc_Physics (core_courses, math_support, simulations, notes, electives, minors)
   - 02_MSc_DataDriven_Modeling (core_courses, electives, projects, notes)
   - 03_MSc_Physics (scientific_computing_concentration, advanced_materials_concentration, electives, projects, notes)
   - 04_MPhil_PhD_Prep (Physics_PhD, Nano_Science_Technology_PhD, qualifying_exam_practice, mock_research_proposals, literature_reviews)
   - resources/curricula
   - portfolio_projects (simulations, notebooks, visualizations, open_source_physics, mit_ocw, community)
   - Anki_decks
   - weekly_reflections

2. Auto-create these root files with appropriate content:
   - .gitignore (Python, Jupyter, Obsidian, macOS, Windows, VS Code)
   - STRUCTURE.md (professional folder structure documentation)
   - README.md (project goals, structure, learning mode)
   - progress_log.md (initial template + today's Launch Entry)
   - cron_examples.md (4 core cron rules with full content)
   - openclaw_skill.json (4 OpenClaw rules)
   - ROADMAP.md (24-month BSc → MSc → PhD roadmap)
   - SETUP.md (OpenClaw + Python env)
   - LICENSE (MIT)

3. Auto-create README.md in these important course folders:
   - 01_BSc_Physics/core_courses/PHYS_2124_Math_Methods_I/README.md
   - 01_BSc_Physics/core_courses/PHYS_3032_Classical_Mechanics/README.md
   - 01_BSc_Physics/core_courses/PHYS_3142_Computational_Methods/README.md
   - 01_BSc_Physics/core_courses/PHYS_4811_ML_in_Physics/README.md
   - 02_MSc_DataDriven_Modeling/core_courses/MSDM_5004_Numerical_Methods/README.md
   - 02_MSc_DataDriven_Modeling/electives/MSDM_5055_Deep_Learning/README.md
   - 04_MPhil_PhD_Prep/README.md

4. Initialize Git:
   - git init
   - git add .
   - git commit -m "feat: initialize Physics Self-Study Project with full structure and initial files"

5. After completion, tell the user:
   - What has been auto-created
   - Next steps: create GitHub repo and push
   - Follow-up recommendations: commit habits, OpenClaw skill usage

Execute with high automation. Only pause for GitHub Repo URL input.
Use Traditional Chinese for responses. Keep technical commands in English.
```

---

## ✅ Already Applied to PhysicsSelfStudy Repo

| Step | Status | Evidence |
|------|--------|----------|
| Folder structure (4 phases + minors) | ✅ | 50+ sub-folders created |
| `.gitignore` | ✅ | Python/Jupyter/Obsidian ignores |
| `STRUCTURE.md` | ✅ | 4407 bytes |
| `README.md` | ✅ | 6886 bytes (4-phase overview) |
| `progress_log.md` | ✅ | Initial template (2026-06-07) |
| `cron_examples.md` | ✅ | 4 rules with prompts |
| `openclaw_skill.json` | ✅ | 4 OpenClaw rules |
| `ROADMAP.md` | ✅ | 24-month BSc → MSc plan |
| `SETUP.md` | ✅ | OpenClaw + Python env |
| `LICENSE` | ✅ | MIT |
| **All 7 listed course READMEs** | ✅ | All created |
| + 17 additional course READMEs | ✅ | HKUST catalog aligned |
| `04_MPhil_PhD_Prep/README.md` | ✅ | Top-level README |
| `git init` | ✅ | |
| `git add .` + `git commit` | ✅ | 6 commits |
| GitHub Repo created | ✅ | https://github.com/yip-lgtm/PhysicsSelfStudy |
| `git push -u origin` | ✅ | All files + folders pushed |

**Final commit:** `643650b` (2026-06-07 09:51 UTC)

---

## 🎯 HKUST Course Catalog Alignment (Bonus)

Beyond the basic 7 courses listed in the prompt, the repo now has:

### BSc Core (10 courses)
- PHYS 2124, 3031, 3032, 3033, 3036, 3038, 3142, 4050, 4051, 4811

### BSc Electives (10 courses)
- PHYS 3037, 3042, 3053, 3071, 4055, 4058, 4071, 4191, 4291, 4812

### Math Support (2 courses)
- MATH 2351, 2352

### Minors (2 programs)
- Minor in Physics (9 cr)
- Minor in Astrophysics & Cosmology (9 cr)

**Total course folders: 24** (compared to original 7)

---

## 🔁 How to Reuse This Template

To apply this prompt to a new repo (e.g., `HKUST-Physics-PhD-Prep`):

### Option A: Manual Setup
```bash
git clone https://github.com/<user>/<repo>.git
cd <repo>

# Use the prompt above in OpenClaw/Claude
# Or run the included SETUP_AUTOMATION_PROMPT.md
```

### Option B: Direct Copy from PhysicsSelfStudy
```bash
# Clone this repo as template
git clone https://github.com/yip-lgtm/PhysicsSelfStudy.git new-project
cd new-project
rm -rf .git
git init
git remote add origin <new-repo-url>
# Edit README.md, progress_log.md to reflect new project
git add .
git commit -m "feat: initialize from PhysicsSelfStudy template"
git push -u origin main
```

### Option C: Use GitHub Template
1. Go to https://github.com/yip-lgtm/PhysicsSelfStudy/settings
2. Enable "Template repository"
3. Use the "Use this template" button on new repos

---

## 📊 Repo Statistics (Final)

| Item | Count |
|------|-------|
| Top-level files | 9 |
| Phase folders | 4 |
| Minor programs | 2 |
| Total sub-folders | 50+ |
| Course READMEs | 24 |
| Total commits | 6 |
| Repo size | ~95 KB |
| Last updated | 2026-06-07 09:51 UTC |

---

*Last updated: 2026-06-07 — Final canonical version*
