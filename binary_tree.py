class Node:
    def __init__(self, parent=None, value=0):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = parent


class BinarySearchTree:
    counter = 0

    def __init__(self, preorder_list):
        self.index = -1
        self.check = 0
        self.init_list = preorder_list
        self.rooot = None
        self.pre_order()
        self.tree = []
        self.inorder_tree_walk(self.rooot)
        self.check +=1
        self.tree = sorted(self.tree)
        self.inorder_tree_walk(self.rooot)

    def pre_order(self, parent=None):
        self.index += 1
        if self.init_list[self.index] == 0:
            return None
        node = Node(parent, self.init_list[self.index])
        if parent is None:
            self.rooot = node
        node.left_child = self.pre_order(node)
        node.right_child = self.pre_order(node)
        return node

    def inorder_tree_walk(self, x):

        if x is not None:

            self.inorder_tree_walk(x.left_child)
            if self.check:
                x.value = self.tree[self.counter]
                self.counter += 1
            else:
                self.tree.append(x.value)
            self.inorder_tree_walk(x.right_child)

    def tree_search(self, x, k):
        if x is None or k == x.value:
            return x
        elif k < x.value:
            return self.tree_search(x.left_child, k)
        return self.tree_search(x.right_child, k)

    def root(self):
        return self.rooot

    def parent(self, k):
        return k.parent

    def left(self, k):
        return k.left_child

    def right(self, k):
        return k.right_child

    def key(self, k):
        return k.value

    def find_sum(self, s):
        path = []
        for i in self.tree:
            start = self.tree_search(self.rooot, i)
            temp_sum = start.value
            temp_path = [start]
            while temp_sum < s:
                if start.value != self.rooot.value:
                    start = start.parent
                    temp_sum += start.value
                    temp_path.append(start)
                else:
                    break
            if temp_sum == s:
                to_rev = []
                for j in range(len(temp_path)):
                    to_rev.append(temp_path.pop())
                path.append(to_rev)
        return path
