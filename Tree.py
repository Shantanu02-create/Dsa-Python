#A Tree is a non-linear data structure that organizes data hierarchically. It consists of nodes, where each node contains a value and references to its child nodes. The topmost node is called the root, and nodes without children are called leaves. Trees are used in various applications such as representing hierarchical relationships, organizing data for efficient searching and sorting, and implementing abstract data types like binary search trees and heaps.       
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None