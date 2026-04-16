import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# -------------------------------
# 🔹 PAGE CONFIG
# -------------------------------
st.set_page_config(layout="wide")

# -------------------------------
# 🔹 LOAD DATA (CSV)
# -------------------------------
df = pd.read_csv("aggregated_transaction.csv")

# -------------------------------
# 🔹 SIDEBAR FILTERS
# -------------------------------
st.sidebar.title("🔎 Filters")

years = sorted(df['year'].unique())
year = st.sidebar.selectbox("Select Year", years)

quarters = sorted(df['quarter'].unique())
quarter = st.sidebar.selectbox("Select Quarter", quarters)

# -------------------------------
# 🔹 FILTER DATA
# -------------------------------
df_filtered = df[
    (df['year'] == year) &
    (df['quarter'] == quarter)
]

# -------------------------------
# 🔹 MAIN LAYOUT
# -------------------------------
col1, col2 = st.columns([3, 1])

# ===============================
# 🗺️ INDIA MAP
# ===============================
with col1:

    st.subheader("🗺️ India Map")

    df_map = df_filtered.groupby('state')['transaction_amount'].sum().reset_index()

    if not df_map.empty:

        df_map['state'] = df_map['state'].str.replace("-", " ").str.title()

        geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/india_states.geojson"

        fig_map = px.choropleth(
            df_map,
            geojson=geojson,
            featureidkey="properties.ST_NM",
            locations="state",
            color="transaction_amount",
            color_continuous_scale="Blues"
        )

        fig_map.update_geos(fitbounds="locations", visible=False)

