from difflib import SequenceMatcher

"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

# weights arreay by value
weights = [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7]


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data, weight):
        self.vertex = data
        self.weight = weight
        self.next = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self):
        self.graph = []

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest, weight):
        # Adding the node to the source node
        node = AdjNode(dest, weight)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src, weight)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        i = 0
        for g in self.graph:
            printf("Adjacency list of vertex {i}\n head".format(i), end="")
            temp = g
            while temp:
                # print(" -> {}".format(temp.vertex), end="")
                #print(F" -> Node Position = {temp.vertex} : weight = {temp.weight}", end="")
                temp = temp.next
            print(" \n")
            i = i + 1

    # goes through and adds edges to adjancey list
    def add_edges(self, Nodes):
        for i in range(len(NodeArray)):
            for j in range(i + 1, len(NodeArray)):
                # get weight of each node with others
                w = calculate_weights(NodeArray[i], NodeArray[j])

                if w >= (2 / 7):
                    self.add_edge(i, j, w)


# calculate the connected-ness of each node
def calculate_weights(node1, node2):
    w = 0
    # calculate weight - does not include play time or is banned

    # Account and Character name
    for i in range(0, 2):
        if node1[i] == node2[i]:
            w += weights[i]
        else:
            match = SequenceMatcher(None, node1[i], node2[i]).find_longest_match(0, len(node1[i]), 0, len(node2[i]))
            if match.size >= 3:
                w += weights[i] * min(weights[i], weights[i] * match.size / 10)

    # IP, UUID, Location
    for i in range(2, 5):
        if node1[i] == node2[i]:
            w += weights[i]

    return w