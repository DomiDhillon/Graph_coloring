# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 02:02:40 2021

@author: domin
"""
from subG import subG

def ordering_neibs(dic,node5d):
    '''return order (cw or ccw) of neighbors of the 5deg node
    Important is that they are connected to each other in that order'''
    sub=subG(dic=dic,node5d=node5d)
    ordered_list=[]
    visited_list=[node5d]
    centerNode=node5d
    for i in range(len(list(sub.neighbors(node5d)))): #itterate x-time (x=num of neibs)
        j=0
        while list(sub.neighbors(centerNode))[j] in visited_list:
            j+=1
            if j==len(list(sub.neighbors(centerNode))):
                return ordered_list
        being_visited=list(sub.neighbors(centerNode))[j]
        ordered_list.append(being_visited)
        visited_list.append(being_visited)
        centerNode=being_visited
    print("Ordering of neighbors: {}".format(ordered_list))
    return ordered_list