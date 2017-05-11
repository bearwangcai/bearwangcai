#!Python 3
#code=UTF-8

"""
冒泡法排序
Author： WangHaobin
Date 20170429
Version 1.0
"""

import cairo
from test import *
import math

A=[2,7,5,9,1,13,12,29,13,14.5,17,1.3,2]
#A=[13,12,11,10,9,8,7,6,5,4,3,2,1]
B=[]



def draw(A):
    ims=cairo.ImageSurface(cairo.FORMAT_ARGB32,2000,1000)
    cr = cairo.Context(ims)
    cr.set_source_rgb(0.6, 0.6, 10.6)


    count=0
    for i in range (0,len(A)):
        for j in range (0,len(A[i])):
            cr.arc(70+70*i,70+70*j,5+math.sqrt(A[i][j]),0,2*math.pi)
            cr.fill()
            count+=1
    
    ims.write_to_png(r"C:\Users\大熊\Desktop\sorting\image.png")
    




def sorting(A):
    """
    按照冒泡法排序
    @param A: a list of number
    @return A: a list of number sorted from small to big
    @return B: a list of number mark all the changes of A
    """
    B.append(A[:])

    for i in range (0,len(A)-1):
        for j in range (0,len(A)-i-1):
            if (A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]
                B.append(A[:])

    return A,B   
    
def test_sorting1():
    C,D=sorting(A)
    assert C==[1,1.3,2,2,5,7,9,12,13,13,14.5,17,29]
    

if __name__ == "__main__":    
    C,D=sorting(A)   
    draw(D)
    print(C)
    print(len(D))