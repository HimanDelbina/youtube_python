import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random 


seed = 0
random.seed(seed)
np.random.seed(seed)

g = nx.Graph()
# g = nx.DiGraph()
# g.add_nodes_from("ABCDE")
# g.add_nodes_from(["A","B","C","D","E"])

# g.add_node("A")
# g.add_node("B")
# g.add_node("C")
# g.add_node("D")
# g.add_node("E")

# g.add_edges_from(["AC","BC","BD","CD","DE"])
# g.add_edges_from([('A','C'),('B','C'),('B','D'),('C','D'),('D','E')])

# g.add_edge('A','C')
# g.add_edge('B','C')
# g.add_edge('B','D')
# g.add_edge('C','D')
# g.add_edge('D','E')


# pos={
#     "A":(1,4),
#     "B":(4,3.5),
#     "C":(3.6,1.4),
#     "D":(5.8,3.5),
#     "E":(3,6),
# }


# nx.draw(g ,pos=pos, node_color= "blue",node_size = 800 ,with_labels=True,font_color="white" ,font_size= 15,font_weight="bold",width=2)
# plt.margins(0.3)
# plt.show()



g.graph["name"]="himan"

g.add_nodes_from([
    ("A",{"age":22,"gender":"Female"}),
    ("B",{"age":16,"gender":"Male"}),
    ("C",{"age":18,"gender":"Male"}),
    ("D",{"age":32,"gender":"Female"}),
    ("E",{"age":19,"gender":"Male"})
])

# g.add_node("A",age=22,gender="Female")
# g.add_node("B",age=12,gender="Male")
# g.add_node("C",age=18,gender="Male")
# g.add_node("D",age=32,gender="Female")
# g.add_node("E",age=16,gender="Male")

g.add_edges_from([
    ('A','C',{"weight":1}),
    ('B','C',{"weight":0.2}),
    ('B','D',{"weight":0.8}),
    ('C','D',{"weight":0.6}),
    ('D','E',{"weight":1.2}),
])
# g.add_edge('A','C',weight=1)
# g.add_edge('B','C',weight=0.2)
# g.add_edge('B','D',weight=0.8)
# g.add_edge('C','D',weight=0.6)
# g.add_edge('D','E',weight=1.2)


pos={
    "A":(1,4),
    "B":(4,3.5),
    "C":(3.6,1.4),
    "D":(5.8,3.5),
    "E":(3,6),
}

pos_node_attributes={}
for node,(x,y) in pos.items():
    pos_node_attributes[node]=(x,y+0.5)
    

# pos_node_attributes={
#     "A":(0.5,4.5),
#     "B":(4,4),
#     "C":(3.6,0.7),
#     "D":(6.4,4),
#     "E":(3,6.5),
# }




print(f"Node_Count = {g.number_of_nodes()}")
print(f"Edge_Count = {g.number_of_edges()}")

for deg in g.nodes:
    print(f"Degree({deg}) = {g.degree(deg)} ")
    
for neigh in g.nodes:
    neighbor_list=[n for n in g.neighbors(neigh)]
    print(f"Neighbor({neigh}) = {neighbor_list}")

for node in g.nodes(data=True):
    print(node)
    
print("######################################")
for n,d in g.nodes(data=True):
    print(n)
    print(d)
    print("######################################")
    

node_lable = {n:(d["age"],d["gender"]) for n,d in g.nodes(data=True) }



for u,v,d in g.edges(data=True):
    print(u,v)
    print(d)
    print("######################################")
edge_lable = {(u,v):d["weight"] for u,v,d in g.edges(data=True) }
    
for edge in g.edges(data=True):
    print(edge)


nx.draw(g ,pos=pos, node_color= "blue",node_size = 800 ,with_labels=True,font_color="white" ,font_size= 15,font_weight="bold",width=2 , edge_color="grey")
nx.draw_networkx_labels(g,labels=node_lable, pos=pos_node_attributes ,font_color="black" ,font_size= 10,font_weight="bold" )
nx.draw_networkx_edge_labels(g,edge_labels=edge_lable, pos=pos ,label_pos=0.5, font_color="red" ,font_size= 10,font_weight="bold" )
plt.margins(0.3)
plt.show()