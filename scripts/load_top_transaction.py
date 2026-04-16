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
path = "C:/Users/ELCOT/Desktop/PhonePe_Project/data/pulse-master/data/top/transaction/country/india/state/"

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

                    if content.get("data"):

                        # 🔹 Districts
                        if content["data"].get("districts"):
                            for item in content["data"]["districts"]:
                                name = item.get("entityName", "")
                                count = item.get("metric", {}).get("count", 0)
                                amount = item.get("metric", {}).get("amount", 0)

                                data.append([
                                    state,
                                    int(year),
                                    int(file.replace(".json", "")),
                                    name,
                                    count,
                                    amount
                                ])

                        # 🔹 Pincodes
                        if content["data"].get("pincodes"):
                            for item in content["data"]["pincodes"]:
                                name = item.get("entityName", "")
                                count = item.get("metric", {}).get("count", 0)
                                amount = item.get("metric", {}).get("amount", 0)

                                data.append([
                                    state,
                                    int(year),
                                    int(file.replace(".json", "")),
                                    name,
                                    count,
                                    amount
                                ])

# 🔹 Convert to DataFrame
df = pd.DataFrame(data, columns=[
    "state", "year", "quarter",
    "entity_name", "transaction_count", "transaction_amount"
])

# 🔹 Clean NaN values
df = df.fillna(0)

# 🔹 Insert into MySQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO top_transaction
        (state, year, quarter, entity_name, transaction_count, transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        str(row["state"]),
        int(row["year"]),
        int(row["quarter"]),
        str(row["entity_name"]),
        int(row["transaction_count"]),
        float(row["transaction_amount"])
    ))

conn.commit()

cursor.close()
conn.close()

print("✅ Top transaction data loaded successfully!")
