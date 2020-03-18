# coding: utf-8

# well, this is my first ML program, gangbalu!!!
# ciga, decision tree

from tree import TreeNode

def NextAttribute(D, A):
    pass
 
"""
calculation some data, then select a new attribute to do division
return attribute name from A
"""

def goodMore(D):
    goodNum = 0
    badNum = 0
    for d in D:
        if d['label'] == 'good':
            goodNum += 1
        elif d['label'] == 'bad':
            badNum += 1
        else:
            print('error spelling of label')
    if goodNum >= badNum:
        return True
    else:
        return False

# every time, pass a parent and its data set as the superset D, which is going to
# be divided
def TreeGenerate(parent, D, A):
    attribute = NextAttribute(D, A)
    parent.setAttribute(attribute)
    # step 1, all have the same label, or not
    labels = [d['label'] for d in D]
    if 'good' not in labels:
        parent.setLeaf()
        parent.setLabel('bad')  # only label can be set, because attr already init
        return 'we all bad'
    elif 'bad' not in labels:
        parent.setLeaf()
        parent.setLabel('good')
        return 'we all good'
    else:
        pass

    #step 2, A is empty, or every child of parent has the same value of attribute
    same = True
    for i in range(len(D)-1):
        if D[i] != D[i+1]:
            same = False
            break
    if A == [] or same:
        parent.setLeaf()
        if goodMore(D):
            parent.setLabel('good')
        else:
            parent.setLabel('bad')
    else:
        pass

    #step 3, not above situation, start to divide
    for value in V[attribute]:
        child = TreeNode(False, value, None)
        parent.addChild(child)
        Dv = []
        for d in D:
            if d[attribute] == value:
                Dv.append(d)
        if Dv == []:
            parent.setLeaf()
            if goodMore(D):
                parent.setLabel('good')
            else:
                parent.setLabel('bad')
            return 'Dv is empty'
        # in step 3, Dv is not empty
        A.remove(attribute)
        TreeGenerate(child, Dv, A)

def test_new_sample(new_sample):
    #new sample is a dictionary too
    pass
# return label, good, or bad




if __name__ == "__main__":

    A = ['color', 'root', 'knock', 'texture', 'navel', 'touch']
    V = {'color': ('ÇàÂÌ', 'ÎÚºÚ', 'Ç³°×'), 
            'root': ('òéËõ', 'ÉÔòé', 'Ó²Í¦'),
            'knock': ('Çå´à', '×ÇÏì', '³ÁÃÆ'),
            'texture': ('ÇåÎú', 'ÉÔºý', 'Ä£ºý'),
            'navel': ('°¼ÏÝ', 'ÉÔ°¼', 'Æ½Ì¹'),
            'touch': ('Ó²»¬', 'ÈíÕ³')}
    #     ÑÕÉ«  £¬ ¸ùµÙ£¬  ÇÃ»÷Éù£¬ ÎÆÀí£¬     Æê²¿£¬   ´¥¸Ð
    # etc. many xi and yi, and xi has many dimentions
    # or D = [(x1, y1), (x2, y2), ......, (xn, yn)]
    import extraction
    data = extraction.extract_ciga('./data.csv')
    # for one in data:
    #  print(one)

    # root, no value, not determine attribute to divide 
    decision_tree_root = TreeNode(False, None, None) 

    TreeGenerate(decision_tree_root, D, A)


























