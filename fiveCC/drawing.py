# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:25:17 2021

@author: domin
"""

import networkx as nx
import matplotlib.pyplot as plt
import copy
from planarityCheck import nxgraphmaker, planarityCheck
from ordering_neighbors import ordering_neibs
from col_swaper import col_swaper

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
    
def coloring2(dic,colors=None):
    adjlist=adjlisting(dic=dic) #to be sure all neighbors are listed with each node
    if planarityCheck(dic=adjlist):
        print("The graph is planar.")
    else:
        return("Not planar, can't do.")
    if not colors:
        colors=['lightblue','pink','green','red','purple']
    #colors.sort()
    for value in adjlist.values(): 
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
                    #print(options) 
                    options.remove(min(options))
                    #print(options)
                for neib in value:
                    if neib not in col_labels:
                        col_labels.__setitem__(neib,"")
                    if not col_labels[neib]:
                        col_labels[neib]=min(options)
                        options.remove(min(options))
        if len(value)==5: #the vertex of degree=5
            ######COLOR-CLASH CHECKER TO IMPLEMENT#########
            node5d=key #coloring will be rearanged around this node
    
    orderedNeibs=ordering_neibs(dic=adjlist,node5d=node5d) #ordering neighbors of the 5deg node
    col_labels=col_swaper(dic=adjlist,orderedNeibs=orderedNeibs,col_labels=col_labels) #changing colors between w1 and w3 (or w2 and w4)
    G=nxgraphmaker(adjlist)
    posit=nx.planar_layout(G)
    nx.draw(G, posit,node_color=col_labels.values(), with_labels=True)
    plt.show()
              