# Graph_coloring
Assigning 5 colour labels to planar graph vertices, such that there's no 2 adjascent vertices that have the same colour.

<img src="https://user-images.githubusercontent.com/65451658/215811559-93193ba4-fbf5-4bf7-9f0b-5798477befc0.gif" width="600" height="400"/>

+ NetworkX
+ theory and explanation of steps in the notebook
  + dictionary -> adjacency matrix -> graph
  + check planarity
  + color nodes such that every 2 adjacent nodes have different labels -> it will probably clash around the 5-degree vertice
  + order the neighbors of 5-degree vertice in clockwise order
  + swap color between vertice 1 and 3 if they are not connected, otherwise swap colours of v2 and v4.
  + plot the graph using the right color labels
+ for a static plot, use coloring2 function from drawing.py; for gif, use gifmaker.py




