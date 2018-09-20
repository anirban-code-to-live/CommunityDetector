import networkx as nx
import community
import numpy as np
from matplotlib import pyplot as plt


class LouvainMethod:

    def __init__(self, graph):
        self._graph = graph
        self._nodes = list(self._graph.nodes())
        self._edges = list(self._graph.edges())

    def find_communities(self):
        partition = community.best_partition(self._graph, randomize=True)
        number_of_communities = max(partition.values()) + 1
        partition_list = []
        for i in range(number_of_communities):
            partition_list_i = [item for item in partition.items() if item[1] == i]
            partition_list.append(partition_list_i)

        partition_sizes = [len(partition) for partition in partition_list]
        # print(partition_sizes)
        top_two_partition_indices = np.argsort(partition_sizes)[-2:]
        # print(top_two_partition_indices)
        for i in range(number_of_communities):
            cluster_number1 = partition_list[top_two_partition_indices[0]][0][1]
            # print(cluster_number1)
            cluster_number2 = partition_list[top_two_partition_indices[1]][0][1]
            # print(cluster_number2)
            if i not in top_two_partition_indices:
                partition_to_be_merged1 = partition_list[i]
                for j in range(len(partition_to_be_merged1)):
                    item = list(partition_to_be_merged1[j])
                    item[1] = cluster_number1
                    partition_to_be_merged1[j] = tuple(item)
                # print(partition_to_be_merged)
                merged_partition1 = partition_to_be_merged1 + partition_list[cluster_number1]
                total_partition1 = merged_partition1 + partition_list[cluster_number2]
                # print(len(total_partition))
                for k in range(number_of_communities):
                    if k != i and k not in top_two_partition_indices:
                        total_partition1 += partition_list[k]
                # print(dict(total_partition1))
                modularity1 = community.modularity(dict(total_partition1), self._graph)
                # print(modularity1)

                partition_to_be_merged2 = partition_list[i]
                for j in range(len(partition_to_be_merged2)):
                    item = list(partition_to_be_merged2[j])
                    item[1] = cluster_number2
                    partition_to_be_merged2[j] = tuple(item)
                # print(partition_to_be_merged)
                merged_partition2 = partition_to_be_merged2 + partition_list[cluster_number2]
                total_partition2 = merged_partition2 + partition_list[cluster_number1]
                # print(len(total_partition))
                for k in range(number_of_communities):
                    if k != i and k not in top_two_partition_indices:
                        total_partition2 += partition_list[k]
                # print(dict(total_partition2))
                modularity2 = community.modularity(dict(total_partition2), self._graph)
                # print(modularity2)

                if modularity1 > modularity2:
                    partition_list[i] = partition_to_be_merged1
                else:
                    partition_list[i] = partition_to_be_merged2

                # print(partition_list)

        final_list = []
        for i in range(len(partition_list)):
            partition_i = partition_list[i]
            for j in range(len(partition_i)):
                final_list.append(partition_i[j])
        # print(dict(final_list))
        # print(list(set(dict(final_list).values())))
        positive_cluster_index = list(set(dict(final_list).values()))[0]
        negative_cluster_index = list(set(dict(final_list).values()))[1]
        # print(positive_cluster_index)
        # print(negative_cluster_index)
        positive_cluster = []
        negative_cluster = []
        for i in range(len(final_list)):
            cluster_index = final_list[i][1]
            if cluster_index == positive_cluster_index:
                positive_cluster.append(final_list[i][0])
            else:
                negative_cluster.append(final_list[i][0])
        return positive_cluster, negative_cluster

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
        plt.savefig('community_plots/community_louvain.pdf')
