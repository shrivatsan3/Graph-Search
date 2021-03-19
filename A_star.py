# -*- coding: utf-8 -*-
"""
ASEN 5519
ALGORITHMIC MOTION PLANNING

Program to demonstrate the working of A* Algorithm on a graph
input : Graph with vertices, edges, weights and heuristics defined
output : Path to goal and the length of path

Author: Shrivatsan K.
"""

class Graph:
    
    def __init__(self):
        self.graph = {}     # initialize the graph as an empty dictionary 
        self.heuristics = {}
    def add_element(self, graph, vertex, neighbor, weight):
        if vertex not in graph:
            graph[vertex] = []      # add edges in an adjacency list manner with vertices as the keys
        graph[vertex].append((neighbor, weight))
    
    def add_heuristic(self, heuristics, vertex, heuristic):
        if vertex not in heuristics:
            heuristics[vertex] = []      
            heuristics[vertex].append(heuristic)
        
    def define_graph(self):             # add new vertex and its associated edges
        vertex = input("add vertex: ")
        heuristic = input("enter its heuristic: ")
        self.add_heuristic(self.heuristics, vertex, heuristic)
        No_of_neighbors = int(input("\nenter number of neighbors: "))   
           
        for i in range(No_of_neighbors):
                neighbor = input('\nenter {} neighbor: '.format(i+1))
                weight = float(input('enter associated weight: '))
                self.add_element(self.graph, vertex, neighbor, weight)
      
G = Graph()
G.graph = {'start':[('A',1),('B',1),('C',1)],                       #defining graph
            'A':[('start',1),('D',1),('E',1),('F',3)],
            'B':[('start',1),('G',4),('H',1),('I',2)],
            'C':[('start',1),('J',1),('K',1),('L',1)],
            'D':[('A',1)],
            'E':[('A',1),('goal',3)],
            'F':[('F',3)],
            'G':[('B',4),('goal',3)],
            'H':[('B',1)],
            'I':[('B',2),('goal',3)],
            'J':[('C',1)],
            'K':[('C',1),('goal',2)],
            'L':[('C',1)],
            'goal':[('E',3),('G',3),('I',3),('K',2)]}

G.heuristics = {'A':3,              #defining heuristics at each node as given in ppt slide
                'B':2,
                'C':3,
                'D':3,
                'E':1,
                'F':3,
                'G':2,
                'H':1,
                'I':2,
                'J':3,
                'K':2,
                'L':3,
                'goal':0}    

 
visited_nodes = []          #list to keeps track of all the nodes that have been visited
priority_queue = []         #list to keeps track of shortest path
path = []                   #list of nodes to be followed to goal
        
visited_nodes.append('start')           #visit the start node
priority_queue.append('start')          #add start node to priority list
path.append('start') 
for i in G.graph[priority_queue[0]]:    #add the neighbors of start   
        f = i[1] + G.heuristics[i[0]]                    
        priority_queue.append((i[0],f))
        visited_nodes.append(i[0])
    
priority_queue.pop(0)
priority_queue.sort(key=lambda tup: tup[1])     #sort the nodes according to cost function or priority
number_of_iterations = 1


while priority_queue:
        number_of_iterations = number_of_iterations+1
        
        if(priority_queue[0][0] == 'goal'):     #if goal is the first element, then shortest path to goal has been found
            break
        
        else:            
            
            for i in G.graph[priority_queue[0][0]]:         #add the neighbors of the first node in priority queue
                if i[0] == 'start':         #fisrt run of this will cause start to be classified as neighbor. Dont add start to the queue
                    continue
                if i[0] in visited_nodes and i[1] > priority_queue[0][1]:  #if a shorter path has been found for a node that has already been visited, then add it to the queue
                    continue
                else:
                    f = priority_queue[0][1] + i[1] + G.heuristics[i[0]] - G.heuristics[priority_queue[0][0]]  #calculating priority
                    priority_queue.append((i[0],f))
                    visited_nodes.append(i[0])
                    
            path.append(priority_queue[0][0])
            priority_queue.pop(0)                    
            priority_queue.sort(key=lambda tup: tup[1])         #sort according to priority
path.append('goal')
path_flag = 0

for node in reversed(path):
    
    if node == 'start':
        continue
    
    if (path_flag == 1):
        path.remove(node)
        
    if (path_flag == 0):
        for neighbor in G.graph[node][0] :
            if neighbor == 'start':
                path_flag = 1
                break
           
print(path) 
print('Final point in path and its distance from start: ')                            
print(priority_queue[0])    