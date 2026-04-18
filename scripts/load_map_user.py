
# 1. Map User

python
import pandas as pd
import json
import os

path = "pulse/data/map/user/hover/country/india/state/"
Map_state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'Registered_users': [],
    'App_opens': []
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

            for z, x in D['data']['hoverData'].items():
                district = z
                registered = x['registeredUsers']
                appopens = x['appOpens']

                clm['District'].append(district)
                clm['Registered_users'].append(registered)
                clm['App_opens'].append(appopens)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

Map_User = pd.DataFrame(clm)
print(Map_User.head())


---
