# Physics Self-Study Project — Repository Structure

This repository is organized by **HKUST target programs** so that notes, simulations, projects, and deliverables are clearly mapped to specific degrees and courses. This makes portfolio building, progress tracking, and eventual application materials much cleaner.

## Top-Level Structure

```
physics-selfstudy/
├── README.md                          # Project overview + how to use this repo
├── STRUCTURE.md                       # This file — explains the folder organization
├── progress_log.md                    # Weekly hours, insights, blockers, wins
├── cron_examples.md                   # OpenClaw cron rules for weekend blocks
├── 01_BSc_Physics/                    # Phase 1: BSc foundation bridge
│   ├── core_courses/                  # Notes + solved problems for required physics courses
│   ├── math_support/                  # Calculus, Linear Algebra, Multivariable Calculus
│   ├── minors/                        # Undergraduate Minor Programs (Physics & Astrophysics)
│   ├── simulations/                   # Python simulations mapped to BSc courses
│   └── notes/                         # Lecture notes, derivations, Anki exports
│
├── 02_MSc_DataDriven_Modeling/        # Phase 2: Joint MSc Data-Driven Modeling
│   ├── core_courses/                  # MSDM 5001–5004 + 6771
│   ├── electives/                     # Time series, Deep Learning, Statistical ML, Optimization, etc.
│   ├── projects/                      # Major reproducible projects (PINNs, stochastic models, etc.)
│   └── notes/
│
├── 03_MSc_Physics/                    # Phase 2: MSc Physics (with concentrations)
│   ├── scientific_computing_concentration/   # MSPY 5230, 5240, 5250 (recommended primary)
│   ├── advanced_materials_concentration/     # MSPY 5001, 5210, 5220 (alternative)
│   ├── electives/                     # Quantum materials, AI in Science, Solid State, etc.
│   ├── projects/
│   └── notes/
│
├── 04_MPhil_PhD_Prep/                 # Phase 3: Research readiness
│   ├── Physics_PhD/                   # Qualifying exam practice, mock proposals for Physics PhD
│   ├── Nano_Science_Technology_PhD/   # Qualifying exam + literature for Nano S&T PhD
│   ├── qualifying_exam_practice/      # Mixed qualifying-style questions + solutions
│   ├── mock_research_proposals/       # 5–10 page mock proposals (computational or nano track)
│   └── literature_reviews/            # Annotated bibliographies + subfield reviews
│
├── resources/
│   ├── curricula/                     # Official HKUST program PDFs / pastes (BSc, MScs, PhDs)
│   └── mapping_files/                 # Alignment documents (BSc, Data-Driven, Physics, Nano PhD)
│
├── portfolio_projects/                # Polished, final-version simulations + short papers (GitHub showcase)
├── Anki_decks/                        # Spaced-repetition decks (formulas, concepts, methods)
├── weekly_reflections/                # End-of-week insight summaries
└── old_archive/                       # (Optional) Move old flat structure here if migrating
```

## How to Use This Structure

- **Phase 1 work** → `01_BSc_Physics/`
- **Phase 2 work** → `02_MSc_DataDriven_Modeling/` **and** `03_MSc_Physics/`
- **Phase 3 work** → `04_MPhil_PhD_Prep/`
- **Undergraduate Minors** → `01_BSc_Physics/minors/`
- Every major simulation or project eventually moves (or is copied) to `portfolio_projects/` with a clean README and short write-up.
- All official curriculum documents and mapping files live in `resources/`.

## Recommended Git Workflow

1. Work inside the relevant program/course folder during the weekend block.
2. When a project/simulation is mature and well-documented, copy or move the final version to `portfolio_projects/`.
3. Commit frequently with clear messages (e.g., "Week 3: Lagrangian mechanics simulation + notes").
4. Keep `progress_log.md` updated every weekend.

This structure makes it obvious to future reviewers (HKUST admissions, mentors, or yourself in 2 years) exactly how your self-study maps to the actual degree requirements.

---
*Maintained by PhysicsSelfStudy Project Manager (OpenClaw) — aligned with HKUST BSc Physics (including Minors), MSc Data-Driven Modeling, MSc Physics, and MPhil/PhD in Physics / Nano Science & Technology.*