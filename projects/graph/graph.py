"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 in self.vertices:
            print(f'Hey bruh, you need to add {v2} first.')
        else:
            print(f'Hey bruh, you need to add {v1} first.')

    def get_neighbors(self, vertex_id):
        if vertex_id not in self.vertices:
            print('Come at me with a real vertex bruh!')
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            if current_vertex not in visited:
                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    queue.enqueue(vertex)
        print(visited)

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    stack.push(vertex)
        print(visited)        

    def dft_recursive(self, starting_vertex, visited=set()):
        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                visited.add(vertex)
                self.dft_recursive(vertex, visited)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        paths = dict()
        paths[starting_vertex] = [starting_vertex]
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            #if destination is connected, return it
            if destination_vertex in self.get_neighbors(current_vertex):
                return paths[current_vertex] + [destination_vertex]
            #else keep updating paths until it's found
            for vertex in self.get_neighbors(current_vertex):
                if vertex not in paths:
                    paths[vertex] = paths[current_vertex] + [vertex]
                    queue.enqueue(vertex)

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        paths = dict()
        paths[starting_vertex] = [starting_vertex]
        while stack.size() > 0:
            current_vertex = stack.pop()
            for vertex in self.get_neighbors(current_vertex):
                current_path = paths[current_vertex] + [vertex]
                #if path for this vertex exists and its current path greater than or equal one already found, ignore it
                #only 'vertex not in paths' is required to give an optimal solution for this exact graph
                if vertex in paths and len(current_path) < len(paths[vertex]) or vertex not in paths:
                    paths[vertex] = current_path
                    stack.push(vertex)
        return paths[destination_vertex]

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        if starting_vertex in visited: return None
        if starting_vertex == destination_vertex: return [starting_vertex]
        visited.add(starting_vertex)
        for vertex in self.get_neighbors(starting_vertex):
            path = self.dfs_recursive(vertex, destination_vertex, visited)
            if path is not None: return [starting_vertex] + path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))