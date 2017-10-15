
import pandas as pd
import networkx as nx

df = pd.read_csv('Data/10000_transactions.csv', engine="python")
listy = {}
top = [[0,"",[]],[0,"",[]],[0,"",[]],[0,"",[]],[0,"",[]]]
for i in range(0,17955):
    if df.iloc[i].product_name not in listy:
        listy[""+df.iloc[i].product_name] = 0
    listy[""+df.iloc[i].product_name] = listy[""+df.iloc[i].product_name] + 1
for key in listy:
    for i in range(0,5):
        if listy[key]>top[i][0]:
            #shift
            for a in range(i+2,5):
                top[a][0] = top[a-1][0]
            top[i][1] = key
            top[i][0] = listy[key]
            break  
print(top)
for key in listy:
    print key+": "+str(listy[key])
#now get number of unique people for each





    
