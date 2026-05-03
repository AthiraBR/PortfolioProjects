import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="A/B Test Results Analyser", layout="wide", page_icon="📈")

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .reportview-container .main .block-container{
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .metric-card {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border-top: 4px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Function to load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/aaubs/data_science_master/main/data/ab_data.csv"
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        # Fallback URL if first one fails
        url2 = "https://raw.githubusercontent.com/beery4010/Analyze-AB-Test-Results/master/ab_data.csv"
        df = pd.read_csv(url2)
        return df

def clean_data(df):
    # Remove records where group and landing page don't align
    # Control should see old_page, treatment should see new_page
    mismatch = ((df['group'] == 'treatment') == (df['landing_page'] == 'new_page')) == False
    df_clean = df[~mismatch].copy()
    
    # Check for duplicate users
    df_clean.drop_duplicates(subset='user_id', inplace=True)
    return df_clean

st.title("📈 A/B Test Results Analyser")
st.markdown("Analyze A/B test data to determine if a feature change had a statistically significant impact on conversion rates.")

with st.spinner("Loading and preparing data..."):
    try:
        raw_df = load_data()
        df = clean_data(raw_df)
        st.success(f"Data loaded successfully! Analyzed **{len(df):,}** unique users.")
    except Exception as e:
        st.error(f"Failed to load data. Error: {e}")
        st.stop()

st.header("1. Data Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", f"{len(df):,}")
col2.metric("Control Group Size", f"{len(df[df['group'] == 'control']):,}")
col3.metric("Treatment Group Size", f"{len(df[df['group'] == 'treatment']):,}")

with st.expander("Show Raw Data Sample"):
    st.dataframe(df.head())

st.header("2. Conversion Rates")
# Calculate conversion rates
conversion_summary = df.groupby('group')['converted'].agg(['count', 'sum', 'mean']).reset_index()
conversion_summary.columns = ['Group', 'Total Users', 'Conversions', 'Conversion Rate']
conversion_summary['Conversion Rate (%)'] = conversion_summary['Conversion Rate'] * 100

st.dataframe(
    conversion_summary.style.format({
        'Total Users': '{:,}',
        'Conversions': '{:,}',
        'Conversion Rate': '{:.4f}',
        'Conversion Rate (%)': '{:.2f}%'
    }),
    use_container_width=True
)

# Plot conversion rates
st.subheader("Conversion Rate Visualization")
fig, ax = plt.subplots(figsize=(10, 5))
# Use modern styling
plt.style.use('dark_background')
sns.set_theme(style="darkgrid")
fig.patch.set_facecolor('#0e1117')
ax.set_facecolor('#0e1117')

bars = sns.barplot(
    x='Group', 
    y='Conversion Rate', 
    data=conversion_summary, 
    palette=['#ff4b4b', '#00b4d8'], 
    ax=ax,
    hue='Group',
    legend=False
)

for index, row in conversion_summary.iterrows():
    ax.text(index, row['Conversion Rate'] / 2, f"{row['Conversion Rate (%)']:.2f}%", 
            color='white', ha="center", fontweight='bold', fontsize=12)

ax.set_title("Conversion Rate by Group", fontsize=16, color='white', pad=20)
ax.set_ylabel("Conversion Rate", color='white')
ax.set_xlabel("Group", color='white')
ax.set_ylim(0, max(conversion_summary['Conversion Rate']) * 1.2)
ax.tick_params(colors='white')

st.pyplot(fig)

st.header("3. Statistical Significance Test")
st.markdown("We use a **Two-Proportion Z-test** to determine if the difference in conversion rates is statistically significant.")

col_a, col_b = st.columns([1, 2])
with col_a:
    alpha = st.slider("Select Significance Level (Alpha)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)

# Perform Z-test
control_conversions = conversion_summary[conversion_summary['Group'] == 'control']['Conversions'].values[0]
treatment_conversions = conversion_summary[conversion_summary['Group'] == 'treatment']['Conversions'].values[0]
control_total = conversion_summary[conversion_summary['Group'] == 'control']['Total Users'].values[0]
treatment_total = conversion_summary[conversion_summary['Group'] == 'treatment']['Total Users'].values[0]

count = np.array([treatment_conversions, control_conversions])
nobs = np.array([treatment_total, control_total])

stat, pval = proportions_ztest(count, nobs, alternative='two-sided')

st.subheader("Test Results")
col1, col2 = st.columns(2)
col1.metric("Z-Statistic", f"{stat:.4f}")
col2.metric("P-Value", f"{pval:.4f}")

if pval < alpha:
    st.success(f"### 🎉 Statistically Significant!\nThe p-value (**{pval:.4f}**) is less than alpha (**{alpha}**). We reject the null hypothesis.\n\n**Conclusion:** The feature change *did* move the needle.")
else:
    st.warning(f"### 🛑 Not Statistically Significant.\nThe p-value (**{pval:.4f}**) is greater than alpha (**{alpha}**). We fail to reject the null hypothesis.\n\n**Conclusion:** The feature change *did not* have a significant impact.")
