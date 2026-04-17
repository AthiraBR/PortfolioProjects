# System Architecture

## Flow

```
auth_logs.csv
     │
     ▼
[log_generator.py]  →  Generates synthetic events (normal + malicious)
     │
     ▼
[detection_rules.py]  →  Applies rule signatures; returns alert list
     │
     ▼
[risk_engine.py]  →  Aggregates alerts per user; computes weighted risk score
     │
     ▼
[alert_engine.py]  →  Orchestrates above; deduplicates; saves alerts.csv
     │
     ▼
[user_behavior_risk.py] → Builds user behavior profiles (UEBA) and assigns risk scores (0–100)
     │
     ▼
[app.py]  →  Streamlit dashboard consuming alerts.csv + auth_logs.csv
```

---

### 🧩 Component Descriptions

| Module | Responsibility |
|-------|--------------|
| `src/log_generator.py` | Generates synthetic authentication logs with realistic attack scenarios |
| `src/detection_rules.py` | Detects anomalies like brute force, impossible travel, and abnormal access |
| `src/risk_engine.py` | Computes event-level risk scores based on severity |
| `src/alert_engine.py` | Orchestrates detection pipeline, aggregates and deduplicates alerts |
| `src/user_behavior_risk.py` | Builds UEBA-style user profiles and calculates behavioral risk scores |
| `app.py` | Streamlit dashboard for SOC-style monitoring and investigation |

---

### 🧠 Architecture Insight

- Moves from **event-based detection → user-centric risk analysis**
- Combines **rule-based detection + behavior analytics**
- Simulates **UEBA systems used in real SOC environments**


