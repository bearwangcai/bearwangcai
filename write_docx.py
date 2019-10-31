import os  
import docx
from docx import Document
from read_docx import read_file
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.shared import RGBColor

global professions

global province_names #省名

global content_names #共性意见 个性意见

global all


def write_file(file):

    for province_name in province_names:
        document = Document()
        document.styles['Normal'].font.name = u'仿宋'
        document.styles['Normal'].font.size = Pt(15)
        document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'仿宋')        
        
        #标题行
        run = document.add_heading('',level=0).add_run(province_name + '分公司2020-2022年网络发展滚动规划初审评审意见')
        run.font.name=u'黑体'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体') 
        run.font.size = Pt(18)
        run.font.color.rgb = RGBColor(0x0a,0x0a,0x0a)
        run.bold = True
        
        
        p = document.add_paragraph('')
        p = document.add_paragraph('  2019年9月25日-9月26日集团公司网络发展部组织集团规划项目组对你省公司2020-2022年网络发展滚动规划总体思路进行了集中评审，形成审查意见如下。')
        p = document.add_paragraph('')


        # 一 总体要求
        run = document.add_heading('',level=1).add_run('一 总体要求')
        run.font.name=u'黑体'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体') 
        run.font.size = Pt(17)
        run.font.color.rgb = RGBColor(0x1a,0x1a,0x1a)
        run.bold = True  


        # 二 各专业具体要求  
        p = document.add_paragraph('')
        run = document.add_heading('',level=1).add_run('二 各专业具体要求')
        run.font.name=u'黑体'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体') 
        run.font.size = Pt(17)
        run.font.color.rgb = RGBColor(0x1a,0x1a,0x1a)
        run.bold = True
        p = document.add_paragraph('')     

        for profession in professions:
            
            #document.add_heading(profession, level=1)

            try:
                if (len(profession) == 1):
                    profession = profession[0]

                    #添加大专业标题
                    run = document.add_heading('',level=2).add_run(profession)
                    run.font.name=u'黑体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体') 
                    run.font.size = Pt(16)
                    run.font.color.rgb = RGBColor(0x1a,0x1a,0x1a)
                    p = document.add_paragraph('')  


                    for content_name in content_names: #共性问题，个性问题
                        p.add_run(content_name).bold = True
                        for content in file[profession][province_name][content_name]:
                            p = document.add_paragraph(content)

                else:

                    for index, sub_profession in enumerate(profession):

                        if index == 0:
                            #添加大专业标题
                            run = document.add_heading('',level=2).add_run(sub_profession)
                            run.font.name=u'黑体'
                            run._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体') 
                            run.font.size = Pt(16)
                            run.font.color.rgb = RGBColor(0x1a,0x1a,0x1a)
                            p = document.add_paragraph('') 

                        else:

                            #添加小专业标题
                            run = document.add_heading('',level=3).add_run(sub_profession)
                            run.font.name=u'黑体'
                            run._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体') 
                            run.font.size = Pt(15)
                            run.font.color.rgb = RGBColor(0x1a,0x1a,0x1a)
                            run.bold = True 
                            p = document.add_paragraph('')

                            for content_name in content_names: #共性问题，个性问题
                                p.add_run(content_name).bold = True
                                for content in file[sub_profession][province_name][content_name]:
                                    p = document.add_paragraph(content)
            except: 
                pass

        document.save(r'C:\Users\x270\Desktop\test' + '\\'+ province_name + '分公司2020-2019年网络发展滚动规划初审意见.docx')

def main():
    global professions
    #professions = ['IDC',['无线网','移动网','核心网']]
    
    #professions = [['数据网'],['STN(IPRAN)'],['传输网'],['接入网'],['IDC'],['DC'],['云'],['业务平台'],['CDN'],['移动核心网'],['固网核心网'],['应急通信'],['节能减排']]

    professions = [['移动网','移动核心网','固网核心网'],['基础网','接入网','IP网','STN(IPRAN)','传输网'],['IDC及DC基础设计建设','IDC','DC','IDC网络'],['云计算','云资源池','CDN','业务平台']]

    global province_names #省名
    province_names = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
    global content_names #共性意见 个性意见
    content_names = ['（一）共性意见','（二）你省审查意见']
    global all
    all = read_file()
    write_file(all)

if __name__ == "__main__":
    main()




        
