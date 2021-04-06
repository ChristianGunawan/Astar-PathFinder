import networkx as nx
import matplotlib.pyplot as plt
from read_input import coordinateDict
from PathFinder import Astar, treeDict


def graphMaker(start, goal):
    # Inisialisasi Graph
    G = nx.Graph()
    # Initialize variables from PathFinder
    visited_graph, ordered_sequence, cost_function = Astar(start, goal)
    # Jarak
    distance_sum = 0
    for i in range(len(ordered_sequence) - 1):
        distance_sum += treeDict[ordered_sequence[i]][ordered_sequence[i + 1]]
    # Bentuk semua nodes
    for nodes in treeDict:
        G.add_node(nodes, pos = (coordinateDict[nodes]['lat'], coordinateDict[nodes]['lng']))
    # Bentuk semua edges
    for nodes in treeDict:
        for children in treeDict[nodes]:
            G.add_edge(nodes, children, weight = treeDict[nodes][children])
    
    # Posisi
    pos = nx.get_node_attributes(G, 'pos')
    # Bobot
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,pos, edge_labels= labels)
    # Mewarnai node yang dikunjungi
    node_color = []
    for node in G.nodes:
        if node in ordered_sequence:
            node_color.append("red")
        else :
            node_color.append("blue")
        
    nx.draw(G, pos , with_labels = True, node_size = 1000,  node_color = node_color)
    for i in range(len(ordered_sequence)):
        if(i != len(ordered_sequence) - 1):
            print(f"{ordered_sequence[i]} =>", end = " ")
        else:
            print(ordered_sequence[i])
    print(f"Panjang lintasan adalah {distance_sum}")
    plt.show()