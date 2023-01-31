# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:33:29 2021

@author: domin
"""

import networkx as nx


def nxgraphmaker(dic):
    '''return nx.Graph() object from dictionary'''
    G=nx.Graph()
    for key, value in dic.items():
        for i in range(len(value)):
            #edge=pydot.Edge(key,value[i])
            G.add_edge(key,value[i])
    return G

def planarityCheck(dic):
    '''check whether graph is planar (dict input);
    can use without adjlisting'''
    G=nxgraphmaker(dic=dic)
    is_planar=nx.algorithms.planarity.check_planarity(G)[0]
    return is_planar

