from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def build_graph(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                    triangle = tuple(sorted([node, neighbor1, neighbor2]))
                    triangles.add(triangle)
    return triangles

def filter_triangles_with_t(triangles):
    return [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

def main(file_path):
    connections = parse_input(file_path)
    graph = build_graph(connections)
    triangles = find_triangles(graph)
    triangles_with_t = filter_triangles_with_t(triangles)
    print("Number of triangles with at least one 't'-starting node:", len(triangles_with_t))

if __name__ == "__main__":
    main("input.txt")
