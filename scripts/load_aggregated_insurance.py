# 3. Aggregated Insurance

python
import pandas as pd
import json
import os

path = "pulse/data/aggregated/insurance/country/india/state/"
Agg_state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Insurance_count': [],
    'Insurance_amount': []
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

            for z in D['data']['transactionData']:
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']

                clm['Insurance_count'].append(count)
                clm['Insurance_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

Agg_Insurance = pd.DataFrame(clm)
print(Agg_Insurance.head())


---