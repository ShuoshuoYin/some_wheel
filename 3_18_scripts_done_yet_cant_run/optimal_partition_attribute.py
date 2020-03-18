# coding: utf-8

# this for selecting an attribute to be the partition attribute
# using A as the attributes' list, and D as the parent data set

import math

A = ['color', 'root', 'knock', 'texture', 'navel', 'touch']
V = {'color': ('����', '�ں�', 'ǳ��'), 
        'root': ('����', '����', 'Ӳͦ'),
        'knock': ('���', '����', '����'),
        'texture': ('����', '�Ժ�', 'ģ��'),
        'navel': ('����', '�԰�', 'ƽ̹'),
        'touch': ('Ӳ��', '��ճ')}

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

# ��Ϣ�� information entropy
def Ent(D):
    p1 = goodNum(D)/len(D)
    p2 = badNum(D)/len(D)
    return -(p1*math.log(p1, 2) + p2*math.log(p2, 2))

# ���ֽ�����õ�һ��list
def devide(D, a):
    Dv = []
    for v in V[a]:
        l = []
        for d in D:
            if d[a] == v:
                l.append(d)
        Dv.append(l)
    return Dv

# ��Ϣ���� information gain
def Gain(D, a):
    Dv = divide(D, a)
    tmp = 0
    for dv in Dv:
        tmp += len(dv)/len(D)*Ent(dv)
    return Ent(D)-tmp

# ����ֵ����a�Ĺ���ֵ intrinstic value 
def IV(D, a):
    Dv = divide(D, a)
    tmp = 0
    for dv in Dv:
        ratio = len(dv)/len(D)
        tmp += ratio*log(ratio, 2) 
    return -tmp

# ������ gain ratio
def Gain_ratio(D, a):
    return Gain(D, a)/IV(a)

"""
Ҳ����ʹ�û���ָ�����֣��뱾�ű�����Ϣ���桢�����ʷ������⻥��
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
    
# �������ϵĺ�����ȷ��һ���ӿ�
def NextAttribute(D, A):
    # ʹ����Ϣ�����������
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
    
    # ʹ�û���ָ��
    """
    gini_of_attributes = {}
    for a in A:
        gini_of_attributes[a] = Gini_index(D, a)
    return min(gini_of_attributes, key=lambda a: gini_of_attributes[a])
    """



