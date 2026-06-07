# PhysicsSelfStudy — Setup Automation Prompt (Reusable Template)

> **Reusable automation prompt for setting up a Physics Self-Study project from scratch**
> **Status: Already applied to https://github.com/yip-lgtm/PhysicsSelfStudy ✅**

---

## 📋 Original Prompt (Yip's Spec)

You are the PhysicsSelfStudy Project Manager, also an automation expert.

The user wants to quickly and automatically set up a Physics Self-Study Project's Git Repository, applying a professional folder structure.

Please use terminal commands to complete the following tasks as automatically as possible, only asking the user when necessary:

### Tasks

1. **Confirm current working directory**
2. **Auto-create full folder structure** (use `mkdir -p`):

```
physics-selfstudy/
├── 01_BSc_Physics/
│   ├── core_courses/
│   ├── math_support/
│   ├── simulations/
│   └── notes/
├── 02_MSc_DataDriven_Modeling/
│   ├── core_courses/
│   ├── electives/
│   ├── projects/
│   └── notes/
├── 03_MSc_Physics/
│   ├── scientific_computing_concentration/
│   ├── advanced_materials_concentration/
│   ├── electives/
│   ├── projects/
│   └── notes/
├── 04_MPhil_PhD_Prep/
│   ├── Physics_PhD/
│   ├── Nano_Science_Technology_PhD/
│   ├── qualifying_exam_practice/
│   ├── mock_research_proposals/
│   └── literature_reviews/
├── resources/
│   └── curricula/
├── portfolio_projects/
├── Anki_decks/
├── weekly_reflections/
├── progress_log.md
├── cron_examples.md
├── STRUCTURE.md
└── README.md
```

3. **Auto-create these root files:**
   - `.gitignore` (Python, Jupyter, Obsidian, macOS, Windows, VS Code)
   - `STRUCTURE.md` (professional structure documentation)
   - `README.md` (project goals, structure, learning mode)
   - `progress_log.md` (initial template with today's date)
   - `cron_examples.md` (4 cron rules)

4. **Initialize Git Repo:**
   - `git init`
   - `git add .`
   - `git commit -m "feat: initialize Physics Self-Study Project with full folder structure and automation files"`

5. **Next steps for user:**
   - Create new GitHub Repo (suggested: `physics-selfstudy` or `HKUST-Physics-PhD-Prep`)
   - Connect and push:
     ```bash
     git remote add origin <GitHub URL>
     git branch -M main
     git push -u origin main
     ```

6. **Provide follow-up recommendations:**
   - Weekly commit naming convention
   - How to organize existing files
   - How to use with OpenClaw PhysicsSelfStudy skill

**Execute as automatically as possible. Only pause for GitHub URL input.**

---

## ✅ Already Applied to PhysicsSelfStudy Repo

| Step | Status | Evidence |
|------|--------|----------|
| Folder structure (4 phases) | ✅ | 41 folders created |
| `.gitignore` | ✅ | Python/Jupyter/Obsidian ignores |
| `STRUCTURE.md` | ✅ | 4407 bytes |
| `README.md` | ✅ | 6886 bytes (4-phase overview) |
| `progress_log.md` | ✅ | Initial template (2026-06-07) |
| `cron_examples.md` | ✅ | 4 rules with prompts |
| `git init` | ✅ | |
| `git add .` + `git commit` | ✅ | 3 commits |
| GitHub Repo created | ✅ | https://github.com/yip-lgtm/PhysicsSelfStudy |
| `git push -u origin` | ✅ | All 24 files + 41 folders pushed |

**Final commit:** `8890651` (2026-06-07 00:49 UTC)

---

## 🔁 How to Reuse This Template

To apply this template to a new repo (e.g., `HKUST-Physics-PhD-Prep`):

### 1. Create GitHub Repo
- Go to https://github.com/new
- Name: `HKUST-Physics-PhD-Prep` (or other)
- Public, with issues/projects/wiki
- Do NOT initialize with README

### 2. Run Setup Script
```bash
# Clone empty repo
git clone https://github.com/<user>/<repo>.git
cd <repo>

# Run folder structure creation
mkdir -p 01_BSc_Physics/{core_courses,math_support,simulations,notes}
mkdir -p 02_MSc_DataDriven_Modeling/{core_courses,electives,projects,notes}
mkdir -p 03_MSc_Physics/{scientific_computing_concentration,advanced_materials_concentration,electives,projects,notes}
mkdir -p 04_MPhil_PhD_Prep/{Physics_PhD,Nano_Science_Technology_PhD,qualifying_exam_practice,mock_research_proposals,literature_reviews}
mkdir -p resources/curricula
mkdir -p portfolio_projects/{simulations,notebooks,visualizations,open_source_physics,mit_ocw,community}
mkdir -p Anki_decks weekly_reflections

# Copy templates from PhysicsSelfStudy
cp /path/to/PhysicsSelfStudy_repo/{.gitignore,README.md,STRUCTURE.md,progress_log.md,cron_examples.md,openclaw_skill.json,ROADMAP.md,SETUP.md,LICENSE} .

# Commit and push
git add .
git commit -m "feat: initialize Physics Self-Study Project with full folder structure and automation files"
git push -u origin main
```

### 3. Customize
- Update README.md with new project name
- Update progress_log.md
- Adjust ROADMAP.md for new goals

---

*Last updated: 2026-06-07 00:49 UTC*
