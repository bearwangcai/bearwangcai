f1=open('F:/python_DEM_text/datahandle/test4.txt')
s=f1.readlines()
for line in s:
    line =line.rstrip()
    print([i for i in line.split(' ')])
    print('*********')


f = open(r"F:\Fw_ 数据需求-反馈\coordinatewrong.txt", "w+")
f.write("xfin\tyfin\n")
for i in range(0, len(xfin)):
    f.write(str(xfin[i]) + "\t" + str(yfin[i]) + "\n")
f.close()