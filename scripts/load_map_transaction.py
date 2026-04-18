# 4. Map Transaction

python
import pandas as pd
import json
import os

path = "pulse/data/map/transaction/hover/country/india/state/"
state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'Count': [],
    'Amount': []
}

print("Map Transaction script continues similarly...")


---