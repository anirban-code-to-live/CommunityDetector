import numpy as np
import networkx as nx
import community
from scipy.sparse import csgraph
import matplotlib
from matplotlib import pyplot as plt
import FiedlerMethod as fm
import LouvainMethod as lm


if __name__ == '__main__':
    print('Welcome to the world of bottlenose dolphins!!\n')
    dolphin_graph = nx.read_gml('../data/dolphins.gml')

    # Solution for part-II :: Using Fiedler Vector
    fiedler_method = fm.FiedlerMethod(dolphin_graph)
    positive_cluster_fiedler, negative_cluster_fiedler = fiedler_method.find_communities()
    fiedler_method.draw_graph_with_community_structure(positive_cluster_fiedler, negative_cluster_fiedler)
    print('Following are the two clusters obtained using Fielder Method')
    print('Cluster-1 ::: ')
    print(positive_cluster_fiedler)
    print('Cluster-2 ::: ')
    print(negative_cluster_fiedler)
    print('')

    # Solution for part-I :: Using Louvain Method
    louvain_method = lm.LouvainMethod(dolphin_graph)
    positive_cluster_louvain, negative_cluster_louvain = louvain_method.find_communities()
    louvain_method.draw_graph_with_community_structure(positive_cluster_louvain, negative_cluster_louvain)
    print('Following are the two clusters obtained using Louvain Method')
    print('Cluster-1 ::: ')
    print(positive_cluster_louvain)
    print('Cluster-2 ::: ')
    print(negative_cluster_louvain)