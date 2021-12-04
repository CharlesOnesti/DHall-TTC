from graph import Graph

g = Graph([0,1,2,3,4,5,6])
g.addEdge(0, 4)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(3, 0)
g.addEdge(4, 0)
g.addEdge(5, 0)
g.addEdge(6, 4)

# print(g.graph)
# print(g.V)
g.findSCCs()

print(g.sccs)