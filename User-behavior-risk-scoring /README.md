# 👤 User Behavior Risk Scoring System (UEBA-lite)

A cybersecurity project focused on analyzing user authentication behavior to detect abnormal patterns and assign dynamic risk scores — simulating **User and Entity Behavior Analytics (UEBA)** used in modern SOC environments.

---

## 🚀 Overview

This project models how security teams identify risky users by analyzing login behavior over time.

Instead of only detecting individual anomalies, the system:
- Aggregates behavior patterns
- Evaluates user risk holistically
- Prioritizes high-risk identities

---

## 🔍 Key Features

### 👤 User Behavior Profiling
- Tracks login frequency, failure rate, and activity patterns per user
- Identifies abnormal usage trends

### ⚠️ Risk Scoring Engine
- Assigns each user a **0–100 risk score**
- Based on:
  - Failed login ratio
  - Off-hours activity
  - Geographic anomalies
  - Alert severity

### 🌍 Geo-Based Behavior Analysis
- Detects unusual login locations
- Highlights suspicious countries

### 🔴 Impossible Travel Detection
- Identifies rapid location changes across countries
- Visualizes attack paths on a global map

### 📊 SOC-Style Dashboard
- User risk prioritization
- Threat timeline visualization
- Investigation-ready insights

---

## 🧠 Tech Stack

- Python  
- Pandas / NumPy  
- Streamlit  
- Plotly  
- Rule-based behavior analytics  

---

## 📂 Project Structure

```bash
user-behavior-risk-scoring/ 
│
├── app.py # Dashboard (Streamlit) 
├── data/ 
│ ├── auth_logs.csv 
│ ├── alerts.csv 
│ └── user_risk_profiles.csv 
│ 
├── src/ 
│ ├── log_generator.py 
│ ├── detection_rules.py 
│ ├── risk_engine.py 
│ ├── alert_engine.py 
│ └── user_behavior_risk.py 
│ 
├── requirements.txt 
└── README.md
```

## ▶️ How It Works
```bash
Authentication Logs
        ↓ 
Detection Rules (Anomalies)
        ↓ 
Risk Engine (Event-Level) 
        ↓ 
User Behavior Analysis
        ↓ 
User Risk Score (0–100)
        ↓ 
SOC Dashboard Visualization
```

## ▶️ How to Run
```bash
python src/log_generator.py 
python src/alert_engine.py 
streamlit run app.py
```

## Dashboard Capabilities
- 👤 Top risky users
- 🔥 Threat prioritization
- ⏱ Login activity timeline
- 🌍 Geo visualization of behavior
- 🔴 Attack path mapping (impossible travel)
- 🧾 Investigation queue

## Use Case

Simulates how SOC teams:

- Detect compromised accounts
- Identify insider threats
- Prioritize users for investigation
- Monitor identity-based attacks
