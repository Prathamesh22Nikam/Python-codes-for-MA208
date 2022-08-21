import math as m
def func(x):
	return x+1-(1/2)*(m.e**x)
def f(x,y):
	return y-x*x+1
h= float(input('enter h:'))
x0=float(input('enter x0:'))
y0=float(input('enter y0:'))
b=float(input('enter b:'))
n=int((b-x0)/h)
x=[0 for i in range(n+1)]
y=[0 for i in range(n+1)]
x[0]=x0
y[0]=y0
for i in range (n):
	x[i+1]=x[i]+h
for i in range (n):
	y[i+1]= y[i]+ h*(f(x[i]+(h/2),y[i]+(h/2)*f(x[i],y[i])))
for i in range (1,n+1):
	
	d=func(x[i])
	e=abs(d-y[i])
	print(i,round(x[i],3),round(y[i],6),round(d,6),round(e,6))