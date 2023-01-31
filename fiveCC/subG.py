# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 02:52:54 2021

@author: domin
"""

from planarityCheck import nxgraphmaker

def subG (dic,node5d):
    '''creates a subgraph of the 5-deg node and its neighbors'''
    G=nxgraphmaker(dic)
    nodeList=[nei for nei in G.neighbors(node5d)]
    nodeList.append(node5d)
    subGraph=G.subgraph(nodeList)
    return subGraph