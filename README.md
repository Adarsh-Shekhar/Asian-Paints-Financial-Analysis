# Asian Paints Financial Dashboard & Predictive Analytics

A Python and Streamlit web application for analyzing, visualizing, and predicting the financial performance of **Asian Paints**. 

The application presents key financial metrics, trend visualizations, and a machine learning model comparison to predict profit direction based on performance indicators.

---

## Features

- **Key Performance Indicators (KPIs):** Instant summary of the latest Sales, Net Profit, and Operating Profit Margin (OPM %).
- **Financial Visualizations:**
  - Historical Sales vs. Net Profit trend analysis line chart.
  - Operating Profit Margin (OPM %) progression over time bar chart.
  - Distribution of Net Profit across different profit trend classifications box plot.
- **Predictive Machine Learning:**
  - Trains and compares **Logistic Regression** and **Decision Tree** classifiers.
  - Predicts the `Profit_Trend` ("Profit Grew" vs. "Profit Declined") using features such as `Sales_Growth`, `OPM_Percent`, `Interest`, and `Other_Income`.
  - Displays real-time test accuracy for both models within the dashboard.

---

## Tech Stack

- **Python 3.x**
- **Dashboard & UI:** [Streamlit](https://streamlit.io/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **Data Visualization:** [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/)

---

## Project Structure

```text
├── Asian_Paints_clean.csv  # Processed historical financial dataset
├── app.py                  # Main Streamlit dashboard application script
├── Untitled0.ipynb         # Data exploration and prototyping notebook
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation
```

---

## Installation & Running Locally

### 1. Clone or Download the Repository
Ensure all files are placed within the same directory.

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Dashboard
Run the Streamlit app:
```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## Dataset Schema (`Asian_Paints_clean.csv`)

The dataset includes financial records across multiple periods with the following features:

| Column Header | Description |
|---|---|
| `Period` | Reporting financial period (e.g., Mar-2015, Mar-2016) |
| `Sales` | Total revenue generated (in ₹ Crores) |
| `Operating_Profit` | Operating profit earned before tax and interest |
| `OPM_Percent` | Operating Profit Margin percentage |
| `Other_Income` | Non-operating income sources |
| `Interest` | Total interest expenses |
| `Depreciation` | Depreciation charges |
| `Profit_Before_Tax` | Profit before income tax deductions |
| `Net_Profit` | Net income after all tax deductions |
| `EPS` | Earnings Per Share |
| `Sales_Growth` | Year-over-year sales growth rate |
| `Net_Profit_Growth` | Year-over-year net profit growth rate |
| `Profit_Trend` | Classification target (`Profit Grew` / `Profit Declined`) |

---

## Machine Learning Model Summary

The dashboard uses standard financial indicators as feature inputs:
- `Sales_Growth`
- `OPM_Percent`
- `Interest`
- `Other_Income`

Two models are trained on an 80/20 train-test split:
1. **Logistic Regression:** Serves as a linear baseline classification model.
2. **Decision Tree Classifier:** Captures non-linear decision thresholds for profit trend classification.

Model accuracy metrics are evaluated on the test dataset and reported dynamically in the application table.
