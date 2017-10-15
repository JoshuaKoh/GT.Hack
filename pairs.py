
# coding: utf-8

# In[ ]:


import pandas as pd
import itertools as it
import collections as col
import networkx as nx
import matplotlib.pyplot as plt

count = col.Counter()
combos = []
df = pd.read_csv('Data/10000_transactions.csv', engine="python")
listy = []
#make a list
for i in range(1,17955):
    for a in range(0,len(df[df.order_number==df.iloc[i].order_number])):
        listy.append((df[df.order_number==df.iloc[i].order_number]).iloc[a].product_name)
    combos = combos + list(it.combinations(listy,2))
    listy = []
#print count(combos)

for pair in combos:
    count[pair] = count[pair]+1
common = count.most_common()[0:12]
print common
ids = {}
i=0
for cell in common:
    if cell[0][0] not in ids:
        ids[cell[0][0]] = i
        i = i + 1
for cell in common:
    if cell[0][1] not in ids:
        ids[cell[0][1]] = i
        i = i + 1
#print ids

#networkx junk
G = nx.Graph()

for cell in common:
    #G.add_node(cell[0][0])
    #G.add_node(cell[0][1])
    G.add_edge(cell[0][0],cell[0][1],color='r',weight=cell[1]*0.05)

pos = nx.spring_layout(G,k=0.1,iterations=3)

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]

plt.figure(50,figsize=(10,8)) 
nx.draw(G, pos, edges=edges, edge_color=colors, width=weights)
nx.draw_networkx_labels(G,pos)
plt.show()


    

