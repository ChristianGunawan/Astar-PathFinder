import networkx as nx
import matplotlib.pyplot as plt
from read_input import read_input
from PathFinder import Astar, treeDict, oneWayPathDict


def graphMaker(start, goal):
    # Inisialisasi Graph
    G = nx.Graph()
    # Initialize variables from PathFinder
    visited_graph, ordered_sequence, cost_function = Astar(start, goal)
    # Bentuk semua nodes
    for nodes in oneWayPathDict:
        for children in oneWayPathDict[nodes]:
            G.add_edge(nodes, children, weight = oneWayPathDict[nodes][children])
    nx.draw(G, with_labels = True)
    labels = nx.get_edge_attributes(G, 'weight')
    pos = nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G,pos, edge_labels= labels)
    
    plt.show()
    

if __name__ == "__main__":
    print(treeDict)
    graphMaker("ITB", "Goal")