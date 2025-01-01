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

def bron_kerbosch(graph, r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return
    for node in list(p):
        bron_kerbosch(
            graph,
            r.union({node}),
            p.intersection(graph[node]),
            x.intersection(graph[node]),
            cliques
        )
        p.remove(node)
        x.add(node)

def find_largest_clique(graph):
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    largest_clique = max(cliques, key=len, default=[])
    return sorted(largest_clique)

def generate_password(clique):
    return ",".join(clique)

def main(file_path):
    connections = parse_input(file_path)
    graph = build_graph(connections)
    largest_clique = find_largest_clique(graph)
    password = generate_password(largest_clique)
    print("Password to get into the LAN party:", password)

if __name__ == "__main__":
    main("input.txt")
