import os  
import docx
from docx import Document

global profession
global province_name #省名
global content_name #共性意见 个性意见




def file_name(file_dir):   
    files_name = []
    profession_file = []   
    for root, dirs, files in os.walk(file_dir): #读文件夹中的文件名（根目录，子文件夹目录，文件名）  
        for file in files:  
            
            (filename,_) = os.path.splitext(file)
            profession_file.append(filename)
            files_name.append(os.path.join(root, file)) #合成标准路径名

    num = len(files_name)              
    return  profession_file, files_name, num #都有哪些专业，文件路径，文件总数

def read(file_name):
    province = {} #按省存储
    document = Document(file_name)  #打开文件demo.docx
    for index,paragraph in enumerate(document.paragraphs):
        if paragraph.text in province_name:
            province_name_now = paragraph.text
            province[paragraph.text] = {} #各省该专业评审意见字典
        elif paragraph.text in content_name:
            content_name_now = paragraph.text
            province[province_name_now][content_name_now] = [] #创建共性意见/个性意见字典
        else:
            try:
                province[province_name_now][content_name_now].append(paragraph.text) #填写内容
            except:
                pass
    return province


def read_file():
    profession = {}
    global province_name #省名
    province_name = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
    global content_name #共性意见 个性意见
    content_name = ['（一）共性意见','（二）你省审查意见']
    file_dir = r'C:\Users\x270\Desktop\新建文件夹'
    profession_file, files_name, num = file_name(file_dir)

    print(num) #文件总数

    for i in range(num): #读文件
        profession[profession_file[i]] = read(files_name[i])

    return profession



if __name__ == "__main__":
    profession = read_file()



