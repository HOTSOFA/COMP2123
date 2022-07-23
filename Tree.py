from Node import Node

"""
Tree
----------

This class represents the Binary Tree used to model our baby mobile. 

Each Tree consists of the following properties:
    - root: The root of the Tree

The class also supports the following functions:
    - put(node, child, left_child): Adds child to the given node as the left or right child depending on the value of left_child
    - move_subtree(node_a, node_b, left_child): Move node_a to the left or right child of node_b depending on the value of left_child
    - find_max_imbalance(): Finds the node with the maximum imbalance in the tree

Your task is to complete the following functions which are marked by the TODO comment.
Note that your modifications to the structure of the tree should be correctly updated in the underlying Node class!
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Tree():
    # These are the defined properties as described above
    root: Node

    def __init__(self, root: Node = None) -> None:
        """
        The constructor for the Tree class.
        :param root: The root node of the Tree.
        """
        self.root = root
        self.ls = []

    def put(self, node: Node, child: Node, left_child: bool) -> None:
        """
        Adds the given child to the given node as the left or right child depending on the value of left_child.
        If a node already has a child at the indicated position, this function should do nothing.
        You are guranteed that the given node is not already part of the tree
        :param node: The node to add the child to.
        :param child: The child to add to the node.
        :param left_child: True if the child should be added to the left child, False otherwise.
        """
        if node is None or child is None or left_child is None:
            return
        if left_child:
            if node.left_child is None:
                node.add_left_child(child)

        if not left_child:
            if node.right_child is None:
                node.add_right_child(child)

        # TODO Add the child to the node as the left or right child depending on the value of left_child

    def move_subtree(self, node_a: Node, node_b: Node, left_child: bool) -> None:
        """
        Moves the subtree rooted at node_a to the left or right child of node_b depending on the value of left_child.
        If node_b already has a child at the indicated position, this function should do nothing
        You can safely assume that node_b is not descendent of node_a.
        :param node_a: The root of the subtree to move.
        :param node_b: The node to add the subtree to.
        :param left_child: True if the subtree should be added to the left child, False otherwise.
        """
        if node_a is None or node_b is None or left_child is None:
            return

        if left_child:
            if node_b.left_child is None:
                node_a.parent.delete_child(node_a)
                node_b.add_left_child(node_a)

        elif not left_child:
            if node_b.right_child is None:
                node_a.parent.delete_child(node_a)
                node_b.add_right_child(node_a)




        # TODO Move the subtree rooted at node_a to the left or right child of node_b

    def fill_imbalance_stack(self, node: 'Node'):
        self.ls.append(node.get_imbalance())
        if node.left_child is not None:
            self.fill_imbalance_stack(node.left_child)
        if node.right_child is not None:
            self.fill_imbalance_stack(node.right_child)

    def find_max_imbalance(self) -> int:
        """
        Finds the node with the maximum imbalance in the tree.
        :return: The node with the maximum imbalance.
        """
        if self.root is None:
            return
        self.fill_imbalance_stack(self.root)
        return max(self.ls)
        # TODO Find the node with the maximum imbalance


A = Node(5)
tree = Tree(A)

B = Node(10)
C = Node(2)
D = Node(8)

tree.put(A, C, True)
tree.put(A, D, False)
tree.put(C, B, True)

"""
        Set up the tree to be used throughout the test
        This is the tree given in the sample
        A(5)
        /   \
        C(2) D(8)
        /
        B(10)
"""

