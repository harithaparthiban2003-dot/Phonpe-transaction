import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import matplotlib.pyplot as plt

# -------------------------------
# 🔹 PAGE CONFIG
# -------------------------------
st.set_page_config(layout="wide")

# -------------------------------
# 🔹 CUSTOM CSS (PHONEPE STYLE)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #1c0f3c;
    color: white;
}
[data-testid="stAppViewContainer"] {
    background-color: #1c0f3c;
}
h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🔹 HEADER
# -------------------------------
st.markdown("""
<h1 style='text-align: center; color: white;'>
📊 PhonePe Transaction Insights Dashboard
</h1>
""", unsafe_allow_html=True)

# -------------------------------
# 🔹 DB CONNECTION
# -------------------------------
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="H@rikrish03",
    database="phonepe_db"
)

# -------------------------------
# 🔹 SIDEBAR
# -------------------------------
st.sidebar.title("🔎 Filters")

years = pd.read_sql("SELECT DISTINCT year FROM aggregated_transaction", conn)['year'].tolist()
year = st.sidebar.selectbox("Select Year", sorted(years), index=len(years)-1)

quarters = pd.read_sql(
    f"SELECT DISTINCT quarter FROM aggregated_transaction WHERE year={year}", conn
)['quarter'].tolist()

quarter = st.sidebar.selectbox("Select Quarter", sorted(quarters))

# -------------------------------
# 🔹 MAIN LAYOUT
# -------------------------------
col1, col2 = st.columns([3, 1])

# ===============================
# 🗺️ BIG INDIA MAP (CENTER)
# ===============================
with col1:

    st.subheader("🗺️ India Map")

    query_map = f"""
    SELECT state, SUM(transaction_amount) AS total
    FROM aggregated_transaction
    WHERE year = {year} AND quarter = {quarter}
    GROUP BY state
    """

    df_map = pd.read_sql(query_map, conn)

    if not df_map.empty:

        df_map['state'] = df_map['state'].str.replace("-", " ").str.title()

        india_geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/india_states.geojson"

        fig_map = px.choropleth(
            df_map,
            geojson=india_geojson,
            featureidkey="properties.ST_NM",
            locations="state",
            color="total",
            color_continuous_scale="Blues"   # 🔥 BLUE THEME
        )

        # 🔥 REMOVE BACKGROUND COMPLETELY
        fig_map.update_geos(
            fitbounds="locations",
            visible=False
        )

        fig_map.update_layout(
            height=700,   # 🔥 BIG SIZE
            margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor='rgba(0,0,0,0)',  # transparent
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig_map, use_container_width=True)

    else:
        st.warning("No map data available")

# ===============================
# 📊 RIGHT SIDE PANEL
# ===============================
with col2:

    # 🔹 TOTAL KPI
    query_total = f"""
    SELECT SUM(transaction_amount) AS total
    FROM aggregated_transaction
    WHERE year = {year} AND quarter = {quarter}
    """

    total = pd.read_sql(query_total, conn)['total'][0] or 0

    st.metric("💰 Total Transactions", f"₹ {total:,.0f}")

    # 🔹 PIE CHART (WHITE BG)
    st.subheader("🥧 Transaction Types")

    query_pie = f"""
    SELECT transaction_type, SUM(transaction_amount) AS total
    FROM aggregated_transaction
    WHERE year = {year} AND quarter = {quarter}
    GROUP BY transaction_type
    """

    df_pie = pd.read_sql(query_pie, conn)

    if not df_pie.empty:
        fig2, ax2 = plt.subplots()

        # 🔥 WHITE BACKGROUND PIE
        fig2.patch.set_facecolor('white')

        ax2.pie(
            df_pie['total'],
            labels=df_pie['transaction_type'],
            autopct='%1.1f%%'
        )

        st.pyplot(fig2)

    else:
        st.warning("No pie data")

    # 🔹 BAR CHART
    st.subheader("📊 Top States")

    query_bar = f"""
    SELECT state, SUM(transaction_amount) AS total
    FROM aggregated_transaction
    WHERE year = {year} AND quarter = {quarter}
    GROUP BY state
    ORDER BY total DESC
    LIMIT 5
    """

    df_bar = pd.read_sql(query_bar, conn)

    if not df_bar.empty:
        fig1, ax1 = plt.subplots()

        ax1.barh(df_bar['state'], df_bar['total'])
        ax1.set_facecolor('white')  # clean look

        st.pyplot(fig1)

    else:
        st.warning("No bar data")

# -------------------------------
# 🔹 CLOSE CONNECTION
# -------------------------------
conn.close()
