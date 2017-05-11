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
#print(pro2)



#需要调研的省份*******************************
province=list(set(pro2))
#print(province)













product1=[]    
"read the product"
for i in range(0,len(data)):
    product1.append(data[i][1])
product2=[]
for i in product1:
    if i !='':
        product2.append(i)



company1=[]
"read the company"
for i in range(len(data)):
    company1.append(data[i][2])
#print(company1)


        
propre=[]
produpre=[]   
compre=[]     
for i in province:
    for j in range(0,len(pro1)):
        for k in range(0,len(pro1[j])):
            if i==pro1[j][k]:
                propre.append(i)
                produpre.append(product2[j])
                compre.append(company1[j])
   
#print(len(propre))
#print(len(produpre))





def write_excel():
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    for i in range(0,len(propre)):
        sheet1.write(i,0,propre[i])
        sheet1.write(i,1,produpre[i])
        sheet1.write(i,2,compre[i])
    
    f.save(r"G:\移动设计院工作\飞行检测\省份产品对应表2.xls")
write_excel()


