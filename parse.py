class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def build_tree(lines):
    root = None
    node_stack = []
    depth_stack = []

    for line in lines:
        # Determine the node depth and name
        depth = 0
        while line[depth] == ' ':
            depth += 1
        name = line.strip()

        # Create the new node
        node = TreeNode(name)

        # Add the node to the tree
        if depth == 0:
            root = node
        else:
            while len(node_stack) > depth - 1:
                node_stack.pop()
                depth_stack.pop()
            node_stack[-1].children.append(node)
        node_stack.append(node)
        depth_stack.append(depth)

    return root

# Example usage
text = """Node1
  Node2
    Node3
  Node4
    Node5
      Node6"""

lines = text.strip().split('\n')
root = build_tree(lines)

# Print the tree for verification
def print_tree(node, depth=0):
    print(' ' * depth + node.name)
    for child in node.children:
        print_tree(child, depth + 2)

print_tree(root)


def print_leaf_paths(node, path=[]):
    path.append(node.name)

    if not node.children:
        print(' -> '.join(path))
    else:
        for child in node.children:
            print_leaf_paths(child, path)

    path.pop()

# Example usage
text = """Node1
  Node2
    Node3
  Node4
    Node5
      Node6"""

lines = text.strip().split('\n')
root = build_tree(lines)

# Print all leaf paths of the tree
print_leaf_paths(root)
