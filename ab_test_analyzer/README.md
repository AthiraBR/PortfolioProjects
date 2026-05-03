# 📈 A/B Test Results Analyser

This project is a complete end-to-end data science web application built with **Streamlit** to analyze A/B testing data. It evaluates whether a feature change (e.g., a new landing page) had a statistically significant impact on user conversion rates.

## Features

- **Automated Data Loading & Cleaning**: Dynamically fetches the Udacity A/B test dataset and cleans mismatched records or duplicate users.
- **Conversion Rate Analysis**: Computes conversion metrics for both Control and Treatment groups.
- **Data Visualization**: Presents an easy-to-read, beautifully styled bar chart comparing conversion rates.
- **Statistical Significance Testing**:
  - Implements a **Two-Proportion Z-test**.
  - Includes an interactive slider to let users select the desired **Significance Level (Alpha)**.
  - Dynamically calculates the Z-Statistic and P-Value to conclude whether the results are statistically significant or not.

## Tech Stack

- **Python 3**
- **Streamlit**: For the interactive web dashboard.
- **Pandas & NumPy**: For data manipulation and metric calculations.
- **SciPy & Statsmodels**: For statistical testing.
- **Matplotlib & Seaborn**: For data visualization.

## Dataset

This app uses a widely known public A/B testing dataset originally from the Udacity Data Analyst Nanodegree. It contains over 290,000 rows of user interaction data with columns such as `user_id`, `group` (control vs treatment), `landing_page` (old_page vs new_page), and `converted` (0 or 1).

## How to Run Locally

### Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

### Setup

1. **Clone the repository and navigate to the project directory:**
   ```bash
   cd ab_test_analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. **View the Dashboard:**
   Open your browser and navigate to `http://localhost:8501`.
   <img width="792" height="875" alt="image" src="https://github.com/user-attachments/assets/93cfe957-d215-49be-b510-2ac65d530708" />
   <img width="792" height="459" alt="image" src="https://github.com/user-attachments/assets/7506ce1f-4e9d-4801-919d-3e4e6fce1ae2" />



## Interpretation of Results

The application helps answer the core question of A/B testing: *Did the change move the needle?*
By comparing the calculated P-Value against the chosen Alpha level, the dashboard will clearly state whether you should **reject the null hypothesis** (the change had an effect) or **fail to reject the null hypothesis** (the change did not have a statistically significant effect).
