# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:49:11 2023

@author: domin
"""
import string
import networkx as nx
import matplotlib.pyplot as plt
import imageio
import os
import copy

def random_planar_graph_generator(n = 15, #input("number of nodes"), 
                                  p = 0.35,  #input("probability of edge creation"), 
                                  to_adjac_matrix = True,
                                 seed = None):
    """
    + generates planar graph of degree 5 with custom number of nodes and edge probability
    + beyond 15 nodes at p=0.42, it will be harder to get a planar graph.
    """
    while True:
        random_graph = nx.fast_gnp_random_graph(n = n, #input("number of nodes"), 
                                                p = p,  #input("probability of edge creation"), 
                                                seed=seed, directed=False)
        if nx.algorithms.planarity.check_planarity(random_graph)[0]:
            if max(nx.degree(random_graph))[1]>4:
                if nx.is_connected(random_graph):
                    break
    if to_adjac_matrix:
        
        #default graphs have digit nodes, which is not that practical here
        mapping = dict(zip(random_graph, string.ascii_lowercase))
    
        # nodes to characters a through z
        random_graph_relabeled = nx.relabel_nodes(random_graph, mapping)
        
        #plot uncolored
        posit=nx.planar_layout(random_graph_relabeled)
        nx.draw(random_graph_relabeled,posit, with_labels = True)
        plt.show()
        
        return nx.to_dict_of_lists(random_graph_relabeled)
    else:
        return random_graph


def four_chromatic(adj_matrix = None, 
                   input_graph = None, 
                   list_of_4_colors = None,
                   n = 15,   #input("number of nodes")
                   p = 0.4,  #input("probability of edge creation") for random graph
                   makeGif = False):
    
    """
    coloring planar graph with 4 colours
    -------------------------------------
    choose your own colors and input them as list to list_of_4_colors.
    For a simple plot, use makeGif = False; to get a gif, set it to True and specify folder.
    """
    if list_of_4_colors:
        input_options = list_of_4_colors
    else:
        input_options=['mediumturquoise','darkorange','lightgreen','darkorchid']
    
    
    #init label assignemnt to nodes
    labels = {}
    
    #deal with input
    if adj_matrix:
        inputG = nx.Graph(adj_matrix)
    elif input_graph:
        inputG = input_graph
    else:
        inputG = nx.Graph(random_planar_graph_generator(n=n, p=p))
    
    #init waiting list with the first node
    waiting_list = [list(inputG.nodes())[0]]
    
    visited = []
    
    
    while waiting_list:
        
       # print(waiting_list)
        #refresh options for every visited node
        options=copy.deepcopy(input_options)
        
        #remove current node from waiting list and assign it as currentNode
        currentNode = waiting_list.pop(0)
        
        #iterate over its neighbors
        for n in list(inputG.neighbors(currentNode)):
    
            #add to waiting list if not there
            if (n not in waiting_list) & (n not in visited):
                waiting_list.append(n)
            
            #if in lebel keys, remove the value
            if n in list(labels.keys()):
                if labels[n] in options:
                    options.remove(labels[n])
                
                
        #color the current node
        labels.__setitem__(currentNode, options[0])
        visited.append(currentNode)
        
    # print(labels)
    # print(list(testingG.nodes()))
    # print(list(labels).sort())
    
    if not makeGif:
        posit=nx.planar_layout(inputG)
        nx.draw(inputG,posit, node_color=[labels[n] for n in list(inputG.nodes())], with_labels = True)
        plt.show()
    
    if makeGif:
        new_labels = [labels[n] for n in list(inputG.nodes())] #corresponding to nodes ordered alphabetically
        color_map = ["black" for c in new_labels]
                
        #init list with filnames, so we can use it for gifmaker later on
        filenames = []
        
        #PLOT ALL BLACK init graph
        # create file name and append it to a list
        filename = f'{0}.png'
        filenames.append(filename)
        #nx.draw(G, posit,node_color=color_map, with_labels=True)
        posit=nx.planar_layout(inputG)
        if len(list(inputG.nodes()))>7:
            nx.draw(inputG,posit, node_color=color_map, with_labels = True, edge_color = "midnightblue")
        else:
            nx.draw(inputG, posit,node_color=color_map, node_size =1800, 
                with_labels=True, edge_color = "midnightblue", 
                font_weight="semibold")
        plt.rcParams["figure.figsize"] = (9,6)
        
        # SAVE FIG
        plt.savefig(os.path.join(path2filenames,"figs",filename))
        plt.show()
        
        for i in range(len(new_labels)):
            # create file name and append it to a list
            filename = f'{i+1}.png'
            filenames.append(filename)
            color_map[:i+1] = new_labels[:i+1]
            if len(list(inputG.nodes()))>7:
                nx.draw(inputG,posit, node_color=color_map, with_labels = True, edge_color = "midnightblue")
            else:
                nx.draw(inputG, posit,node_color=color_map, node_size =1800, with_labels=True, 
                    edge_color = "midnightblue", font_weight="semibold")
            plt.rcParams["figure.figsize"] = (9,6)
            # save frame
            if i == len(new_labels)-1:   #make the gif wait a bit on the last plot
                for additionals in range(10):
                    filename = f'{i+1+additionals}.png'
                    filenames.append(filename)
                    plt.savefig(os.path.join(path2filenames,filename))
            plt.savefig(os.path.join(path2filenames,filename))
            plt.show() 
      
         # build gif
        with imageio.get_writer(os.path.join(path2filenames,'coloring.gif'), mode='I', fps=4) as writer:
            for filename in filenames:
                image = imageio.imread(os.path.join(path2filenames,filename))
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
    path2filenames = "../gifmaker" 
    
    four_chromatic(adj_matrix=graph1,makeGif=False, p=0.42)