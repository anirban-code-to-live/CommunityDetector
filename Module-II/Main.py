import numpy as np
import networkx as nx
from scipy.sparse import csgraph

if __name__ == '__main__':
    print 'Welcome to the world of bottlenose dolphins'
    dolphin_graph = nx.read_gml('../data/dolphins.gml')
    # print dolphin_graph.nodes()
    # print dolphin_graph.edges()
    dolphin_graph_node_list = list(dolphin_graph.nodes())
    dolphin_count = len(dolphin_graph_node_list)
    print 'Dolphin count :: ' + str(dolphin_count)
    # print dolphin_graph_node_list[0]
    dolphin_graph_edge_list = list(dolphin_graph.edges())
    dolphin_graph_edge_count = len(dolphin_graph_edge_list)
    print 'Dolphin graph edge count :: ' + str(dolphin_graph_edge_count)
    # print dolphin_graph_edge_list[0]
    node_to_id = {}
    for i in range(dolphin_count):
        node_to_id[dolphin_graph_node_list[i]] = i
    print node_to_id
    dolphin_graph_adjacency_mat = np.zeros((dolphin_count, dolphin_count))
    for i in range(dolphin_graph_edge_count):
        src_dolphin_id = node_to_id[dolphin_graph_edge_list[i][0]]
        dest_dolphin_id = node_to_id[dolphin_graph_edge_list[i][1]]
        dolphin_graph_adjacency_mat[src_dolphin_id][dest_dolphin_id] = 1
        dolphin_graph_adjacency_mat[dest_dolphin_id][src_dolphin_id] = 1

    print dolphin_graph_adjacency_mat
    print np.sum(dolphin_graph_adjacency_mat)

    dolphin_graph_laplacian_mat = csgraph.laplacian(dolphin_graph_adjacency_mat)
    # print dolphin_graph_laplacian_mat

    # print np.sum(dolphin_graph_adjacency_mat[61])
    eigen_values, eigen_vectors = np.linalg.eigh(dolphin_graph_laplacian_mat)
    print eigen_values
    print eigen_vectors[0]
