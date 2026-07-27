import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Setup Page
st.set_page_config(page_title="Financial Dashboard: Asian Paints", layout="wide")
st.title("Financial Dashboard: Asian Paints")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("Asian_Paints_clean.csv")

df = load_data()

# KPI Cards
st.subheader("Key Performance Indicators")
c1, c2, c3 = st.columns(3)
c1.metric("Sales", f"₹{df['Sales'].iloc[-1]:,.0f}")
c2.metric("Net Profit", f"₹{df['Net_Profit'].iloc[-1]:,.0f}")
c3.metric("OPM Percent", f"{df['OPM_Percent'].iloc[-1]:.1f}%")

# Visualizations
st.write("---")
st.subheader("Financial Visualizations")
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(df['Period'], df['Sales'], marker='o', label='Sales')
    ax1.plot(df['Period'], df['Net_Profit'], marker='s', label='Net Profit')
    ax1.set_xticks(range(0, len(df['Period']), max(1, len(df['Period'])//5)))
    ax1.set_title("Sales & Net Profit Trend")
    ax1.legend()
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.barplot(x='Period', y='OPM_Percent', data=df, ax=ax2, color='skyblue')
    ax2.set_xticks(range(0, len(df['Period']), max(1, len(df['Period'])//5)))
    ax2.set_title("Operating Profit Margin (OPM %)")
    st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.boxplot(x='Profit_Trend', y='Net_Profit', data=df[df['Profit_Trend'] != 'N/A'], ax=ax3)
ax3.set_title("Net Profit by Profit Trend")
st.pyplot(fig3)

# Predictive Modeling Table
st.write("---")
st.subheader("Predictive Modeling (Profit Trend Prediction)")

df_model = df.dropna(subset=['Sales_Growth']).copy()
X = df_model[['Sales_Growth', 'OPM_Percent', 'Interest', 'Other_Income']]
y = df_model['Profit_Trend']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
log_reg = LogisticRegression().fit(X_train, y_train)
dt = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)

# Compare
results = pd.DataFrame({
    "Model": ["Logistic Regression", "Decision Tree (Default)"],
    "Accuracy": [
        f"{accuracy_score(y_test, log_reg.predict(X_test))*100:.2f}%",
        f"{accuracy_score(y_test, dt.predict(X_test))*100:.2f}%"
    ]
})

st.table(results)