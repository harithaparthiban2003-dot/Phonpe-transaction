<<<<<<< HEAD
# Phonpe-transaction
Data Extraction, SQL Proficiency, Data Visualization, Analytical Thinking, Documentation, Streamlit
=======
\# 📊 PhonePe Transaction Insights Dashboard



\## 📌 Project Overview



This project is a data analytics dashboard built using Python, MySQL, and Streamlit to analyze and visualize PhonePe transaction data.

It provides interactive insights into transaction trends across different states, categories, and time periods in India.



\---



\## 🎯 Objectives



&#x20;Analyze large-scale transaction data

&#x20;Visualize insights using interactive dashboards

&#x20;Understand regional and categorical transaction patterns

&#x20;Build a real-time data-driven application



\---



\## 🛠️ Tech Stack



&#x20;Programming Language Python

&#x20;Database MySQL

&#x20;Visualization Matplotlib, Plotly

&#x20;Framework Streamlit

&#x20;Libraries Pandas, MySQL Connector



\---



\## 📂 Project Structure



```

PhonePe\_Project

│

├── data                      # Dataset files (JSONCSV)

├── scripts                   # Data loading scripts

│   ├── load\_aggregated\_transaction.py

│   ├── load\_aggregated\_user.py

│   └── load\_aggregated\_insurance.py

│

├── app.py                     # Main Streamlit dashboard

├── logo.png                   # PhonePe logo

└── README.md                  # Project documentation

```



\---



\## 🗄️ Database Schema



The project uses multiple tables to store structured data



\### 🔹 Aggregated Tables



&#x20;aggregated\_transaction

&#x20;aggregated\_user

&#x20;aggregated\_insurance



\### 🔹 Map Tables



&#x20;map\_user

&#x20;map\_transaction

&#x20;map\_insurance



\### 🔹 Top Tables



&#x20;top\_user

&#x20;top\_transaction

&#x20;top\_insurance



\---



\## ⚙️ Features



&#x20;🗺️ India Map Visualization (State-wise transaction analysis)

&#x20;📊 Bar Charts (Top performing states)

&#x20;🥧 Pie Charts (Transaction type distribution)

&#x20;💰 KPI Metrics (Total transaction amount)

&#x20;🎛️ Interactive Filters (Year \& Quarter selection)

&#x20;💜 PhonePe Styled UI



\---



\## 🚀 How to Run the Project



\### 1️⃣ Clone or Download



```

git clone your-repo-link

cd PhonePe\_Project

```



\### 2️⃣ Install Dependencies



```

pip install pandas streamlit matplotlib plotly mysql-connector-python

```



\### 3️⃣ Setup MySQL Database



&#x20;Create database



```sql

CREATE DATABASE phonepe\_db;

```



&#x20;Import data using Python scripts



\### 4️⃣ Run the Application



```

python -m streamlit run app.py

```



\---



\## 📈 Key Insights



&#x20;Identifies top-performing states based on transaction volume

&#x20;Shows distribution of transaction types

&#x20;Highlights regional transaction trends

&#x20;Enables time-based analysis using filters



\---



\## ⚡ Challenges Faced



&#x20;Handling missingnull values in JSON data

&#x20;Fixing state name mismatches for map visualization

&#x20;Optimizing SQL queries for performance

&#x20;UI alignment and responsive design in Streamlit



\---



\## 🔮 Future Enhancements



&#x20;Add district-level drill-down analysis

&#x20;Implement real-time data updates

&#x20;Enhance UI with animations and advanced styling

&#x20;Deploy dashboard on cloud (Streamlit Cloud  AWS)



\---



>>>>>>> 176ce3e (Initial commit - PhonePe Dashboard Project)
