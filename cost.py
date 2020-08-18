import numpy as np 
import csv
data=list(csv.reader(open('ex1data1.csv','r')))
#print(data)
data1 =np.array(data,dtype='float')
x=np.zeros(len(data1))
y=np.zeros(len(data1))
for i in range(len(data1)):
	x[i]=data1[i][0]
	y[i]=data1[i][1]

theta=np.zeros(2)
h=np.zeros(len(y))

for i in range(0,len(y)):
	h[i]=((theta[0]+(theta[1]*x[i]))-y[i])**2
print(h)
j=(1/2*len(y))*(sum(h))
print(j)