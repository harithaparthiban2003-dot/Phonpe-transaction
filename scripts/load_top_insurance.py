# 5. Top Insurance

python
import pandas as pd
import json
import os

path = "pulse/data/top/insurance/country/india/state/"
Top_state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Pincode': [],
    'Insurance_count': [],
    'Insurance_amount': []
}

for i in Top_state_list:
    p_i = path + i + "/"
    Top_yr = os.listdir(p_i)

    for j in Top_yr:
        p_j = p_i + j + "/"
        Top_yr_list = os.listdir(p_j)

        for k in Top_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for z in D['data']['pincodes']:
                name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']

                clm['Pincode'].append(name)
                clm['Insurance_count'].append(count)
                clm['Insurance_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

Top_Insurance = pd.DataFrame(clm)
print(Top_Insurance.head())
