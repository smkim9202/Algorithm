# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:47:27 2021

@author: SMKIM
"""
'''
    트리만들기
    ___*     _ 2개  * 0개  _* 1개 i=0 
    __*_*    _ 1개  * 0개  _* 2개 i=1
    _*_*_*   _ 0개  * 0개  _* 3개 i=2
    *_*_*_*  _ 0개  * 1개  _* 3개 i=3
'''

#3단트리
h=3
for i in range(0,h):
    print(" " * 10,end="")
    print(" "*4,end="")
    if i==0:
        print(" " * (h-1) + "*")
    if i==(h-1):
        print("*" + " *" * (h-1))
    if i!=0 and i!=(h-1):
       print(" " * (h-(i+2)) + " *" * (i+1))

h=h+2
for i in range(0,h):
    print(" " * 10,end="")
    print(" "*2,end="")
    if i==0:
        print(" " * (h-1) + "*")
    if i==(h-1):
        print("*" + " *" * (h-1))
    if i!=0 and i!=(h-1):
       print(" " * (h-(i+2)) + " *" * (i+1))


h=h+2
for i in range(0,h):
    print(" " * 10,end="")
    if i==0:
        print(" " * (h-1) + "*")
    if i==(h-1):
        print("*" + "_*" * (h-1))
    if i!=0 and i!=(h-1):
       print(" " * (h-(i+2)) + " *" * (i+1))
print(" " * 10,end="")
print("Merry Chritmas!")


#트리만들기
def star(h=3,dan=1,n=1): 
    for i in range(0,h):
        print(" " * (2*(dan-n)),end="")
        print(" " * 10,end="")
        if i==0:
            print(" " * (h-1) + "*")
        if i==(h-1):
            print("*" + " *" * (h-1))
        if i!=0 and i!=(h-1):
           print(" " * (h-(i+2)) + " *" * (i+1))


def drawTree():
    dan=int(input("몇 단 트리 만들까요~? "))
    for i in range(0,dan):
        star(3+(i*2),dan,i+1)
    print(" " *(dan*3),end="")
    print("Merry Chritmas!")


drawTree()















