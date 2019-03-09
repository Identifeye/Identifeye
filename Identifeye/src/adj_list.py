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
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

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

    # Function to print the graph (in adj list format)
    def print_graph(self):
        for i in range(self.V):

            # get current node
            temp = self.graph[i]

            # if no links skip
            if(temp == None):
                continue

            print("Adjacency list of vertex {}\n head".format(i), end="")

            while temp:
                print(F" -> Node Position = {temp.vertex} : weight = {round(temp.weight,3)}", end="")
                temp = temp.next
            print(" \n")

    # Function to print the graph (in the given data format)
    def print_data_matches(self, NodeArray):
        for i in range(self.V):

            # get current adjancey list node
            temp = self.graph[i]

            # if no links skip
            if (temp == None):
                continue

            # get current data point
            current_data = NodeArray[i]

            print("Account Name {}\n".format(current_data[0]), end="")

            while temp:

                connected_to = NodeArray[temp.vertex]
                print(F" -> Connected To: = {connected_to[0]} with a confidence of {round((temp.weight*100), 1)}%", end="\n")
                temp = temp.next
            print(" \n")


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


# goes through and adds edges to adjancey list
def add_edges(NodeArray, graph):
    for i in range(len(NodeArray)):
        for j in range(i + 1, len(NodeArray)):
            # get weight of each node with others
            w = calculate_weights(NodeArray[i], NodeArray[j])

            if w >= (2 / 7):
                graph.add_edge(i, j, w)

    print()


if __name__ == "__main__":
    NodeArray = [["hello_gator", "Bob", "127.1.0.1", 56897, "US", True, 105],
                 ["what_account", "Jason", "265.2.0.2", 63541, "Canada", False, 212],
                 ["jello_pie", "Jason", "315.6.4.7", 88541, "Mexico", False, 105],
                 ["jason_565", "Rambo", "127.1.0.1", 11115, "US", False, 2],
                 ["not_hello_gator", "Bob", "127.1.0.1", 56897, "US", False, 5],
                 ["random", "Ryan", "666.3.2.1", 78912, "Mexico", False, 88],
                 ["jello_man", "Simba", "111.5.6.0", 63541, "Canada", False, 12]]

    V = len(NodeArray)
    graph = Graph(V)
    add_edges(NodeArray, graph)

graph.print_data_matches(NodeArray)