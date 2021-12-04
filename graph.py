# https://www.geeksforgeeks.org/strongly-connected-components/
# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict
import copy
#This class represents a directed graph using adjacency list representation
class Graph():
   
  def __init__(self, agent_list):
    self.agent_list = agent_list # agent_list
    self.graph = defaultdict(list) # default dictionary to store graph
    self.sccs = []
  
  # function to add an edge to graph
  def addEdge(self,u,v):
    self.graph[u].append(v)
  
  # A function used by DFS
  def DFSUtil(self,v,visited, new_scc):
    # Mark the current node as visited and print it
    visited[v]= True
    new_scc.append(v)
    #Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
        if visited[i]==False:
            self.DFSUtil(i,visited,new_scc)


  def fillOrder(self,agent,visited, stack):
    # Mark the current node as visited 
    visited[agent]= True
    #Recur for all the vertices adjacent to this vertex
    for i in self.graph[agent]:
        if visited[i]==False:
            self.fillOrder(i, visited, stack)
    stack = stack.append(agent)
    

  # Function that returns reverse (or transpose) of this graph
  def getTranspose(self):
    g = Graph(self.agent_list)

    # Recur for all the vertices adjacent to this vertex
    for i in self.graph:
        for j in self.graph[i]:
            g.addEdge(j,i)
    return g

  def findSCCs(self):
    stack = []
    new_scc = []
    # Mark all the vertices as not visited (For first DFS)
    visited = { x: False for x in self.agent_list }
    # Fill vertices in stack according to their finishing
    # times
    for agent in self.agent_list:
        if visited[agent]==False:
            self.fillOrder(agent, visited, stack)

    # Create a reversed graph
    gr = self.getTranspose()
      
    # Mark all the vertices as not visited (For second DFS)
    visited = { x: False for x in self.agent_list }

    # Now process all vertices in order defined by Stack
    while stack:
        i = stack.pop()
        if visited[i]==False:
            gr.DFSUtil(i, visited, new_scc)  
            self.sccs.append(new_scc)
            new_scc = []