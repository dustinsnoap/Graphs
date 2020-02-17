import sys
sys.path.insert(0, '../graph')
from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for vertex in ancestors:
        #create graph in reverse
        graph.add_vertex(vertex[0])
        graph.add_vertex(vertex[1])
        graph.add_edge(vertex[1], vertex[0])

    if not graph.get_neighbors(starting_node): return -1

    queue = Queue()
    queue.enqueue(starting_node)
    paths = dict()
    paths[starting_node] = [starting_node]
    while queue.size() > 0:
        current_node = queue.dequeue()
        for node in graph.get_neighbors(current_node):
            paths[node] = paths[current_node] + [node]
            queue.enqueue(node)

    oldest = -1
    distance = 0
    for path in paths:
        if len(paths[path]) > distance or len(paths[path]) == distance and path < oldest:
            oldest = path
            distance = len(paths[path])

    return oldest


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)