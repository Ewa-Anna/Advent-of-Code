puzzle = "input.txt"

with open(puzzle, "r") as file:
    data = file.read()

def parse_input(data):
    rules, updates = data.split("\n\n")
    graph = {}
    for rule in rules.splitlines():
        X, Y = map(int, rule.split("|"))
        graph.setdefault(X, []).append(Y)
    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]
    return graph, updates

def validate_update(update, graph):
    subgraph = {node: [neighbor for neighbor in graph.get(node, []) if neighbor in update]
                for node in update}
    
    sorted_order = topological_sort(subgraph)
    if not sorted_order:
        return False  
    
    return update == sorted_order

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1
    
    queue = [node for node in graph if in_degree[node] == 0]
    sorted_order = []
    
    while queue:
        current = queue.pop(0)
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_order) != len(graph):
        return None  
    return sorted_order

def find_middle_sum(graph, updates):
    total = 0
    for update in updates:
        if validate_update(update, graph):
            middle = len(update) // 2
            total += update[middle]
    return total


graph, updates = parse_input(data)
result = find_middle_sum(graph, updates)
print(result)
