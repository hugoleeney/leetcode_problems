"""
133. Clone Graph
Difficulty: medium

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]


Constraints:

1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

"""


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return f"{self.val}"

    def __eq__(self, other):
        if self.val != other.val:
            return False
        else:
            for a,b in zip(self.neighbors, other.neighbors):
                if a.val != b.val:
                    return False
            return True



class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        new = Node(node.val)
        self.visited[node.val] = new

        for n in node.neighbors:
            if n.val in self.visited:
                new.neighbors.append(self.visited[n.val])
            else:
                new.neighbors.append(self.cloneGraph(n))

        return new


def list_to_graph(a):
    nodes = {}
    for idx, ele in enumerate(a):
        idx = idx+1
        n = nodes.get(idx, Node(idx))
        nodes[idx] = n
        for i in ele:
            if i in nodes:
                n.neighbors.append(nodes[i])
            else:
                neigh = Node(i)
                nodes[i] = neigh
                n.neighbors.append(neigh)
    return nodes[1]


def graph_to_list_of_nodes(g):
    nodes = {}
    stack = [g]
    while stack:
        node = stack.pop()
        if node.val not in nodes:
            nodes[node.val] = node
            for n in node.neighbors:
                stack.append(n)
    return sorted(nodes.values(), key=lambda x: x.val)



if __name__ == "__main__":
    tc = list_to_graph([[2,4],[1,3],[2,4],[1,3]])
    s = Solution()
    clone = s.cloneGraph(tc)

    assert graph_to_list_of_nodes(clone) == graph_to_list_of_nodes(tc)