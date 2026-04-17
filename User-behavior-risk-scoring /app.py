import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
import numpy as np
import random


# ── Page Config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="IAM Threat Monitor",
    layout="wide",
    page_icon="🛡️"
)

# ── Custom Dark Styling ───────────────────────────────────────────
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #e6edf3;
}
</style>
""", unsafe_allow_html=True)

# ── Paths ─────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALERTS_PATH = os.path.join(BASE_DIR, "data", "alerts.csv")
AUTH_PATH = os.path.join(BASE_DIR, "data", "auth_logs.csv")
USER_RISK_PATH = os.path.join(BASE_DIR, "data", "user_risk_profiles.csv")

SEVERITY_COLORS = {
    "Critical": "#ff4d4d",
    "High": "#ff944d",
    "Medium": "#ffd11a",
    "Low": "#4dff88",
}
# ── Country Coordinates (for Geo Visualization) ───────────────────
country_coords = {
    "US": (37.0902, -95.7129),
    "UK": (55.3781, -3.4360),
    "Germany": (51.1657, 10.4515),
    "India": (20.5937, 78.9629),
    "Russia": (61.5240, 105.3188),
    "China": (35.8617, 104.1954),
    "Brazil": (-14.2350, -51.9253),
    "Canada": (56.1304, -106.3468),
}

# ── Loaders ───────────────────────────────────────────────────────
@st.cache_data
def load_alerts():
    if not os.path.exists(ALERTS_PATH):
        return pd.DataFrame()
    df = pd.read_csv(ALERTS_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

@st.cache_data
def load_auth():
    if not os.path.exists(AUTH_PATH):
        return pd.DataFrame()
    df = pd.read_csv(AUTH_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

@st.cache_data
def load_user_risk():
    if not os.path.exists(USER_RISK_PATH):
        return pd.DataFrame()
    return pd.read_csv(USER_RISK_PATH)

# ── Main App ──────────────────────────────────────────────────────
def main():

    st.title("🛡️ IAM Threat Monitor")
    st.markdown("*SOC-style Identity Threat Detection Dashboard*")
    st.markdown("---")

    alerts_df = load_alerts()
    auth_df = load_auth()
    user_df = load_user_risk()

    # ── Detect Impossible Travel ─────────────────────────────
    travel_df = auth_df.copy()
    travel_df = travel_df.sort_values(["user_id", "timestamp"])

    travel_df["prev_country"] = travel_df.groupby("user_id")["country"].shift(1)
    travel_df["prev_time"] = travel_df.groupby("user_id")["timestamp"].shift(1)

    travel_df["time_diff"] = (travel_df["timestamp"] - travel_df["prev_time"]).dt.total_seconds() / 60

    impossible_travel = travel_df[
        (travel_df["country"] != travel_df["prev_country"]) &
        (travel_df["time_diff"] < 120)
    ].dropna()

    if alerts_df.empty:
        st.warning("Run alert_engine.py first.")
        return

    # ── Build Attack Paths ─────────────────────────────
    lines = []

    for _, row in impossible_travel.iterrows():
        src = row["prev_country"]
        dst = row["country"]

        if src in country_coords and dst in country_coords:
            lat1, lon1 = country_coords[src]
            lat2, lon2 = country_coords[dst]

            offset = random.uniform(-2, 2)

            lines.append({
                "lat": [lat1 + offset, lat2 + offset],
                "lon": [lon1 + offset, lon2 + offset],
                "user": row["user_id"],
                "time_diff": row["time_diff"]
            })

    # ── Sidebar ───────────────────────────────────────────────────
    st.sidebar.header("🔍 Filters")

    severity_options = ["All"] + sorted(alerts_df["severity"].unique())
    selected_severity = st.sidebar.selectbox("Severity", severity_options)

    user_options = ["All"] + sorted(alerts_df["user_id"].unique())
    selected_user = st.sidebar.selectbox("User", user_options)

    filtered = alerts_df.copy()

    if selected_severity != "All":
        filtered = filtered[filtered["severity"] == selected_severity]

    if selected_user != "All":
        filtered = filtered[filtered["user_id"] == selected_user]

    # ── KPI ROW ───────────────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🚨 Total Alerts", len(filtered))
    col2.metric("🔥 Critical", len(filtered[filtered["severity"] == "Critical"]))
    col3.metric("⚠️ High", len(filtered[filtered["severity"] == "High"]))
    col4.metric("👤 Users at Risk", filtered["user_id"].nunique())

    st.markdown("---")

    # ── Priority Threats ───────────────────────────────────────────
    st.subheader("🎯 Priority Threats")

    top_threats = filtered.sort_values("risk_score", ascending=False).head(5)

    st.dataframe(
        top_threats[["user_id", "severity", "rule_name", "risk_score"]],
        use_container_width=True
    )

    st.markdown("---")

    # ── Charts Row 1 ───────────────────────────────────────────────
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Alerts by Severity")

        sev_counts = filtered["severity"].value_counts().reset_index()
        sev_counts.columns = ["Severity", "Count"]

        fig_sev = px.bar(
            sev_counts,
            x="Severity",
            y="Count",
            color="Severity",
            color_discrete_map=SEVERITY_COLORS,
            template="plotly_dark"
        )

        st.plotly_chart(fig_sev, use_container_width=True)

    with c2:
        st.subheader("Top Risky Users (Alerts)")

        top_users = (
            filtered.groupby("user_id")["risk_score"]
            .max()
            .sort_values(ascending=False)
            .head(8)
            .reset_index()
        )

        fig_users = px.bar(
            top_users,
            x="risk_score",
            y="user_id",
            orientation="h",
            color="risk_score",
            color_continuous_scale="Reds",
            template="plotly_dark"
        )

        fig_users.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_users, use_container_width=True)

    # ── Threat Timeline ────────────────────────────────────────────
    st.markdown("### ⏱ Threat Timeline")

    timeline = filtered.copy()

    fig_time = px.scatter(
        timeline,
        x="timestamp",
        y="user_id",
        color="severity",
        size="risk_score",
        color_discrete_map=SEVERITY_COLORS,
        template="plotly_dark"
    )

    st.plotly_chart(fig_time, use_container_width=True)

    # ── Failed Login Trend ─────────────────────────────────────────
    if not auth_df.empty:
        st.subheader("Failed Login Trend")

        fails = auth_df[auth_df["login_status"] == "failure"].copy()
        fails["date"] = fails["timestamp"].dt.date

        daily = fails.groupby("date").size().reset_index(name="Failed Logins")

        fig_trend = px.line(daily, x="date", y="Failed Logins", template="plotly_dark")

        st.plotly_chart(fig_trend, use_container_width=True)

    # ── Geo Login Map ─────────────────────────────────────────

    st.markdown("### 🌍 Attack Path Visualization (Impossible Travel)")

    lines = lines[:15]

    fig = go.Figure()

    for line in lines:

        lat1, lat2 = line["lat"][0], line["lat"][-1]
        lon1, lon2 = line["lon"][0], line["lon"][-1]

        # Create smooth curve
        lats = np.linspace(lat1, lat2, 20)
        lons = np.linspace(lon1, lon2, 20)

        # Color based on speed (shorter time = more dangerous)
        time_diff = line.get("time_diff", 120)

        if time_diff < 60:
            color = "#ff4d4d"   # Critical
        else:
            color = "#ff944d"   # High

        fig.add_trace(go.Scattergeo(
            lon=lons,
            lat=lats,
            mode="lines",
            line=dict(width=2, color=color),
            opacity=0.7,
            showlegend=False,
            hovertext=line["user"],
            hoverinfo="text"
        ))

    fig.update_layout(
        geo=dict(
            bgcolor="black",
            showland=True,
            landcolor="rgb(20,20,20)",
            showcountries=True,
            countrycolor="gray"
        ),
        margin=dict(t=0, b=0),
    )

    st.plotly_chart(fig, use_container_width=True)

    # ── User Risk Section ─────────────────────────────────────────
    st.markdown("---")
    st.subheader("👤 User Risk Intelligence")

    if not user_df.empty:

        c3, c4 = st.columns(2)

        with c3:
            fig_user_risk = px.bar(
                user_df.sort_values("risk_score", ascending=False).head(10),
                x="risk_score",
                y="user_id",
                color="risk_level",
                orientation="h",
                color_discrete_map=SEVERITY_COLORS,
                title="🚨 Top Risky Users",
                template="plotly_dark"
            )
            fig_user_risk.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_user_risk, use_container_width=True)

        with c4:
            risk_dist = user_df["risk_level"].value_counts().reset_index()
            risk_dist.columns = ["Risk Level", "Count"]

            fig_pie = px.pie(
                risk_dist,
                names="Risk Level",
                values="Count",
                color="Risk Level",
                color_discrete_map=SEVERITY_COLORS,
                template="plotly_dark"
            )

            st.plotly_chart(fig_pie, use_container_width=True)

        st.subheader("📋 User Risk Table")
        st.dataframe(user_df, use_container_width=True, hide_index=True)

    else:
        st.info("No user risk data found. Run alert_engine.py first.")

    # ── Investigation Table ────────────────────────────────────────
    st.markdown("---")
    st.subheader("🧾 Investigation Queue")

    st.dataframe(
        filtered.sort_values("risk_score", ascending=False),
        use_container_width=True,
        hide_index=True
    )


# ── Run ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()