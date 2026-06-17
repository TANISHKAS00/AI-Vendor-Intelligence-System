# 🚀 AI-Powered Vendor Intelligence System

## 📌 Overview

The **AI-Powered Vendor Intelligence System** is a data analytics and machine learning solution designed to analyze vendor invoice data and identify potential procurement risks. The system helps organizations detect suspicious transactions, monitor vendor performance, identify duplicate invoices, and generate actionable business insights through an interactive web dashboard.

This project combines **Data Analytics, Machine Learning, and Business Intelligence** to support smarter procurement and vendor management decisions.

---

## 🎯 Project Objectives

* Detect suspicious and potentially fraudulent invoices
* Evaluate vendor risk based on transaction behavior
* Rank vendors based on performance metrics
* Identify duplicate invoice records
* Analyze spending patterns and trends
* Forecast future procurement spending
* Provide insights through an interactive dashboard

---

## ✨ Key Features

### ⚠️ Vendor Risk Scoring

Calculates vendor risk based on spending patterns, freight costs, payment delays, and procurement behavior.

### 🏆 Vendor Performance Ranking

Ranks vendors based on procurement metrics and operational performance.

### 📄 Duplicate Invoice Detection

Identifies duplicate invoice records to reduce payment errors and financial leakage.

### 📈 Spend Trend Analysis & Forecasting

Uses **Linear Regression** to analyze historical spending trends and forecast future expenditure.

### 🌐 Interactive Dashboard

Provides a user-friendly Streamlit interface for data exploration and real-time predictions.

### 📊 Automated Reporting

Generates vendor intelligence reports for business decision-making.

---

## 🛠️ Technologies Used

| Category             | Tools         |
| -------------------- | ------------- |
| Programming Language | Python        |
| Data Analysis        | Pandas, NumPy |
| Machine Learning     | Scikit-Learn  |
| Data Visualization   | Matplotlib    |
| Web Application      | Streamlit     |
| Version Control      | Git & GitHub  |

---

## 📂 Dataset Information

The project uses vendor invoice and procurement data containing:

* Vendor Information
* Invoice Details
* Purchase Order Information
* Payment Records
* Freight Costs
* Transaction Amounts
* Procurement Metrics

---

## 🔄 Project Workflow

### Step 1: Data Collection

Vendor invoice and procurement data are collected from operational records.

### Step 2: Data Cleaning & Preprocessing

* Missing value handling
* Data formatting
* Feature preparation

### Step 3: Feature Engineering

Created business-relevant features such as:

* Payment Delay
* Cost Per Unit
* PO Processing Time
* Freight Analysis Metrics

### Step 4: Fraud Detection

Isolation Forest identifies suspicious invoice transactions.

### Step 5: Vendor Risk Analysis

Risk scores are generated based on vendor behavior and financial indicators.

### Step 6: Vendor Performance Evaluation

Vendor performance metrics are calculated and ranked.

### Step 7: Spend Forecasting

Linear Regression predicts future procurement spending trends.

### Step 8: Duplicate Invoice Detection

Potential duplicate invoices are identified.

### Step 9: Dashboard Development

Results are visualized through an interactive Streamlit application.

### Step 10: Deployment

The application is deployed for online access.

---

## 📁 Repository Structure

```text
AI-Vendor-Intelligence-System/
│
├── invoice_intelligence.ipynb
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── vendor_invoice.csv
│
├── Vendor_Intelligence_Output.csv
├── Vendor_Risk_Report.csv
└── Vendor_Performance_Report.csv
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into the project directory:

```bash
cd AI-Vendor-Intelligence-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Results

The system successfully:

✅ Detects anomalous invoices

✅ Identifies duplicate records

✅ Evaluates vendor risk levels

✅ Ranks vendor performance

✅ Forecasts future spending trends

✅ Generates business insights

✅ Provides an interactive decision-support dashboard

---

## 🌍 Live Demo

**Application:**
[https://ai-vendor-intelligence-system-atdtwx7mnzcqzmd8uqlh8r.streamlit.app/]

---

## 💻 GitHub Repository

**Source Code:**
[https://github.com/TANISHKAS00/AI-Vendor-Intelligence-System]

---

## 🚀 Future Enhancements

* Real-time invoice upload functionality
* Database integration (MySQL/PostgreSQL)
* Automated email alerts for suspicious transactions
* Advanced anomaly detection using Deep Learning

---

## 👩‍💻 Author

**Tanishka Sharma**

Data Analytics & Machine Learning Enthusiast

GitHub: [https://github.com/TANISHKAS00]

LinkedIn: [https://www.linkedin.com/in/tanishka-sharma-1198a7355/]

---

## 📜 License

This project is developed for educational and portfolio purposes.
