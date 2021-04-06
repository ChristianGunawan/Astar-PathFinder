import networkx as nx
import matplotlib.pyplot as plt
from read_input import coordinateDict
from PathFinder import Astar, treeDict


def graphMaker(start, goal):
    # Inisialisasi Graph
    G = nx.Graph()
    # Initialize variables from PathFinder
    visited_graph, ordered_sequence, cost_function = Astar(start, goal)
    # Bentuk semua nodes
    for nodes in treeDict:
        G.add_node(nodes, pos = (coordinateDict[nodes]['lat'], coordinateDict[nodes]['lng']))
    # Bentuk semua edges
    for nodes in treeDict:
        for children in treeDict[nodes]:
            G.add_edge(nodes, children, weight = treeDict[nodes][children])

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos , with_labels = True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,pos, edge_labels= labels)
    plt.show()
    
if __name__ == "__main__":
    print(treeDict)
    graphMaker("ITB", "DagoH")