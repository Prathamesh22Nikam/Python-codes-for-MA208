import math as ma
b= float(input('enter beta'))
d= float(input('enter stroke'))
m=0
while(true):
	n=m-b
	l1=d*(ma.sin(radians(m))*ma.sin(radians(n))/ma.sin(radians(b)))
	l2=d*(ma.sin(radians(m))+ma.sin(radians(n)))/ma.sin(radians(b))
	l3=d*(ma.sin(radians(m))-ma.sin(radians(n)))/ma.sin(radians(b))
	print(m,n,round(l1,6),l2,l3)