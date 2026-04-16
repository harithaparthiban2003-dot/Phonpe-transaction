import json
import pandas as pd
import mysql.connector
import os

# 🔹 DB Connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="H@rikrish03",
    database="phonepe_db"
)

cursor = conn.cursor()

# 🔹 Dataset Path (CHECK THIS)
path = "C:/Users/ELCOT/Desktop/PhonePe_Project/data/pulse-master/data/aggregated/user/country/india/state/"

data = []

# 🔹 Loop through folders
for state in os.listdir(path):
    state_path = path + state + "/"

    for year in os.listdir(state_path):
        year_path = state_path + year + "/"

        for file in os.listdir(year_path):
            if file.endswith(".json"):

                file_path = year_path + file

                with open(file_path, "r") as f:
                    content = json.load(f)

                    # 🔹 Safe check for data
                    if content.get("data") and content["data"].get("usersByDevice"):

                        for item in content["data"]["usersByDevice"]:
                            brand = item.get("brand", "")
                            count = item.get("count", 0)
                            percentage = item.get("percentage", 0)

                            data.append([
                                state,
                                int(year),
                                int(file.replace(".json", "")),
                                brand,
                                count,
                                percentage
                            ])

# 🔹 Convert to DataFrame
df = pd.DataFrame(data, columns=[
    "state", "year", "quarter",
    "brand", "user_count", "percentage"
])

# 🔹 Insert into MySQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO aggregated_user
        (state, year, quarter, brand, user_count, percentage)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

cursor.close()
conn.close()

print("✅ Aggregated user data loaded successfully!")
