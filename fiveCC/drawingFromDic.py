# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:25:17 2021

@author: domin
"""

from IPython.display import Image, display
import networkx as nx
import matplotlib.pyplot as plt
import copy
from .planarityCheck import nxgraphmaker

#import os     
#os.environ['PATH'].split(os.pathsep)
#os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

graph1 = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C','G'],
         'E': ['A','F','D'],
         'F': ['A','C','D'],
         'G':['B','D','E']}

def adjlisting(dic):
    '''get propre adj dictionary from manually written dic;
    u need it for coloring'''
    G=nx.Graph()
    for key, value in dic.items():
        for i in range(len(value)):
            #edge=pydot.Edge(key,value[i])
            G.add_edge(key,value[i])
    #M=nx.to_pandas_adjacency(G)
    M=nx.to_dict_of_lists(G)
    return M

def drawing_uncolored (dic):
    '''plots the graph with planar layout; input: adj dictionary'''
    G=nx.Graph()
    #color="green"
    #for key in dic:
    #    node=pydot.Node(key,style="filled",fillcolor=color)
    #    G.add_node(node)
    for key, value in dic.items():
        for i in range(len(value)):
            #edge=pydot.Edge(key,value[i])
            G.add_edge(key,value[i])
    posit=nx.planar_layout(G)
    nx.draw(G, posit, with_labels=True,node_size=1000)
    plt.show()
    
def drawing_colored(dic):
    adjlist=adjlisting(dic=dic) #to be sure all neighbors are listed with each node
    colors=['lightblue','pink','green','red','purple']
    #colors.sort() #if sorted alphabetically, the 'min' can be selected later on -> don't need this, the min selects alphabet' min anyway
    for value in adjlist.values(): #neighbors in ascending order #SHOULD IMPLEMENT CLOCKWISE ORDERING HERE
        value.sort()
        
    col_labels={}
    for key, value in adjlist.items():
        if len(value)<5:#if less than 5 neighbors
            if key not in col_labels:
                col_labels.__setitem__(key,"")
            options=copy.deepcopy(colors)
            for col in options:
            
                if not col_labels[key]:       #if the graph is connected,
                                              # only the first node will be found empty - the others will be neighbors
                    col_labels[key]=min(options) #get it one by one alphabetically
                    print(options) #----------------------------------------------------------
                    options.remove(min(options))
                    print(options) #-----------------------------------------------------
                for neib in value:
                    if neib not in col_labels:
                        col_labels.__setitem__(neib,"")
                    if not col_labels[neib]:
                        col_labels[neib]=min(options)
                        options.remove(min(options))
        if len(value)==5: #the vertex of degree=5
            #if for any vertex the color of vertex==color of any neighbor:
                #swap col 1 and 3 (or 2 and 4) of neighbors w1 and w3 (or w2 and w4)
            
    G=nxgraphmaker(adjlist)
    posit=nx.planar_layout(G)
    nx.draw(G, posit,node_color=col_labels.values(), with_labels=True,node_size=1000)
    plt.show()
              