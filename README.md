# PhonePe Transaction Insights Dashboard

The Indian digital payment system has transformed the way people make transactions across the country. From major cities to remote villages, digital payments have become faster, safer, and more accessible through mobile phones and internet connectivity.

This project is inspired by the PhonePe Pulse dataset and focuses on analyzing transaction data across India using interactive visualizations. The dashboard helps users understand payment trends, state-wise transaction growth, and transaction categories through maps, charts, and key performance indicators.

Built using Python, Streamlit, and MySQL, this project provides meaningful insights into digital payment patterns and supports data-driven decision making.

---

# Announcements

🌟 Interactive India Map added for state-wise transaction analysis
🌟 Year and Quarter filters available for better data exploration
🌟 Pie chart and Bar chart included for category and top state analysis

---

# Table of Contents

* PhonePe Transaction Insights Dashboard
* Announcements
* Goal
* Technologies Used
* Features
* Project Structure
* Dashboard Sections
* Insights
* Conclusion

---

# Goal

The main goal of this project is to visualize and analyze PhonePe transaction data across India and provide useful business insights using an interactive dashboard.

This helps in understanding:

* Transaction growth by state
* Top performing states
* Transaction type distribution
* Year-wise and quarter-wise analysis
* Overall digital payment trends

---

# Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* Matplotlib
* MySQL

---

# Features

## Aggregated Analysis

Shows the total transaction amount and payment category distribution across India.

## India State-wise Map

Interactive 2D India map displaying state-wise transaction values using blue shades.

## Pie Chart

Shows transaction type distribution for selected year and quarter.

## Bar Chart

Displays top performing states based on total transaction amount.

## Filters

Users can select:

* Year
* Quarter

to dynamically update the dashboard.

---

# Project Structure

PhonePe_Project
│
├── app.py
├── README.md
├── scripts/
│   ├── load_aggregated_transaction.py
│   ├── load_aggregated_user.py
│   ├── load_map_transaction.py
│   └── more loader scripts

---

# Dashboard Sections

## KPI Section

Displays:

* Total Transaction Amount

## Map Visualization

Shows India map with state-wise payment values.

## Pie Chart Section

Displays transaction category contribution.

## Top States Section

Shows top 5 states with highest transaction values.

---

# Insights

* Maharashtra, Karnataka, and Tamil Nadu show higher transaction volumes
* Merchant payments and peer-to-peer transactions dominate usage
* Digital payment adoption has significantly increased across all regions
* State-wise comparison helps identify high-performing regions

---

# Conclusion

This project demonstrates how data visualization can simplify complex financial transaction data and convert it into meaningful business insights.

The PhonePe Transaction Insights Dashboard helps users understand India's growing digital payment ecosystem through simple, interactive, and effective visual analytics.
