# Import deque from collections module, which is a double-ended queue that supports efficient insertion and removal at both ends
from collections import deque

# Define a function that takes a graph (represented as an adjacency list) and a starting node as parameters
def bfs(graph, start):
    # Create an empty queue and append the start node to it
    queue = deque()
    queue.append(start)
    # Create an empty set or list to store the visited nodes
    visited = set()
    # Loop until the queue is empty
    while queue:
        # Pop the first node from the queue
        node = queue.popleft()
        # If the node has already been visited, skip it
        if node in visited:
            continue
        # Otherwise, mark the node as visited and print it
        visited.add(node)
        print(node)
        # Loop through the neighbors of the node
        for neighbor in graph[node]:
            # If the neighbor has not been visited, append it to the queue
            if neighbor not in visited:
                queue.append(neighbor)

# Create a sample graph as a dictionary of lists
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
}

# Call the bfs function with the graph and a start node
bfs(graph, 0)
