#!python 3
#coding utf-8
"""
coordinate
Author:Bear
"""

from math import cos,pi
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

"read data"
book=xlrd.open_workbook(r"C:\Users\Bear\Documents\WeChat Files\wanghaobin849340\Files\Fw_ 数据需求-反馈\小区列表.xls")
#book=xlrd.open_workbook(r"E:\中移动\test.xlsx")
table=book.sheet_by_index(0)
nrows=table.nrows
#print (nrows)
data=[]
lon=[]
lat=[]
cor=[]
step=5
for clonum in range(1,nrows):
    data.append(table.row_values(clonum))
#print(data[0])

"read coordiante"
for i in range(0,len(data)):
    cor.append(data[i][2:4])
#print(len(cor))
"read longitude"
for i in range(0,len(data)):
    lon.append(data[i][2])
#print(lon[0])
"read latitude"
for i in range(0,len(data)):
    lat.append(data[i][3])
#print(lat[0])

"find the position of start and end"
lonmax=max(lon)
lonmin=min(lon)
latmax=max(lat)
latmin=min(lat)
#print(lonmax,lonmin,latmax,latmin)
#lonmax=103.932777 lonmin=103.58881 latmax=36.13733 latmin=36.023888
#基站经度相对值x
x=[]
for i in lon:
    count=0
    x_lon=(i-lonmin)*111000*cos(lat[count]*pi/180)
    x.append(x_lon)
#基站纬度相对值y   
y=[]
for i in lat:
    y_lat=(i-latmin)*111000
    y.append(y_lat)
    
    
#print(len(x))
#print(len(y))

"find the xyposition of start and end"
xmax=max(x)
xmin=min(x)
ymax=max(y)
ymin=min(y)


"画出基站方格"
A1=np.arange(ymin-500,ymax+500,step)
B1=np.arange(xmin-500,xmax+500,step)
'''
count1=len(A1)*len(B1)
print(count1)
x1=np.zeros(count1)
y1=np.zeros(count1)
'''
x1=[]
y1=[]
for i in A1:
    for j in B1:
        x1.append(j)
        y1.append(i)

areaxy=list(zip(x1,y1))


'''
"find corner"
xantenna=[]
yantenna=[]
for j in range(0,len(y)):
    dis=[]
    for i in range(0,len(y1)):
        dis.append((x[j]-x1[i])**2+(y[j]-y1[i])**2)
#    print(len(dis))
    c=dis.index(min(dis))
    xantenna.append(x1[c])
    yantenna.append(y1[c])

#print (xantenna)
'''
antennaxy=list(zip(x,y))
kdTree_areaxy=cKDTree(areaxy)
kdTree_antenna=cKDTree(antennaxy)
#print(kdTree_areaxy)

areaxyfin=[]
for i in range(len(areaxy)):
    if  kdTree_antenna.query_ball_point(areaxy[i],2000):
        areaxyfin.append(areaxy[i])
print(len(areaxyfin))

a=np.array(areaxyfin)
f1=plt.subplot(121)
plt.scatter(x,y)
label='原始基站位置'
plt.grid()



f3=plt.subplot(122)
plt.scatter(a[:,0],a[:,1],s=0.1)
label='自适应区域划分'
plt.grid()


plt.show()


f = open(r"H:\MyDocuments\Fw_ 数据需求-反馈\5m.txt", "w+")
f.write("x\t\t\ty\n")
for i in range(len(a)):
    f.write(str(a[i][0]) + "\t" + str(a[i][1]) + "\n")
f.close()