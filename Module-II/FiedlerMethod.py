import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


class FiedlerMethod:

    def __init__(self, graph):
        self._graph = graph
        self._nodes = list(self._graph.nodes())
        self._edges = list(self._graph.edges())

    def draw_graph_with_community_structure(self, cluster1, cluster2):
        pos = nx.spring_layout(self._graph)
        label_dict = {}
        for i in range(len(self._nodes)):
            label_dict[self._nodes[i]] = self._nodes[i]
        # for i in range(len(self._nodes)):
        #     if self._nodes[i] in cluster1:
        #         pos[self._nodes[i]][1] += 2
        nx.draw_networkx_nodes(self._graph, pos, cluster1, node_color='r', node_shape='o', node_size=100)
        nx.draw_networkx_nodes(self._graph, pos, cluster2, node_color='g', node_shape='s', node_size=100)
        # nx.draw(dolphin_graph, with_labels=True, node_color=node_colors.ravel())
        nx.draw_networkx_edges(self._graph, pos, alpha=0.8)
        nx.draw_networkx_labels(self._graph, pos, labels=label_dict, font_size=5)
        # plt.show()
        plt.savefig('community_plots/community_fiedler.pdf')

    def find_communities(self):
        dolphin_count = len(self._nodes)
        fiedler_vector = nx.fiedler_vector(self._graph)
        X_data = np.array(fiedler_vector).reshape((len(fiedler_vector), 1))
        kmeans = KMeans(n_clusters=2).fit(X_data)
        negative_cluster = [i for i in range(len(kmeans.labels_)) if kmeans.labels_[i] == 0]
        positive_cluster = [i for i in range(len(kmeans.labels_)) if kmeans.labels_[i] == 1]
        assert len(negative_cluster) + len(positive_cluster) == dolphin_count
        positive_dolphins = [self._nodes[i] for i in positive_cluster]
        negative_dolphins = [self._nodes[i] for i in negative_cluster]
        return positive_dolphins, negative_dolphins
