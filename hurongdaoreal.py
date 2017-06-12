from copy import deepcopy
class cctype(object):
    def __init__(self,x_init_p,y_init_p,width,long,name):
        self.x_init_p=x_init_p-1
        self.y_init_p=y_init_p-1
        self.width=width
        self.long=long
        self.name=name
    def xyposition(self):
        xyp=[]
        for i in range(self.width):
            for j in range(self.long):
                xyp.append([self.x_init_p+i,self.y_init_p+j])
        return xyp
    def classtype(self):
        return 'caocao'
class gytype(cctype):
    def classtype(self):
        return 'guanyu'
class zftype(cctype):
    def classtype(self):
        return 'zhangfei'
class bingtype(cctype):
    def classtype(self):
        return 'bing'

class chesscheck(object):
    def __init__ (self,x,y):
        self.x=x
        self.y=y 
    def get_chess(self):
        chessp=[]
        for i in range(self.x):
            for j in range(self.y):
                chessp.append([i,j])
        return chessp
    def wincondition(self):
        return [[(x-1)/2,y],[(x+1)/2,y]]
        
        

checkerboard=chesscheck(5,4)
Caocao=cctype(1,2,2,2,'Caocao')
Zhaoyun=zftype(1,1,2,1,'Zhaoyun') 
Huangzhong=zftype(1,4,2,1,'Huangzhong') 
Zhangfei=zftype(3,1,2,1,'Zhangfei') 
Machao=zftype(3,4,2,1,'Machao') 
Guanyu=gytype(3,2,1,2,'Guanyu')
feibingjia=bingtype(4,2,1,1,'feibingjia')
feibingyi=bingtype(4,3,1,1,'feibingyi')
feibingbing=bingtype(5,1,1,1,'feibingbing')
feibingding=bingtype(5,4,1,1,'feibingding')  
chess=[Caocao,Zhaoyun,Huangzhong,Zhangfei,Machao,Guanyu,feibingjia,feibingyi,feibingbing,feibingding]
#空格初始位置

def type1(typemark1,typemark2,typeposition1,typeposition2):#判断是否已经有这个状态，有的话删除，没有的话返回新值
    flag=0
    for num,item in enumerate(typemark1):
        if typeposition1[num]== typeposition2(typemark2.index(item)):
            flag=1
            break
    if flag==0: 
        return typemark2 ,typeposition2

def getktt(hrdchess):
    kongge=deepcopy(checkerboard.get_chess())
    typemark=[]
    typeposition=[]
    for i in hrdchess:
    #print(i)
        for j in i.xyposition():
            #print(type(j))
            kongge.remove(j)
            typemark.append(i.classtype())
            typeposition.append(j)
    return typemark , typeposition , kongge


#print(typemark)
#print(typeposition)
#huarongdaostep=0
huarongdao=[]
stepnum=0
typemarks1,typepositions1,kongges1=getktt(chess)
huarongdao.append([chess,typemarks1,typepositions1,kongges1,0,stepnum])#华容道第一步
'''
for i in huarongdao:#状态树[0]是棋子[1]该点类型[2]是所有点的位置[3]是上一步空格的位置[4]是上一步状态的地址
def move_left(i)    
    for j in i[0]:#
        k=j
        k.x_init_p-=1
        typemark1,typeposition1,kongge1=getktt(k)
        #验证空格总数是否为2
        if len(kongge1)==2:
            if (type1(typemark1,typemarkall,typeposition1,typepositionall))
            
'''