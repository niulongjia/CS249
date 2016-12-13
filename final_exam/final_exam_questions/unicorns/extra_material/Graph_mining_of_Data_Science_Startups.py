# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
#%matplotlib inline
Startups = pd.read_csv('data_science_startups.tsv', sep='\t')
Startups.shape
Startups.head()

"""
Display Startups by the City in which they are located
"""
G=nx.Graph()

for x in Startups[['name', 'city']].values:
    startup = x[0].replace(' ','_')
    city = x[1].replace(' ','_')
    G.add_edge( startup, city )
     
city_adjacency = [
   ('San_Francisco', 'San_Ramon'),
   ('San_Mateo', 'San_Francisco'),
   ('Redwood_City', 'San_Mateo'),
   ('Menlo_Park', 'Redwood_City'),
   ('Palo_Alto', 'Menlo_Park'),
   ('Mountain_View', 'Palo_Alto'),
   ('Sunnyvale', 'Mountain_View'),
   ('Santa_Clara', 'Sunnyvale'),
   ('San_Jose', 'Santa_Clara'),
   ('Cupertino', 'Sunnyvale'),
   ('Cupertino', 'Santa_Clara'),
   ('Cupertino', 'San_Jose'),
   ('Los_Gatos', 'Cupertino'),
   ('Los_Gatos', 'San_Jose')]


for x, y in city_adjacency:
     x_ = x.replace(' ','_')
     y_ = y.replace(' ','_')
     G.add_edge( x_, y_ )




#plt.figure(figsize=(25,18))
#
#pos = nx.fruchterman_reingold_layout(G) # positions for all nodes
#
## nodes
#nx.draw_networkx_nodes(G, pos, node_size=5)
#
#nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for (u,v,d) in G.edges(data=True)], width=1, edge_color="m", alpha=0.5)
#
#nx.draw_networkx_labels(G, pos, font_size=14, font_family='sans-serif', font_color="b", alpha=0.4)
#
#plt.axis('off')
#
#plt.show()

plt.figure(figsize=(18,12))
pos=nx.spring_layout(G) # positions for all nodes
# nodes
nx.draw_networkx_nodes(G, pos, node_size=3)
# edges
nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for (u,v,d) in G.edges(data=True)], width=1, edge_color="m", alpha=0.5)
# labels
nx.draw_networkx_labels(G, pos, font_size=10,font_color="b",font_family='sans-serif', alpha=0.4)
plt.axis('off')
plt.show()

"""
Display Startups by the sectors they are involved in
"""
Gs = nx.Graph()

for x in Startups[['name', 'category_list']].values:
    startup = x[0].replace(' ','_')
    sectors = x[1].split('|')
    for sector in sectors:
        Gs.add_edge( startup, sector.replace(' ','_') )

plt.figure(figsize=(28,20))
pos = nx.fruchterman_reingold_layout(Gs) # positions for all nodes
nx.draw_networkx_nodes(Gs, pos, node_size=50)
nx.draw_networkx_edges(Gs, pos, edgelist=[(u,v) for (u,v,d) in Gs.edges(data=True)], width=1, edge_color="m", alpha=0.5)
nx.draw_networkx_labels(Gs, pos, font_size=16, font_family='sans-serif', font_color="b", alpha=0.2)
plt.axis('off')
plt.show()

"""
Display Startups along with their Investors
"""
Startups_and_Investors = pd.read_csv('data_science_startups_and_investors.tsv', sep='\t')
Startups_and_Investors.shape
Startups_and_Investors.columns
Gi = nx.Graph()

def fixup(s):
   return s.replace('-','_').replace('(','_').replace(')','_').replace('&','_').replace('/','_').replace('.','_').replace('!','_')

for x in Startups_and_Investors[['name', 'investor','raised_amount_usd']].values:
    startup  = fixup(x[0])
    investor = fixup(x[1])
    Gi.add_edge( startup, investor )

plt.figure(figsize=(35,40))
pos = nx.fruchterman_reingold_layout(Gi)
nx.draw_networkx_nodes(Gi, pos, node_size=50)
nx.draw_networkx_edges(Gi, pos, edgelist=[(u,v) for (u,v,d) in Gi.edges(data=True)], width=1, edge_color="m", alpha=0.7)
nx.draw_networkx_labels(Gi, pos, font_size=16, font_family='sans-serif', font_color="b", alpha=0.2)
plt.axis('off')
plt.show()


Investor_count = Startups_and_Investors[['name','investor']].groupby('investor').count()
Shared_Investors = Investor_count[ Investor_count['name'] > 1 ]
Gsi = nx.Graph()

List_of_shared_Investors = list(Shared_Investors.index)

for x in Startups_and_Investors[['name', 'investor','raised_amount_usd']].values:
    startup  = fixup(x[0])
    investor = fixup(x[1])
    if investor in List_of_shared_Investors:
        Gsi.add_edge( startup, investor )
plt.figure(figsize=(35,40))

pos = nx.fruchterman_reingold_layout(Gsi)
nx.draw_networkx_nodes(Gsi, pos, node_size=50)
nx.draw_networkx_edges(Gsi, pos, edgelist=[(u,v) for (u,v,d) in Gsi.edges(data=True)], width=1, edge_color="m", alpha=0.5)
nx.draw_networkx_labels(Gsi, pos, font_size=16, font_family='sans-serif', font_color="b", alpha=0.2)
plt.axis('off')
plt.show()

"""
Display the graph of Startups that share a common Investor
"""


Startups_with_a_common_Investor = pd.merge( left=Startups_and_Investors, right=Startups_and_Investors, how="inner",
                                           left_on="investor", right_on="investor")[['name_x', 'name_y']].drop_duplicates()

Startups_with_a_common_Investor = Startups_with_a_common_Investor[
                             Startups_with_a_common_Investor['name_x'] != Startups_with_a_common_Investor['name_y'] ]

Startups_with_a_common_Investor.head(10)
Gcc = nx.Graph()

for x in Startups_with_a_common_Investor[['name_x', 'name_y']].values:
    startup0  = fixup(x[0])
    startup1 = fixup(x[1])
    Gcc.add_edge( startup0, startup1 )
plt.figure(figsize=(35,40))

pos = nx.spring_layout(Gcc)
nx.draw_networkx_nodes(Gcc, pos, node_size=50)
nx.draw_networkx_edges(Gcc, pos, edgelist=[(u,v) for (u,v,d) in Gcc.edges(data=True)], width=1, edge_color="m", alpha=0.5)
nx.draw_networkx_labels(Gcc, pos, font_size=16, font_family='sans-serif', font_color="b", alpha=0.2)
plt.axis('off')
plt.show()