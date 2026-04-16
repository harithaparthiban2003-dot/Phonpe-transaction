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

# 🔹 Dataset Path
path = "C:/Users/ELCOT/Desktop/PhonePe_Project/data/pulse-master/data/map/user/hover/country/india/state/"

data = []

# 🔹 Loop through folders
for state in os.listdir(path):
    state_path = path + state + "/"

    for year in os.listdir(state_path):
        year_path = state_path + year + "/"

        for file in os.listdir(year_path):
            if file.endswith(".json"):

                with open(year_path + file, "r") as f:
                    content = json.load(f)

                    if content.get("data") and content["data"].get("hoverData"):

                        for district, details in content["data"]["hoverData"].items():
                            users = details.get("registeredUsers", 0)
                            app_opens = details.get("appOpens", 0)

                            data.append([
                                state,
                                int(year),
                                int(file.replace(".json", "")),
                                district,
                                users,
                                app_opens
                            ])

# 🔹 Convert to DataFrame
df = pd.DataFrame(data, columns=[
    "state", "year", "quarter",
    "district", "registered_users", "app_opens"
])

# 🔹 Insert into MySQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO map_user
        (state, year, quarter, district, registered_users, app_opens)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

cursor.close()
conn.close()

print("✅ Map user data loaded successfully!")
