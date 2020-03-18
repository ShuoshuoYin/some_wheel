# coding: utf-8

# this for selecting an attribute to be the partition attribute
# using A as the attributes' list, and D as the parent data set

import math

A = ['color', 'root', 'knock', 'texture', 'navel', 'touch']
V = {'color': ('青绿', '乌黑', '浅白'), 
        'root': ('蜷缩', '稍蜷', '硬挺'),
        'knock': ('清脆', '浊响', '沉闷'),
        'texture': ('清晰', '稍糊', '模糊'),
        'navel': ('凹陷', '稍凹', '平坦'),
        'touch': ('硬滑', '软粘')}

# good num
def goodNum(D):
    num = 0
    for d in D:
        if d['label'] == 'good':
            num += 1
    return num

# bad num
def badNum(D):
    num = 0
    for d in D:
        if d['label'] == 'bad':
            num += 1
    return num

# 信息熵 information entropy
def Ent(D):
    p1 = goodNum(D)/len(D)
    p2 = badNum(D)/len(D)
    return -(p1*math.log(p1, 2) + p2*math.log(p2, 2))

# 划分结果，得到一个list
def devide(D, a):
    Dv = []
    for v in V[a]:
        l = []
        for d in D:
            if d[a] == v:
                l.append(d)
        Dv.append(l)
    return Dv

# 信息增益 information gain
def Gain(D, a):
    Dv = divide(D, a)
    tmp = 0
    for dv in Dv:
        tmp += len(dv)/len(D)*Ent(dv)
    return Ent(D)-tmp

# 固有值属性a的固有值 intrinstic value 
def IV(D, a):
    Dv = divide(D, a)
    tmp = 0
    for dv in Dv:
        ratio = len(dv)/len(D)
        tmp += ratio*log(ratio, 2) 
    return -tmp

# 增益率 gain ratio
def Gain_ratio(D, a):
    return Gain(D, a)/IV(a)

"""
也可以使用基尼指数划分，与本脚本的信息增益、增益率方法互斥互斥
"""
def Gini(D):
    p1 = goodNum(D)/len(D)
    p2 = badNum(D)/len(D)
    return 1 - p1**2 - p2**2

def Gini_index(D, a):
    Dv = divide(D, a)
    tmp = 0
    for dv in Dv:
        tmp += len(dv)/len(D)*Gini(dv)
    return tmp
"""
end of Gini method
"""
    
# 根据以上的函数，确定一个接口
def NextAttribute(D, A):
    # 使用信息增益和增益率
    gain_of_attributes = {}
    for a in A:
        gain_of_attributes[a] = Gain(D, a)
    average = sum(gain_of_attributes.values())/len(A)
    max_ratio = -1
    result = None
    for a in gain_of_attributes:
        if gain_of_attributes[a] >= average:
            gain_ratio = Gain_ratio(D, a)
            if gain_ratio > max_ratio:
                max_ratio = gain_ratio
                result = a
    return result
    
    # 使用基尼指数
    """
    gini_of_attributes = {}
    for a in A:
        gini_of_attributes[a] = Gini_index(D, a)
    return min(gini_of_attributes, key=lambda a: gini_of_attributes[a])
    """



