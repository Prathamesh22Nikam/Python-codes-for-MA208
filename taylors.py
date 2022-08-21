import math as m
def func(x):
	return 0
def f(x,y):
	return y-x**2+1
def f1(x,y):
	return y-x**2+1-(2*x)
def f2(x ,y):
	return y-x**2-1-(2*x)
"""def f3(x,y):
	return
def f4(x,y):
	return"""
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
	c=f(x[i],y[i])+(f1(x[i],y[i])*h/2)+(f2(x[i],y[i])*h*h/6)#+(f3(x[i],y[i])*h*h*h/24)+(f4(x[i],y[i])*h**4/120)
	y[i+1]= y[i]+ h*(c)
for i in range (1,n+1):
	
	d=func(x[i])
	e = abs(d-y[i])
	print(i,round(x[i],3),round(y[i],6),round(d,6),round(e,6))