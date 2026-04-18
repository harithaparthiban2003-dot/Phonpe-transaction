# 2. Aggregated User

python
import pandas as pd
import json
import os

path = "pulse/data/aggregated/user/country/india/state/"
Agg_state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Brand': [],
    'Count': [],
    'Percentage': []
}

for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            try:
                for z in D['data']['usersByDevice']:
                    brand = z['brand']
                    count = z['count']
                    percentage = z['percentage']

                    clm['Brand'].append(brand)
                    clm['Count'].append(count)
                    clm['Percentage'].append(percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

Agg_User = pd.DataFrame(clm)
print(Agg_User.head())


---