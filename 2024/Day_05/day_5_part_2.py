from day_5_part_1 import data, parse_input


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

def correct_order(update, graph):
    subgraph = {node: [neighbor for neighbor in graph.get(node, []) if neighbor in update]
                for node in update}
    return topological_sort(subgraph)

def find_middle_sum_of_corrected(graph, updates):
    incorrect_updates = []
    for update in updates:
        if not validate_update(update, graph):
            incorrect_updates.append(update)
    
    total = 0
    for update in incorrect_updates:
        corrected = correct_order(update, graph)
        middle = len(corrected) // 2
        total += corrected[middle]
    return total

graph, updates = parse_input(data)
result = find_middle_sum_of_corrected(graph, updates)
print(result)