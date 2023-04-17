from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.min = self

    def __repr__(self):
        return f"Node({self.data})"


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, value):
        node = self.root
        parent = None
        while node:
            if value == node.data:
                return node, parent, True
            parent = node
            if value < node.data:
                node = node.left
            else:
                node = node.right
        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        node, parent, fl_find = self.__find(obj.data)

        if not fl_find and node:
            if obj.data < node.data:
                node.left = obj
            else:
                node.right = obj
            while node:
                if node.left and node.left.min.data < node.min.data:
                    node.min = node.left.min
                if node.right and node.right.min.data < node.min.data:
                    node.min = node.right.min
                node = parent
                parent = node.min if node else None

        return obj

    def show_tree(self):
        def gen(node):
            if node:
                yield from gen(node.left)
                yield node.data
                yield from gen(node.right)

        print(*gen(self.root))

    def del_node(self, key):
        node, parent, fl_find = self.__find(key)

        if not fl_find:
            return None

        if node.left is None or node.right is None:
            child = node.left or node.right
            if parent is None:
                self.root = child
            elif parent.left is node:
                parent.left = child
            else:
                parent.right = child
        else:
            min_node = node.right.min
            node.data = min_node.data
            self.del_node(min_node.data)

        while parent:
            if parent.left and parent.left.min.data < parent.min.data:
                parent.min = parent.left.min
            if parent.right and parent.right.min.data < parent.min.data:
                parent.min = parent.right.min
            node = parent
            parent = node.min if node else None

    def show_wide_tree(self):
        if self.root is None:
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not queue:
                print()


v = [20, 5, 24, 2, 16, 11, 21]

t = Tree()
for x in v:
    t.append(Node(x))
t.del_node(24)
t.show_wide_tree()
t.show_tree()
