# PhysicsSelfStudy — OpenClaw Cron + Environment Setup

> **Setup instructions for OpenClaw automation + Python environment**

---

## 🔄 4 + 1 Cron Rules (JSON — OpenClaw Import Ready)

### Cron 1: Saturday Theory Block

```json
{
  "name": "PhysicsTheoryBlock_Sat",
  "schedule": "0 9 * * 6",
  "timezone": "Asia/Hong_Kong",
  "enabled": true,
  "skill_prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Saturday Theory Block（09:00-13:00 HKT）。\n\n任務：\n1. 讀取 progress_log.md 了解目前進度與上週 blocker。\n2. 根據目前 Phase（目前是 Phase 1 BSc），決定今天的主題。\n3. 給用戶清晰的 3–4 小時學習計劃。\n4. 每 90 分鐘給一次 heartbeat nudge。\n5. 結束前要求用戶更新 progress_log.md。\n6. 用繁體中文 + 英文雙語回應。",
  "heartbeat_interval_minutes": 90
}
```

### Cron 2: Sunday Computational Sprint

```json
{
  "name": "PhysicsComputationalSprint_Sun",
  "schedule": "0 14 * * 0",
  "timezone": "Asia/Hong_Kong",
  "enabled": true,
  "skill_prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Sunday Computational Sprint（14:00-18:00 HKT）。\n\n任務：\n1. 讀取 progress_log.md 確認上週理論學習進度。\n2. 安排今天 coding project。\n3. 指定具體任務（folder, simulation, commit）。\n4. 要求用戶邊做邊記錄 insight。\n5. 每 90 分鐘給一次 heartbeat。\n6. 結束時做 10 分鐘 Anki review。\n7. 用中英雙語。",
  "heartbeat_interval_minutes": 90
}
```

### Cron 3: Sunday Weekly Review

```json
{
  "name": "PhysicsWeeklyReview_Sun",
  "schedule": "0 19 * * 0",
  "timezone": "Asia/Hong_Kong",
  "enabled": true,
  "skill_prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Sunday Weekly Review & Planning（19:00 HKT）。\n\n任務：\n1. 讀取這週的 progress_log.md 總結。\n2. 問用戶這週學習了什麼、blocker、insight。\n3. 整理本週完成項目，建議下週優先順序。\n4. 檢查 Anki retention。\n5. 更新下週的 cron 細節。\n6. 最後生成「下週學習計劃」。\n7. 用中英雙語，語氣鼓勵但嚴格。"
}
```

### Cron 4: Monthly Milestone Review

```json
{
  "name": "PhysicsMonthlyReview",
  "schedule": "0 20 1-7 * 0",
  "timezone": "Asia/Hong_Kong",
  "enabled": true,
  "skill_prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Monthly Milestone Review。\n\n任務：\n1. 讀取過去一個月的 progress_log.md 做總結。\n2. 評估用戶是否跟上 Phase 1 進度。\n3. 進行一次綜合 self-quiz（8-10 題）。\n4. 檢查 portfolio_projects/ 裡的項目品質。\n5. 問用戶目前 motivation、blocker。\n6. 更新下個月的學習重點。\n7. 給用戶清晰的「下個月執行計劃」。\n8. 用中英雙語。"
}
```

### Cron 5: Daily Anki Review (10 分鐘) — 可選

```json
{
  "name": "PhysicsDailyAnkiReview",
  "schedule": "0 22 * * 1-5",
  "timezone": "Asia/Hong_Kong",
  "enabled": true,
  "skill_prompt": "你是 PhysicsSelfStudy Project Manager。\n\n現在是 Daily Anki Review（22:00 HKT，10 分鐘）。\n\n任務：\n1. 提醒用戶打開 Anki deck。\n2. 完成 10 分鐘 review。\n3. 記錄 retention rate 到 progress_log.md。\n4. 如果 retention < 80%，提醒下週要補強。\n5. 簡短回應即可。\n6. 用中英雙語。"
}
```

---

## 🚀 OpenClaw 設定步驟

### 1. 建立 Skill
- 打開 OpenClaw UI
- 建立新 Skill：名稱 = `PhysicsSelfStudy`
- 設定 memory path = `/path/to/PhysicsSelfStudy/`
- 設定 progress_log path = `/path/to/PhysicsSelfStudy/progress_log.md`

### 2. 加入 4+1 條 Cron Rules
- 把上面 5 個 JSON 逐個 import
- 設定 timezone = `Asia/Hong_Kong`

### 3. 準備 Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install numpy scipy sympy matplotlib pandas
pip install jupyter ipykernel plotly
pip install qutip
```

---

## 📅 下週六第一次 Theory Block

**日期：** 2026-06-13 (Sat)
**時間：** 09:00-13:00 HKT
**主題：** Vector Calculus
**資源：** MIT OCW 18.02 Lecture 1-3
**目標：** 完成 5-8 題 vector calculus 問題
