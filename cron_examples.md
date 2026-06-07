# PhysicsSelfStudy — OpenClaw Cron Examples

> **Ready-to-use cron rules for OpenClaw automation**

---

## 🔄 4 Core Cron Rules

### Rule 1: Saturday Theory Block (09:00-13:00 HKT)

```json
{
  "name": "Physics_Saturday_Theory_Block",
  "trigger": {
    "type": "cron",
    "expression": "0 9 * * 6",
    "timezone": "Asia/Hong_Kong"
  },
  "duration_minutes": 240,
  "heartbeat_minutes": 90,
  "prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Saturday Theory Block（09:00-13:00 HKT，4 小時）。\n\n任務：\n1. 讀取 progress_log.md 了解目前進度。\n2. 根據目前 Phase（Phase 1 BSc / 2 MSc Data / 3 MSc Physics / 4 PhD Prep），決定今天主題。\n3. 給用戶 4 小時學習計劃：\n   - MIT OCW 影片 / 教材章節\n   - 5-8 題指定練習題\n   - 寫筆記到 01_BSc_Physics/ 對應 course 資料夾\n4. 每 90 分鐘 heartbeat：提醒專注 + 記錄 insight。\n5. 結束前要求用戶更新 progress_log.md。\n6. 用繁中 + 英文雙語。",
  "heartbeat_message": "保持專注。記錄今天學到的 insight。不要滑手機。",
  "enabled": true
}
```

---

### Rule 2: Sunday Computational Sprint (14:00-18:00 HKT)

```json
{
  "name": "Physics_Sunday_Computational_Sprint",
  "trigger": {
    "type": "cron",
    "expression": "0 14 * * 0",
    "timezone": "Asia/Hong_Kong"
  },
  "duration_minutes": 240,
  "heartbeat_minutes": 90,
  "prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Sunday Computational Sprint（14:00-18:00 HKT，4 小時）。\n\n任務：\n1. 讀取 progress_log.md 確認上週進度。\n2. 安排今天 coding project：\n   - Phase 1: vector calc / ODE solver / Schrödinger solver\n   - Phase 2: PINN / GP regression\n   - Phase 3: MD simulation / DFT calc\n   - Phase 4: literature review / research proposal draft\n3. 指定具體任務：\n   - 目標 folder (e.g., 01_BSc_Physics/simulations/)\n   - 完成什麼 simulation / notebook\n   - Commit 到 portfolio_projects/ 的哪個子資料夾\n4. 每 90 分鐘 heartbeat：提醒進度 + stretch。\n5. 結束做 10 分鐘 Anki review + self-quiz。\n6. 用中英雙語。",
  "heartbeat_message": "進度如何？記得 stretch。保持 coding flow。",
  "enabled": true
}
```

---

### Rule 3: Sunday Weekly Review (19:00 HKT)

```json
{
  "name": "Physics_Sunday_Weekly_Review",
  "trigger": {
    "type": "cron",
    "expression": "0 19 * * 0",
    "timezone": "Asia/Hong_Kong"
  },
  "duration_minutes": 30,
  "prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Sunday Weekly Review & Planning（19:00 HKT）。\n\n任務：\n1. 讀取這週 progress_log.md 總結。\n2. 問用戶這週：\n   - 學了什麼？\n   - 最大 blocker？\n   - 學到什麼 insight？\n3. 整理本週完成項目。\n4. 檢查 Anki retention < 80% 就安排補強。\n5. 更新下週 cron 細節（指定下週六要讀哪個 course）。\n6. 寫 weekly_reflections/Week_<N>.md。\n7. 生成「下週學習計劃」。\n8. 用中英雙語，語氣鼓勵但嚴格。",
  "enabled": true
}
```

---

### Rule 4: Monthly Milestone Review (1st Sunday 20:00 HKT)

```json
{
  "name": "Physics_Monthly_Milestone_Review",
  "trigger": {
    "type": "cron",
    "expression": "0 20 1-7 * 0",
    "timezone": "Asia/Hong_Kong"
  },
  "duration_minutes": 60,
  "prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Monthly Milestone Review。\n\n任務：\n1. 讀取過去一個月 progress_log.md 做總結。\n2. 評估用戶是否跟上 Phase 進度。\n3. 進行一次綜合 self-quiz（8-10 題混合）。\n4. 檢查 portfolio_projects/ 項目品質。\n5. 問用戶：\n   - 動機、blocker？\n   - 要唔要調整路線圖？\n6. 更新下個月的學習重點。\n7. 給用戶清晰的「下個月執行計劃」。\n8. 用中英雙語。",
  "enabled": true
}
```

---

## ⏰ Schedule Summary

| Day | Time | Block | Hours |
|-----|------|-------|-------|
| Saturday | 09:00-13:00 | Theory Block | 4h |
| Sunday | 14:00-18:00 | Computational Sprint | 4h |
| Sunday | 19:00-19:30 | Weekly Review | 0.5h |
| 1st Sunday/month | 20:00-21:00 | Monthly Review | 1h |

**Total:** ~8.5h/weekend (with +1h in milestone month)

---

## 🔧 OpenClaw Setup Steps

### 1. Create Skill
- OpenClaw UI → Create Skill: `PhysicsSelfStudy`
- Set memory_path: `/path/to/PhysicsSelfStudy/`
- Set progress_log path: `/path/to/PhysicsSelfStudy/progress_log.md`

### 2. Import Cron Rules
- Paste the 4 JSON rules above into OpenClaw
- Set timezone: `Asia/Hong_Kong`
- Enable heartbeat for Rule 1 and 2 (90 min interval)

### 3. Configure Progress Tracking
- Daily updates → `progress_log.md`
- Weekly reflections → `weekly_reflections/Week_<N>.md`
- Monthly milestones → update `ROADMAP.md`

---

*Last updated: 2026-06-07*
