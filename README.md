# Graph_coloring
Assigning 4-chromatic labels to a planar graph vertices, such that there's no 2 adjascent vertices that have the same colour.

<img src="https://user-images.githubusercontent.com/65451658/216033613-cb2084e9-afb7-424f-9e72-1415e1d04309.gif" width="600" height="400"/>

+ NetworkX


## **Algorithm used for 4-coloring:**
     ```
     init waiting_list <- first_node
     init visited list
     
     While there's items in the waiting_list, do:
         refresh options for colors
         current_node = first on the waiting_list 
         (current_node gets to be popep out from waiting list)
         add all neighbors to waiting list, if they are not there and they are not listed in visited
         color current_node:
              remove curent_node's neighbors' colors (if they exist) from the options
              color with the first option in the list
         maked the current_node as visited
     Plot graph
     ```
+ use ```fourCC.py``` to plot or make gif -> custom input of parameters



## **Algorithm used for 5-coloring**
```
     dictionary -> adjacency matrix -> graph
     check planarity
     color nodes such that every 2 adjacent nodes have different labels -> it will probably clash around the 5-degree vertice
     order the neighbors of 5-degree vertice in clockwise order
     swap color between vertice 1 and 3 if they are not connected, otherwise swap colours of v2 and v4.
     plot the graph using the right color labels
```
  
  + for a static plot, use coloring2 function from ```drawing.py```; for gif, use ```gifmaker.py``` from fiveCC
  + theory and explanation for 5-coloring in the notebook
  + didn't work for randomly generated graphs -> neighbors of 5d node should connected for it to work (?)




