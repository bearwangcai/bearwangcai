import numpy as np
import queue
import matplotlib.pyplot as plt

def quickhull(A):
    A=sorted(A,key=lambda x: x[0])
    p1=A[0]
    pn=A[-1]
    
    Lupper=[]
    Llower=[]
    #分成上包和下包两类
    Lupper.append(p1)
    Llower.append(p1)
    for i in A:
        e=np.array([[i[0],i[1],1],[p1[0],p1[1],1],[pn[0],pn[1],1]])
        flag=np.linalg.det(e)#行列式右手螺旋法则

        if flag > 0 :
            Lupper.append(i)

        else :
            Llower.append(i)
    Lupper.append(pn)  #上包      
    Llower.append(pn)  #下包
    #相同x值在上包中只取y最大值点
    xnum=[]
    Lupperreal=[]   
    for i in Lupper:
        xnum.append(i[0])
    xnum1=sorted(list(set(xnum)))
    for i in xnum1:
        ychange=[]
        for j in Lupper:
            if i == j[0]:
                ychange.append(j[1])
                Lupper.remove(j)
        Lupperreal.append((i,ychange[-1]))
    Lupper=Lupperreal
                
    #相同x值在下包中只取y最小值点                      
    ynum=[]
    Llowerreal=[]    
    for i in Llower:
        ynum.append(i[0])
    ynum1=sorted(list(set(ynum)))
    for i in ynum1:
        ychange=[]
        for j in Llower:
            if i == j[0]:                
                ychange.append(j[1])
                Llower.remove(j)
        Llowerreal.append((i,ychange[0]))
    Llower=Llowerreal
    #将上包和下包分别放入两个队列中
    upp=queue.Queue(0)
    low=queue.Queue(0)
    if Lupper!=[]:
        upp.put(Lupper)


    if Llower!=[]:
        low.put(Llower)


    result=[]
    #处理上包
    while (upp.empty()==False):#当队列不为空时
        data=upp.get()#取出位列队头的点集合
        num=len(data)
        Lupper1=[]
        Lupper2=[]
        if num > 3:#当点集合中点数大于3时，取中心点，可用来寻找外侧点和删除位于中间部分的点
            p1=data[0]
            pn=data[-1]
            if num%2==0 :
                pmid=data[int(num/2)]
                indexnum=int(num/2)
            else:
                pmid=data[int((num-1)/2)]
                indexnum=int((num-1)/2)
            data1=[]
            data2=[]        
            for i in range(indexnum+1):
                data1.append(data[i])
            for i in range(indexnum,num):
                data2.append(data[i])            
            data1.sort()
            data2.sort()
            Lupper1.append(data1[0])
            for item in data1:
                e=np.array([[item[0],item[1],1],[p1[0],p1[1],1],[pn[0],pn[1],1]])            
                flag=np.linalg.det(e)
                if flag > 0 :
                    if item not in Lupper1:
                        Lupper1.append(item)
            if data1[-1] not in Lupper1:
                Lupper1.append(data1[-1])
            upp.put(Lupper1)

            print('Lupper1',Lupper1)
            Lupper2.append(data2[0])
            for item in data2:
                e=np.array([[item[0],item[1],1],[p1[0],p1[1],1],[pn[0],pn[1],1]])
                flag=np.linalg.det(e)
                if flag > 0 :
                    if item not in Lupper2:
                        Lupper2.append(item)
            if data2[-1] not in Lupper2:
                Lupper2.append(data2[-1])
            upp.put(Lupper2)

            print('Lupper2',Lupper2)
        else :
            print('else')
            result.append(data)
            if upp.empty():
                print('upp is empty')

    print('upp completed')    
        
        
        
    while (low.empty()==False):
        data=low.get()
        Llower1=[]
        Llower2=[]
        num=len(data)       
        if num > 3:
            p1=data[0]
            pn=data[-1]
            if num%2==0 :
                pmid=data[int(num/2)]
                indexnum=int(num/2)
            else:
                pmid=data[int((num-1)/2)]
                indexnum=int((num-1)/2)
            print('pmid',pmid)
            data1=[]
            data2=[]        
            for i in range(indexnum+1):
                data1.append(data[i])
            for i in range(indexnum,num):
                data2.append(data[i])            
            data1.sort()
            data2.sort()
            Llower1.append(data1[0])
            for item in data1:
                e=np.array([[item[0],item[1],1],[p1[0],p1[1],1],[pn[0],pn[1],1]])
                flag=np.linalg.det(e)
                if flag < 0 :
                    if item not in Llower1:
                        Llower1.append(item)
            if data1[-1] not in Llower1:
                Llower1.append(data1[-1])
            low.put(Llower1)

            print('Llower1',Llower1)
            Llower2.append(data2[0])
            for item in data2:
                e=np.array([[item[0],item[1],1],[p1[0],p1[1],1],[pn[0],pn[1],1]])
                flag=np.linalg.det(e)
                if flag < 0 :
                    if item not in Llower2:
                        Llower2.append(item)
            if data2[-1] not in Llower2:
                Llower2.append(data2[-1])
            low.put(Llower2)

            print('Llower2',Llower2)
        else :
            result.append(data)
    #删除重复点   
    result1=[]    
    for i in result:
        for j in i:
            result1.append(j)
    result2=[]
    for i in result1:
        if i not in result2:
            result2.append(i)
    return result2
        
def main():
    test=[[0,1],[1,0],[1,1],[1,2],[2,3],[2,2],[2,0],[3,3],[4,1]]
    result=quickhull(test)
    print('result',result)
    
if __name__ == "__main__":      
    main()

 

    