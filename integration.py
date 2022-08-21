import math as ma
def func(x):
	return ma.ln(x)
n=int(input('enter n:'));
x = [0 for i in range(5) ]; 
y = [0 for j in range(5)];
x[0]=0
x[1]=1
x[2]=2
x[3]=3
x[4]=4
for i in range(5):
	y[i]=func(x[i])
y[0]=0
y[1]=1
y[2]=2
y[3]=3
y[4]=4
h = x[1] - x[0]
a= (h/2)*(y[0]+y[1])
b=(h/3)*(y[0]+4*y[1]+y[2])
c=(3*h/8)*(y[0]+3*y[1]+3*y[2]+y[3])
d=(4*h/90)*(7*y[0]+32*y[1]+12*y[2]+32*y[3]+7*y[4])
if(n==1):
	print(a);
elif(n==2):
	print(b);
elif(n==3):
	print(c);
else:
	print(d);
