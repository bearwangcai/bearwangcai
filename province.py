import xlrd
import xlwt
import matplotlib.pyplot as plt

book=xlrd.open_workbook(r"G:\移动设计院工作\飞行检测\2017年一阶段飞行检测产品分配关系表1.xlsx")
#book=xlrd.open_workbook(r"E:\中移动\test.xlsx")
table=book.sheet_by_index(0)
nrows=table.nrows
#print (nrows)
data=[]
pro=[]
for clonum in range(1,nrows):
    data.append(table.row_values(clonum))
#print(data[0])
pro1=[]


company=[]
for i in range(0,len(data)):
    company.append(data[i][2])
#print(set(company))


"read province"
for i in range(0,len(data)):
    pro.append(data[i][3])
#print(len(pro))


'''
pro1与product2的位置是一致的
'''

for i in range(0,len(pro)):
    pro1.append(pro[i].split(','))
#print(pro1)
#print(len(pro1))
#print(pro1[0][0])

pro2=[]
for i in range(0,len(pro1)):
    for j in range(0,len(pro1[i])):
        pro2.append(pro1[i][j])
print(len(pro2))



#需要调研的省份*******************************
province=list(set(pro2))
#print(province)

weight=[]
for i in province:
    count=0
    for j in pro2:
        if j==i:
            count+=1
    weight.append(count)

            

product1=[]    
"read the product"
for i in range(0,len(data)):
    product1.append(data[i][1])
product2=[]
for i in product1:
    if i !='':
        product2.append(i)


        
        
        
'''

def write_excel():
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    for i in range(0,len(province)):
        sheet1.write(i,0,province[i])
        sheet1.write(i,1,weight[i])

    f.save(r"G:\移动设计院工作\飞行检测\省份权重.xls")
write_excel()  
'''










#产品与权值匹配关系 
cdef=[]
f1=open(r"G:\移动设计院工作\飞行检测\产品清单1.txt")
s=f1.readlines()
for line in s:
    line =line.rstrip()
    cdef.append([i for i in line.split(' ')])  
print(cdef)

   
a=[]
b=[]
for i in range(0,len(cdef)):
    a.append(cdef[i][0])
    b.append(cdef[i][1])



d=dict(zip(a,b))
#print(d)



 
#该省份权重值
provinceweight=[]
for i in range(0,len(province)):
    provinceweight.append(0)
#print(provinceweight)


for i in range(0,len(product2)):
    for j in pro1[i]:
        provinceweight[province.index(j)]+=int(d[product2[i]])
#print(provinceweight)
#dpw=dict(zip(province,provinceweight))
#print(dpw)




def write_excel():
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    sheet1.write(0,0,'省份')
    sheet1.write(0,1,'权重')
    for i in range(0,len(province)):
        sheet1.write(i+1,0,province[i])
        sheet1.write(i+1,1,provinceweight[i])

    f.save(r"G:\移动设计院工作\飞行检测\省份权重.xls")
write_excel()  
