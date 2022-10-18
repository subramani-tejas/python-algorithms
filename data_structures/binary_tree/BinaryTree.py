from typing import overload


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"


class BinaryTree(object):
    def __init__(self, root: Node = None):
        # self.root = Node(root)
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is not None:
            # if not empty tree
            current = self.root
            while current:
                # moving left
                if new_node.value < current.value:
                    if not current.left:
                        current.left = new_node
                        return
                    else:
                        current = current.left
                # moving right
                elif new_node.value > current.value:
                    if not current.right:
                        current.right = new_node
                        return
                    else:
                        current = current.right
        else:
            self.root = new_node
            return

    def search(self, find_val):
        if self.root is None:
            return False

        current = self.root
        while current:
            if find_val == current.value:
                return True
            elif find_val < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def traverse_pre_order(self, root):
        # if not root.left and not root.right:
        #     print(root.value, end=", ")
        #     return

        if not root:
            return

        print(root.value, end=", ")
        self.traverse_pre_order(root=root.left)
        self.traverse_pre_order(root=root.right)
        return

    # tree height = root height
    def get_tree_height(self, root):
        if root.left is None and root.right is None:
            return 0
        return 1 + max(self.get_tree_height(root.left), self.get_tree_height(root.right))

    def get_nodes_at_k(self, root, k):
        if not root:
            return
        if k == 0:
            print(root.value, end=", ")
        self.get_nodes_at_k(root.left, k - 1)
        self.get_nodes_at_k(root.right, k - 1)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        return traversal


# Set up tree
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

t = BinaryTree()
t.insert(7)
t.insert(4)
t.insert(9)
t.insert(1)
t.insert(6)
t.insert(8)
t.insert(10)

print(t.search(12))

print("Pre-order traversal: ")
t.traverse_pre_order(t.root)

print(f"\nheight of tree: {t.get_tree_height(t.root)}")

print("Node at distance k: ")
t.get_nodes_at_k(t.root, 1)

print()
print("end")
