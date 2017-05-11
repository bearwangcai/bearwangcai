# coding = utf-8 
import csv 
filename='E:/GS_Insights_Sample_1-EALIDAR_DSM_2M/GS_Insights_Sample_1-EALIDAR_DSM_2M/GS_Insights_Sample_1-EALIDAR_DSM_2M_xyz_Values.csv'


#'''data qcquire'''
data = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = reader.next()
        data = [row for row in reader]
        data = np.array(data)
except csv.Error as e:
    print "Error reading CSVfile at line %s: %s" %(reader.line_num, e)
    sys.exit(-1)
if header:
 ''' '  print header
    print '================' '''
'print data[:,4]'


csvfile = file('E:/Demtest.csv','wb')
writer = csv.writer(csvfile)
for i in range(0,len(c)):
    writer.writerow(row+c[i])
csvfile.close()