import cairo
from test import *
import math

A=[2,7,5,9,1,13,12,29,13,14.5,17,1.3,2]
#A=[13,12,11,10,9,8,7,6,5,4,3,2,1]
B=[] 
def draw1(A,x):
    ims=cairo.ImageSurface(cairo.FORMAT_ARGB32,1000,1000)
    cr = cairo.Context(ims)
    cr.set_source_rgb(0.6, 0.6, 10.6)
    for i in range (0,len(A)):
            cr.arc(70+70*i,70+70*i,5+math.sqrt(A[i]),0,2*math.pi)
            cr.fill()   
    ims.write_to_png(r"C:\Users\大熊\Desktop\sorting\image%d.png"%x)    

def sorting1(A):
    """
    按照冒泡法排序
    @param A: a list of number
    @return A: a list of number sorted from small to big
    """
    count=0
    draw1(A,0)
    for i in range (0,len(A)-1):
        for j in range (0,len(A)-i-1):
            if (A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]
                count+=1
                draw1(A,count)
sorting1(A)


