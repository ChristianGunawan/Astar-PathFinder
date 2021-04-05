import networkx as nx
import matplotlib.pyplot as plt
from read_input import read_input
from PathFinder import Astar, treeDict


def graphMaker(start, goal):
    # Inisialisasi Graph
    G = nx.Graph()
    # Initialize variables from PathFinder
    visited_graph, ordered_sequence, cost_function = Astar(start, goal)
    # Bentuk semua nodes
    for nodes in treeDict:
        for children in treeDict[nodes]:
            G.add_edge(nodes, children)
    nx.draw(G, with_labels = True)
    plt.show()

if __name__ == "__main__":
    print(treeDict)
    graphMaker("S", "G")