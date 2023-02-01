# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:51:41 2023

@author: domin
"""
import os
import imageio
import networkx as nx
import matplotlib.pyplot as plt
import copy
from planarityCheck import nxgraphmaker
from col_swaper import col_swaper
from drawing import adjlisting

def coloring4gif(dic,colors=None):
    adjlist=adjlisting(dic=dic) #to be sure all neighbors are listed with each node
    if planarityCheck(dic=adjlist):
        print("The graph is planar.")
    else:
        return("Not planar, can't do.")
    if not colors:
        colors=['mediumturquoise','darkorange','lightgreen','darkorchid','deeppink']
    #colors.sort()
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
        #inside col_swaper implement bfs/connect check:create subgraph of 2 colors, check whether the nodes w1 and w3 in this subG are connected
    G=nxgraphmaker(adjlist)
    posit=nx.planar_layout(G)
    color_map = ["black" for c in col_labels.values()]
    print(len(col_labels))
    
    #SAVE FIGS
    #init list with filnames, so we can use it for gifmaker later on
    filenames = []
    
    #PLOT ALL BLACK init graph
    # create file name and append it to a list
    filename = f'{0}.png'
    filenames.append(filename)
    #nx.draw(G, posit,node_color=color_map, with_labels=True)
    nx.draw(G, posit,node_color=color_map, node_size =1800, with_labels=True, edge_color = "midnightblue", font_weight="semibold", alpha = 0.9)
    plt.rcParams["figure.figsize"] = (9,6)
    # save frame
    plt.savefig(os.path.join(path2filenames,"figs",filename))
    plt.show()
    
    for i in range(len(col_labels.values())):
        # create file name and append it to a list
        filename = f'{i+1}.png'
        filenames.append(filename)
        color_map[:i+1] = list(col_labels.values())[:i+1]
        #nx.draw(G, posit,node_color=color_map, with_labels=True)
        nx.draw(G, posit,node_color=color_map, node_size =1800, with_labels=True, edge_color = "midnightblue", font_weight="semibold", alpha = 0.9)
        plt.rcParams["figure.figsize"] = (9,6)
        # save frame
        plt.savefig(os.path.join(path2filenames,"figs",filename))
        plt.show() 
  
     # build gif
    with imageio.get_writer(os.path.join(path2filenames,"figs",'coloring.gif'), mode='I', fps=4) as writer:
        for filename in filenames:
            image = imageio.imread(os.path.join(path2filenames,"figs",filename))
            writer.append_data(image)
        writer.close()
    plt.close()

    # Remove files
    for filename in set(filenames):
        os.remove(os.path.join(path2filenames,"figs",filename))
        
        
if __name__ == "__main__":
       
    #generate graph
    graph1 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C','G'],
             'E': ['A','F','D'],
             'F': ['A','C','D'],
             'G':['B','D','E']}
    
    #to folder with "figs" folder -> to store separate plots
    path2filenames = ".../gifmaker/" 
    
    #run gifmaker
    coloring4gif(graph1)
