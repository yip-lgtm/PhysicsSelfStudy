# PhysicsSelfStudy — Open Source Physics Project

[![Status](https://img.shields.io/badge/Status-Phase%201%20%28BSc%29-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)
[![Open Source](https://img.shields.io/badge/Open%20Source-Welcome-brightgreen)](#)
[![Programme](https://img.shields.io/badge/Pathway-BSc%20→%20MSc%20→%20PhD-orange)](#)

> **BSc Physics → MSc Data-Driven Modeling / MSc Physics → MPhil/PhD**
> **HKUST-aligned | Weekend-only | Open Source**

---

## 🎯 Project Overview

A structured, open-source, self-study project covering **24 months of BSc foundation + 24 months of MSc/PhD preparation**:

- **Phase 1 (Year 1-2):** BSc Physics Foundation — Math Methods, Classical Mechanics, E&M, QM, Statistical Mechanics
- **Phase 2 (Year 2-3):** MSc Data-Driven Modeling — ML for Physics, CFD, Quantum Computing, Statistical Inference
- **Phase 3 (Year 3-4):** MSc Physics (HKUST) — Scientific Computing or Advanced Materials concentration
- **Phase 4 (Year 4+):** MPhil/PhD Prep — HKUST Physics PhD or Nano Science Technology PhD

**Current Phase:** Phase 1 — BSc Foundation
**Current Course:** PHYS 2124 Mathematical Methods I
**Started:** 2026-06-07
**Mode:** Weekend-only (Sat Theory + Sun Coding + Sun Review)
**Pathway:** HKUST-aligned (Physics PhD / Nano Sci & Tech PhD)

---

## 📂 Repository Structure (4 Phases)

```
PhysicsSelfStudy/
├── README.md                            ← You are here
├── STRUCTURE.md                         ← Detailed folder structure
├── progress_log.md                      ← Daily/weekly progress tracker
├── cron_examples.md                     ← OpenClaw cron examples
├── .gitignore                           ← Python/Jupyter/Obsidian ignores
│
├── 01_BSc_Physics/                      ← Phase 1: BSc Foundation (Year 1-2)
│   ├── core_courses/                    ← Main BSc courses
│   │   ├── PHYS_2124_Math_Methods_I/
│   │   ├── PHYS_2125_Classical_Mechanics/
│   │   ├── PHYS_2126_Electromagnetism/
│   │   └── PHYS_2127_Quantum_Mechanics_I/
│   ├── math_support/                    ← Math prerequisites
│   ├── simulations/                     ← BSc-level physics simulations
│   └── notes/                           ← General notes
│
├── 02_MSc_DataDriven_Modeling/          ← Phase 2: MSc Data-Driven (Year 2-3)
│   ├── core_courses/                    ← Core ML/stats courses
│   ├── electives/                       ← Elective courses
│   ├── projects/                        ← Course projects
│   └── notes/
│
├── 03_MSc_Physics/                      ← Phase 3: MSc Physics (HKUST) (Year 3-4)
│   ├── scientific_computing_concentration/  ← Comp. physics focus
│   ├── advanced_materials_concentration/    ← Materials focus
│   ├── electives/
│   ├── projects/
│   └── notes/
│
├── 04_MPhil_PhD_Prep/                   ← Phase 4: PhD Prep (Year 4+)
│   ├── Physics_PhD/                     ← HKUST Physics PhD application
│   ├── Nano_Science_Technology_PhD/     ← HKUST Nano Sci & Tech PhD
│   ├── qualifying_exam_practice/        ← QE prep materials
│   ├── mock_research_proposals/         ← Practice proposals
│   └── literature_reviews/              ← Key papers by topic
│
├── 05_Undergraduate_Minors/             ← HKUST Minor Programs
│   ├── README.md                        ← Minors overview
│   ├── Minor_in_Physics/                ← 9-credit Physics minor
│   └── Minor_in_Astrophysics_Cosmology/ ← 9-credit Astro/Cosmo minor
│
├── portfolio_projects/                  ← Showcase projects
│   ├── simulations/
│   ├── notebooks/
│   ├── visualizations/
│   ├── open_source_physics/             ← Community contributions
│   ├── mit_ocw/                         ← MIT OCW solutions
│   └── community/                       ← Community projects
│
├── resources/                           ← Curated resources
│   ├── MIT_OCW_links.md
│   ├── textbooks.md
│   ├── python_env_setup.md
│   └── curricula/                       ← HKUST/other uni curricula
│
├── Anki_decks/                          ← Spaced repetition decks
└── weekly_reflections/                  ← Weekly reflection notes
```

See `STRUCTURE.md` for full details.

---

## 🗓️ Weekly Schedule (OpenClaw Cron)

| Day | Time (HKT) | Block | Duration |
|-----|-----------|-------|----------|
| Saturday | 09:00-13:00 | **Theory Block** | 4h |
| Sunday | 14:00-18:00 | **Computational Sprint** | 4h |
| Sunday | 19:00 | **Weekly Review** | 30min |
| 1st Sunday/month | 20:00 | **Monthly Milestone Review** | 1h |

**Total commitment:** ~8.5 hours/weekend

See `openclaw_skill.json` and `cron_examples.md` for full automation.

---

## 🎓 4-Phase Curriculum

### Phase 1: BSc Foundation (Year 1-2) — HKUST Codes
| Course | Focus | Resources |
|--------|-------|-----------|
| PHYS 2124 Math Methods I | Vector calc, ODE, Linear alg, Complex | MIT OCW 18.02 + 18.03 + Boas |
| PHYS 3032 Classical Mechanics | Lagrangian, Hamiltonian | MIT OCW 8.01 + Taylor |
| PHYS 3142 Computational Methods | Numerical, Monte Carlo, MD | MIT OCW 18.335 + Newman |
| PHYS 4811 ML in Physics | PINN, Neural Operators | Coursera + Bishop + Raissi |
| PHYS 2060 Electromagnetism | Maxwell eq, EM waves | MIT OCW 8.07 + Griffiths |
| PHYS 3050 Quantum Mechanics I | Schrödinger, Hydrogen | MIT OCW 8.04 + Griffiths |
| Statistical Mechanics | Ensembles, Phase transitions | MIT OCW 8.08 + Pathria |

### Phase 2: MSc Data-Driven Modeling (Year 2-3)
| Topic | Focus |
|-------|-------|
| ML for Physics | PINN, Gaussian processes |
| Computational Fluid Dynamics | Navier-Stokes, turbulence |
| Quantum Computing | Qiskit, VQE |
| Statistical Inference | Bayesian, MCMC |

### Phase 3: MSc Physics @ HKUST (Year 3-4)
**Two concentration tracks:**
- **Scientific Computing:** Numerical methods, HPC, simulations
- **Advanced Materials:** Condensed matter, soft matter, materials design

### Phase 4: MPhil/PhD Prep (Year 4+)
**Two PhD pathways at HKUST:**
- **Physics PhD:** Astrophysics, Condensed Matter, Particle Physics, Quantum Info
- **Nano Science Technology PhD:** Nano materials, quantum devices, biotech

See `ROADMAP.md` for detailed 24+ month plan.

---

## 🌍 Open Source — Welcome to Contribute!

This project is **fully open source** under MIT License. Whether you're a:

- 🎓 **Student** — Learn alongside, share notes, ask questions
- 💼 **Practitioner** — Improve simulations, optimize code, add features
- 🔬 **Researcher** — Cite, extend, collaborate on thesis
- 👨‍💻 **Developer** — Add new features, fix bugs, write tests

### How to Contribute

1. **Fork** this repo
2. **Improve** any course material, simulation, or notebook
3. **Submit** a Pull Request with clear description
4. **Open Issues** for bugs, suggestions, or questions

---

## 📊 Progress Tracking

**Current:** Phase 1 (BSc Foundation) — Month 1, Week 1
**Started:** 2026-06-07
**Target BSc completion:** 2028-06-07
**Target PhD application:** 2030

See `progress_log.md` for detailed daily/weekly progress.

---

## 📜 License

MIT License — See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Saba Yip** | yipsaba@polyu-msc.ai
**Background:** PolyU MSc Digital Economics (2027) | Self-studying Physics & Data-Driven Modeling | HKUST PhD aspirant
**Mission:** Build open, rigorous, and accessible physics education for the global community

---

*Built with persistence in Hong Kong | Open for collaboration* 🇭🇰⚛️
