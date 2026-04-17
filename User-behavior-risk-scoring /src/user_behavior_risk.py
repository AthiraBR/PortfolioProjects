import pandas as pd

def compute_user_behavior_risk(df, alerts_df):

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour

    user_profiles = []

    for user in df['user_id'].unique():

        user_df = df[df['user_id'] == user]

        total_logins = len(user_df)
        failed_logins = len(user_df[user_df['login_status'] == "failure"])
        fail_ratio = failed_logins / total_logins if total_logins else 0

        off_hours = len(user_df[(user_df['hour'] < 6) | (user_df['hour'] > 22)])
        off_hour_ratio = off_hours / total_logins if total_logins else 0

        unique_locations = user_df['country'].nunique()

        user_alerts = alerts_df[alerts_df['user_id'] == user]
        alert_count = len(user_alerts)

        severity_weights = {
            "Critical": 40,
            "High": 30,
            "Medium": 20
        }

        alert_score = 0
        for _, row in user_alerts.iterrows():
            alert_score += severity_weights.get(row['severity'], 10)

        risk_score = (
            (fail_ratio * 30) +
            (off_hour_ratio * 20) +
            (unique_locations * 5) +
            (alert_score)
        )

        risk_score = min(risk_score, 100)

        if risk_score > 75:
            level = "Critical"
        elif risk_score > 50:
            level = "High"
        elif risk_score > 25:
            level = "Medium"
        else:
            level = "Low"

        user_profiles.append({
            "user_id": user,
            "total_logins": total_logins,
            "failed_logins": failed_logins,
            "fail_ratio": round(fail_ratio, 2),
            "off_hour_ratio": round(off_hour_ratio, 2),
            "unique_locations": unique_locations,
            "alert_count": alert_count,
            "risk_score": round(risk_score, 2),
            "risk_level": level
        })

    return pd.DataFrame(user_profiles)