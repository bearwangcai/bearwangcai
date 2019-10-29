import os  
import xlrd
import xlwt

global data0
global data1
global unopen_province
global row0_0
global row0_1



def file_name(file_dir):   
    files_name = []
    province = []   
    for root, dirs, files in os.walk(file_dir): #读文件夹中的文件名（根目录，子文件夹目录，文件名）  
        for file in files:  
            files_name.append(os.path.join(root, file)) #合成标准路径名
            if (file[:2] == '内蒙'):
                province.append('内蒙古')
            elif (file[:2] == '黑龙'):
                province.append('黑龙江')
            else:
                province.append(file[:2])
    num = len(files_name)              
    return province, files_name, num #都有哪些省，文件路径，文件总数

def read(files_name_,province,index):

    try:
        book=xlrd.open_workbook(files_name_)

        table0=book.sheet_by_index(0) #sheet0 
        nrows=table0.nrows
        global row0_0
        row0_0 = table0.row_values(0) #sheet0表头
        for row in range(nrows):
            if (table0.row_values(row)[0] == province): #读取相应省份数据
                data0.append(table0.row_values(row))
        
        table1=book.sheet_by_index(1) #sheet1 
        nrows=table1.nrows
        global row0_1
        row0_1 = table1.row_values(0) #sheet1表头
        for row in range(nrows):
            if (table1.row_values(row)[0] == province):#读取相应省份数据
                data1.append(table1.row_values(row))
    except:
        #print(files_name_)
        unopen_province.append(province) #打不开文件的省份名
    



def write_excel(file_dir):
    f = xlwt.Workbook()

    sheet0 = f.add_sheet(u'sheet0',cell_overwrite_ok=True)
    for i_0 in range(len(row0_0)): #写sheet0表头
        sheet0.write(0,i_0,row0_0[i_0])
    for i_1 in range(1,len(data0)+1):
        for i_2 in range(len(data0[0])):
            sheet0.write(i_1,i_2,data0[i_1-1][i_2]) #写sheet0内容

    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    for i_0 in range(len(row0_1)): #写sheet1表头
        sheet1.write(0,i_0,row0_1[i_0])
    for i_1 in range(1,len(data1)+1):
        for i_2 in range(len(data1[0])):
            sheet1.write(i_1,i_2,data1[i_1-1][i_2]) #写sheet1内容
    
    f.save(file_dir)


if __name__ == "__main__":
    data0 = [] #全局变量，按行存储各省工作进展
    data1 = [] #全局变量，按行存储各省需集团协调问题
    unopen_province = [] #全局变量，打不开文件的省
    file_dir = r'D:\事务性工作\网络规划双周报\test'
    province, files_name, num = file_name(file_dir)

    print(num) #文件总数

    for i in range(num): #读文件
        read(files_name[i],province[i],i)

    print('可以打开的文件总数',len(data0))
    print('不可以打开的文件总数',len(unopen_province)) 
    print('不可以打开文件的省',unopen_province)

    write_excel(file_dir + '\\汇总.xls') #写文件
