
def dfs(node, graph, visited, stack):
    if node in stack:
        return True 
    if node in visited:
        return False

    visited.add(node)
    stack.add(node)

    for neighbor in graph.get(node, []):
        if dfs(neighbor, graph, visited, stack):
            return True

    stack.remove(node)
    return False

def has_cycle(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, set()):
                return True
    return False


def has_one_root(tree_map):
    visited = {}
    for vertex,neighbors in tree_map.items():
        for v in neighbors:
            if visited.get(v) == True:
                return False 
            visited[v] = True

    roots = [node for node in tree_map if node not in visited]
    return len(roots) == 1


def is_valid_git_tree(tree_map):
    if has_one_root(tree_map) and not has_cycle(tree_map):
        return True
    return False


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False