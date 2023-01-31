# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 03:14:50 2021

@author: domin
"""
import networkx as nx
import copy
from planarityCheck import nxgraphmaker
from shortest_path import find_shortest_path

def col_swaper (dic,orderedNeibs,col_labels): #set dic=adjlist in coloring
    '''col_labels is dictionary {node:color} created during in coloring()'''
    G=nxgraphmaker(dic)
    w_1and3=[col_labels[orderedNeibs[0]],col_labels[orderedNeibs[2]] ]
    w_2and4=[col_labels[orderedNeibs[1]],col_labels[orderedNeibs[3]] ]
    #print([w_1and3,w_2and4])
    collist=[w_1and3,w_2and4]
    
    #for i in range(2): need to check only one pair - if the first if connected, then automatically take second
    nodelist=[]
    for node, color in col_labels.items():
        if color in collist[0]:
            nodelist.append(node)
    subColors=G.subgraph(nodelist)
    subDict=nx.to_dict_of_lists(subColors) #gives dictionary of subG for BFS
    answer=find_shortest_path(graph=subDict,start=orderedNeibs[0],end=orderedNeibs[2]) #BFS more or less
    if not answer:
        answer=[orderedNeibs[0],orderedNeibs[2]]
    else:
        answer=[orderedNeibs[1],orderedNeibs[3]]
    #print(answer)
    
    new_col_labels=copy.deepcopy(col_labels)
    new_col_labels[answer[0]]=col_labels[answer[1]]
    new_col_labels[answer[1]]=col_labels[answer[0]]
    #print(col_labels,new_col_labels)
    return new_col_labels
    