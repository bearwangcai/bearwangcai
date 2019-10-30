import os  
import docx
from docx import Document
from read_docx import read_file

global professions

global province_names #省名

global content_names #共性意见 个性意见

global all


def write_file(file):

    for province_name in province_names:
        document = Document()
        document.add_heading(province_name + '分公司2020-2022年网络发展滚动规划总体思路评审意见', 0)
        p = document.add_paragraph('')
        p = document.add_paragraph('2019年9月25日-9月26日集团公司网络发展部组织集团规划项目组对你省公司2020-2022年网络发展滚动规划总体思路进行了集中评审，形成审查意见如下。')


        for profession in professions:
            document.add_heading(profession, level=1)
            try:
                if (len(profession) == 1):
                    profession = profession[0]
                    for content_name in content_names: #共性问题，个性问题
                        p = document.add_paragraph('')
                        p.add_run(content_name).bold = True
                        for content in file[profession][province_name][content_name]:
                            p = document.add_paragraph(content)
                else:
                    for index, sub_profession in enumerate(profession):
                        if index == 0:
                            document.add_heading(sub_profession, level=1)
                        else:
                            document.add_heading(sub_profession, level=2)
                            for content_name in content_names: #共性问题，个性问题
                                p = document.add_paragraph('')
                                p.add_run(content_name).bold = True
                                for content in file[profession][province_name][content_name]:
                                    p = document.add_paragraph(content)
            except: 
                pass
                '''
                for content_name in content_names: #共性问题，个性问题
                    p = document.add_paragraph('')
                    p.add_run('content_name').bold = True
                    for content in file[profession][province_name][content_name]:
                        p = document.add_paragraph(content)
                '''
        document.save(r'C:\Users\x270\Desktop\test' + '\\'+ province_name + '分公司2019-2021年网络发展滚动规划初审意见.docx')

def main():
    global professions
    #professions = ['IDC',['无线网','移动网','核心网']]
    professions = [['IDC']]
    global province_names #省名
    province_names = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
    global content_names #共性意见 个性意见
    content_names = ['（一）共性意见','（二）你省审查意见']
    global all
    all = read_file()
    write_file(all)

if __name__ == "__main__":
    main()




        

