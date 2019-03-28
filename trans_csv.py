import re
for i in range(1,34):
     f = file('/home/kai/Downloads/data/{}/201807.csv'.format(i))
     f2 = file('/home/kai/Downloads/data/{}/201807~.csv'.format(i),'w')
     for line in f:
         f2.write(re.sub(r',,',r',\N,',line))
     f2.close()
     f.close()
