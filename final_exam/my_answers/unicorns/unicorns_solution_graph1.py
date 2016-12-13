# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from operator import itemgetter
from sklearn import linear_model
from math import log


#%matplotlib inline

"""
Display Startups along with their Investors
"""
Startups_and_Investors = pd.read_csv('investors_in_unicorns.tsv', sep='\t')
Startups_full_list = pd.read_csv("unicorns.tsv",sep='\t')

def fixup(s):
   return s.replace('-','_').replace('(','_').replace(')','_').replace('&','_').replace('/','_').replace('.','_').replace('!','_')

def isConnected(node1,node2,Startups_with_a_common_Investor):
    return any((Startups_with_a_common_Investor.Company_x==node1)&(Startups_with_a_common_Investor.Company_y==node2))
"""
Display the graph of Startups that share a common Investor
"""
Startups_with_a_common_Investor = pd.merge( left=Startups_and_Investors, right=Startups_and_Investors, how="inner",
                                           left_on="Investor", right_on="Investor")[['Company_x', 'Company_y']].drop_duplicates()

Startups_with_a_common_Investor = Startups_with_a_common_Investor[
                             Startups_with_a_common_Investor['Company_x'] != Startups_with_a_common_Investor['Company_y'] ]


#Startups_with_a_common_Investor_r=pd.DataFrame(index=range(0,len(Startups_with_a_common_Investor)/2),columns=["Company_x","Company_y"])
#Startups_full_list = pd.DataFrame(Startups_and_Investors.Company.drop_duplicates())


count=0

Gcc = nx.Graph()

for x in Startups_with_a_common_Investor[['Company_x', 'Company_y']].values:
    startup0  = fixup(x[0])
    startup1 = fixup(x[1])
#    if (any((Startups_with_a_common_Investor_r.Company_x==startup1)&(Startups_with_a_common_Investor_r.Company_y==startup0))==False):
#        Startups_with_a_common_Investor_r.iloc[count]=[startup0,startup1]
#        count=count+1
    Gcc.add_edge( startup0, startup1 )


"""
(a)
determine the number of connected components
"""
#print "number of connected edges:"+str(len(Startups_with_a_common_Investor)/2)
print "number of connected components:"+str(len(Startups_with_a_common_Investor['Company_x'].drop_duplicates()))

"""
(b) 
print top 10 degree distribution 
determine if degree distribution follows power law.
"""  
node_and_degree = Gcc.degree()
list_of_degree = sorted( node_and_degree.items(), key=itemgetter(1), reverse=True )  # high connectivity among Startups
list_of_degree_values = map(itemgetter(1), list_of_degree)
list_of_degree_values = list_of_degree_values[0:100]

# print top 10 and store all
for i in range(0,10):
    print "number "+str(i)+": "+list_of_degree[i][0]+ " " + str(list_of_degree[i][1])
# determine if degree distribution follows power law.
plt.figure(figsize=(50,50))
regr = linear_model.LinearRegression()
regr.fit(pd.DataFrame(range(0,len(list_of_degree_values))), pd.DataFrame(np.log(list_of_degree_values)))
plt.plot(range(0,len(list_of_degree_values)),np.log(list_of_degree_values),'o')
x=np.arange(0,len(list_of_degree_values))
y=regr.coef_[0][0]*x+regr.intercept_[0]
plt.title("log(degree_distribution) ~ rank")
plt.plot(x,y,'-')

"""
(c) 
compute eigenvector centrality of the nodes
print top 10.
"""
eigvec = nx.eigenvector_centrality(Gcc)
node_eigvec = sorted( eigvec.items(), key=itemgetter(1), reverse=True )
for i in range(0,10):
    print "number "+str(i)+": "+node_eigvec[i][0]+ " " + str(node_eigvec[i][1])

"""
(d)
diameter.
"""
print "diameter:"+str(nx.diameter(Gcc))

"""
(e): compute clustering coefficient.
"""
#range(start,stop) excluding stop.
triangles=0
path_of_2 = 0
length = len(Startups_full_list)
Startups_full_list=Startups_full_list["Company"].tolist()
for i in range(0,length):
    node1=Startups_full_list[i]
#    print "i:"+str(i)
    for j in range(i+1, length):
        node2=Startups_full_list[j]
#        print "i:"+str(i)+" j:"+str(j)
        for k in range(j+1, length):  
            node3=Startups_full_list[k]
#            print "i:"+str(i)+" j:"+str(j)+" k:"+str(k)
            temp1 =    isConnected(node1,node2,Startups_with_a_common_Investor)     
            temp2 =    isConnected(node2,node3,Startups_with_a_common_Investor)    
            temp3 =    isConnected(node1,node3,Startups_with_a_common_Investor)    
            if ( temp1==True & temp2==True):
                path_of_2=path_of_2 + 1
            if ( temp1==True & temp3==True):
                path_of_2=path_of_2 + 1
            if ( temp2==True & temp3==True):
                path_of_2=path_of_2 + 1
                
            if ( temp1 == True & temp2==True & temp3==True):
                triangles=triangles+1

print "clustering coefficient:"+str(3.0*triangles/path_of_2)

print "average clustering using library:"+str(nx.average_clustering(Gcc))
#print "APL:"+str(nx.average_shortest_path_length(Gcc))

# drawing the graph (optional)
#for x in Startups_full_list[['Company']].values:
#    Gcc.add_node(fixup(x[0]))
#
#plt.figure(figsize=(30,40))
#pos = nx.spring_layout(Gcc)
#nx.draw_networkx_nodes(Gcc, pos, node_size=20)
#nx.draw_networkx_edges(Gcc, pos, edgelist=[(u,v) for (u,v,d) in Gcc.edges(data=True)], width=0.2, edge_color="b", alpha=0.5)
#nx.draw_networkx_labels(Gcc, pos, font_size=8, font_family='sans-serif', font_color="b", alpha=0.2)
#plt.axis('off')
#plt.show()