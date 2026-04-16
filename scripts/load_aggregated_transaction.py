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
path = "C:/Users/ELCOT/Desktop/PhonePe_Project/data/pulse-master/data/aggregated/transaction/country/india/state/"

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
                    
                    if "data" in content and content["data"] and "transactionData" in content["data"]:
                        
                        for i in content["data"]["transactionData"]:
                            name = i["name"]
                            count = i["paymentInstruments"][0]["count"]
                            amount = i["paymentInstruments"][0]["amount"]
                            
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
    "transaction_type",
    "transaction_count",
    "transaction_amount"
])

# 🔹 Insert into MySQL
for i, row in df.iterrows():
    cursor.execute("""
        INSERT INTO aggregated_transaction
        (state, year, quarter, transaction_type, transaction_count, transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("✅ Aggregated transaction data loaded successfully!")
