"""
For my first decision tree algorithm and first time to resolve a classification ques-
tion, I determine to write a tree as my data structure tool first.
"""

# using list, dictionary, tuple, or defining a new class, it's a question.
# so, it's important to determine how to use the tree, or what functions and operati-
# ons we want first.

# this file is just used as a module, an interface to tree structure
# examples are as follows

"""
from tree import TreeNode
root = TreeNode('leaf_or_not',
                'attribute_value',
                # for which divided into this node or set from parent node
                'class_label_name if leaf else attribute_name'
                # based on which we divide the D or parent set 
                )
for child in root.getChilds():  # or empty list - [] - if having no child
    print(child.type())
    print(child.label()) # or None if not leaf
    print(child.attribute()) # or None if leaf
    print(child.value())
    # value of the parent's attribute, according to which we divided. 

def getLabel(test_sample, node):
    if node.isLeaf():
        return node.getLabel()
    value = test_sample.get(node.getAttribute())
    child = node.getChild(value)
    getLabel(test_sample, child) 
"""

class TreeNode:
    structure = 'we are all from tree, I\'m very pi'

    def __init__(self, 
            leaf_or_not, 
            value_into_this_node,
            label_or_attribute_for_next_division):
        self.__leaf = leaf_or_not # using bool value
        self.__value = value_into_this_node
        self.__label = label_or_attribute_for_next_division
        self.__childs = []
    def isLeaf():
        return self.__leaf

    def isNotLeaf():
        return not self.__leaf

    def setLeaf():
        self.__leaf = True

    def getValue():
        return self.__value

    def getAttribute():
        return self.__label if not self.__leaf else None

    def getLabel():
        return self.__label if self.__leaf else None

    def setChilds(childs): # list of TreeNode
        self.__childs = childs

    def getChilds():
        return self.__childs

    def getChild(value):
        for child in self.__childs:
            if child.getValue() == value:
                return child
        return None
    
    def childNum():
        return len(self.__childs)

















