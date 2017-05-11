import xlrd
import xlwt

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




def write_excel():
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    for i in range(0,len(propre)):
        sheet1.write(i,0,propre[i])
        sheet1.write(i,1,produpre[i])
        sheet1.write(i,2,compre[i])
    
    f.save(r"G:\移动设计院工作\飞行检测\省份产品对应表2.xls")
write_excel()