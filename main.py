
### 2. `main.py`
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n_len` nodes, numbered from `0` to `n_len-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    # Your implementation goes here
    # Get topological order of the nodes
    topo_order = topological_sort(graph)
    
    # Compute the longest path using the topological order
    return calculate_longest_path(graph, topo_order)
    pass

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    n_len = len(graph)
    node_visited = [False] * n_len
    topo_order = []

    def depth_first_search(node):
        node_visited[node] = True
        for neighbor, _ in graph[node]:
            if not node_visited[neighbor]:
                depth_first_search(neighbor)
        topo_order.append(node)

    for i in range(n_len):
        if not node_visited[i]:
            depth_first_search(i)
            
    return topo_order[::-1]
    pass

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    n_len = len(graph)
    distance = [-float('inf')] * n_len

    for node in topo_order:
        if distance[node] == -float('inf'):
            distance[node] = 0
        # Use a set to store unique edges
        seen_edges = set()
        for neighbor, weight in graph[node]:
            if (node, neighbor) not in seen_edges:
                seen_edges.add((node, neighbor))
                if distance[node] + weight > distance[neighbor]:
                    distance[neighbor] = distance[node] + weight

    return max(distance)
    pass



# # Example usage and test cases
# if __name__ == "__main__":
#     graph4 = [
#         [(1, 1), (2, 1)],
#         [(3, 1)],
#         [(3, 1)],
#         []
#     ]
#     print(longest_path(graph4))  # Output: 2
