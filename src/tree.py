'''
Created on 2 Nov 2015

@author: matt

Given: A positive integer n (n<=1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

Approach:

#get list of edges
#get list of nodes
# for each node_pair
    # find all clusters contained the nodes
        # if in no clusters, make new cluster
        # if in one cluster, add to cluster
        # if in two clusters, add to first and merge the clusters
        # if in >2, error
        
#edges needed = clusters -1

'''

from sys import argv, exit

def get_data(filepath):
    '''
    Extracts number of nodes and node pairs file at specified path
    '''
    with open(filepath, "r") as file:
        max_node = file.readline()
        node_pairs = []
        for line in file.readlines():
            node_pairs.append(line.strip().split(" "))
        assert max_node > 0, "Error, maximum node must be an integer >0"
        assert len(node_pairs) > 0, "Error: no nodes in input data"
        print max_node
        print node_pairs
    return max_node, node_pairs

def construct_tree(max_node, node_pairs):
    '''
    Constructs tree consisting of a list of clusters of linked nodes.

    Each cluster is a list of node pairs, or a single orphan node
    Output is the list of clusters
    '''
    clusters = []
    orphan_nodes = range(1, int(max_node)+1)

    for nodes in node_pairs:

        # Check each node is in valid range
        for node in nodes:
            assert 1 <= int(node) <= int(max_node), "Error, node %d outside specified range (1-%d)" % (int(node), int(max_node))

        # Nodes observed in a pair are not an orphans
        # Remove from the orphan list
        orphan_nodes = [x for x in orphan_nodes if str(x) not in nodes]

        # To record the index of existing clusters containing part of the node
        cluster_hits = []

        # Find clusters already containing the nodes
        for cluster_index, cluster in enumerate(clusters):
            for cluster_node in cluster:
                if (nodes[0] in cluster_node) or (nodes[1] in cluster_node)\
                and cluster_index not in cluster_hits:
                    cluster_hits.append(cluster_index)

        # Append each node to a cluster
        # Merge clusters if node spans 2 clusters

        # Add node to new cluster
        if len(set(cluster_hits)) == 0:
            clusters.append([nodes])

        # Append node to existing cluster
        elif len(set(cluster_hits)) == 1:
            clusters[cluster_hits[0]].append(nodes)

        # Merge clusters and add node to merged cluster
        elif len(set(cluster_hits)) == 2:
            clusters[cluster_hits[0]] += clusters[cluster_hits[-1]]
            clusters[cluster_hits[0]].append(nodes)
            del clusters[cluster_hits[-1]]  # [-1] = highest index of matches

        # If a node spans >2 clusters error, should already be merged
        else:
            print "Error, node spans >2 clusters, check input data!"
            print "Nodes", nodes
            print "Cluster hits:"
            for index in set(cluster_hits):
                print index, "\n", clusters[index]
            exit()

    # Make clusters for orphan nodes
    for node in orphan_nodes:
        clusters.append([[node]])

    for cluster in clusters:
        print cluster

    return clusters

def missing_edges(clusters):
    '''
    Calculates number of edges are needed to join clusters into tree
    '''

    required_edges = len(clusters) -1
    print "Edges needed: %d" % required_edges
    return required_edges

def write_results(results, filepath):
    with open(filepath+".results", "w") as output_file:
        output_file.write(str(results))

def main(filepath):
    max_node, node_pairs = get_data(argv[1])
    clusters = construct_tree(max_node, node_pairs)
    edges = missing_edges(clusters)
    write_results(edges, filepath)

if __name__ == "__main__":
    main(argv[1])