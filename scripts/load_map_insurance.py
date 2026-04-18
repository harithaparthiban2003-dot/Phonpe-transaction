# 2. Map Insurance

python
import pandas as pd
import json
import os

path = "pulse/data/map/insurance/hover/country/india/state/"
Map_state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'Insurance_count': [],
    'Insurance_amount': []
}

for i in Map_state_list:
    p_i = path + i + "/"
    Map_yr = os.listdir(p_i)

    for j in Map_yr:
        p_j = p_i + j + "/"
        Map_yr_list = os.listdir(p_j)

        for k in Map_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for z in D['data']['hoverDataList']:
                district = z['name']
                count = z['metric'][0]['count']
                amount = z['metric'][0]['amount']

                clm['District'].append(district)
                clm['Insurance_count'].append(count)
                clm['Insurance_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

Map_Insurance = pd.DataFrame(clm)
print(Map_Insurance.head())


---