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
k1 =float(h*f(x[0],y[0]))
k2 = float(h*f(x[0]+(h/2),y[0]+(0.5*k1)))
k3=float( h*f(x[0]+(h/2),y[0]+(0.5*k2)))
k4 = float(h*f (x[1],y[0]+ k3))
y[1]= y[0]+(1/6)*(k1+(2*k2 )+(2*k3)+k4)
k1 =float(h*f(x[1],y[1]))
k2 = float(h*f(x[1]+(h/2),y[1]+(0.5*k1)))
k3=float( h*f(x[1]+(h/2),y[1]+(0.5*k2)))
k4 = float(h*f (x[2],y[1]+ k3))
y[2]= y[1]+(1/6)*(k1+(2*k2 )+(2*k3)+k4)
k1 =float(h*f(x[2],y[2]))
k2 = float(h*f(x[2]+(h/2),y[2]+(0.5*k1)))
k3=float( h*f(x[2]+(h/2),y[2]+(0.5*k2)))
k4 = float(h*f (x[3],y[2]+ k3))
y[3]= y[2]+(1/6)*(k1+(2*k2 )+(2*k3)+k4)
for i in range (3,n):
	y[i+1]= y[i-3]+( 4*h/3)*(2*f(x[i],y[i])-1*f(x[i-1],y[i-1])+2*f(x[i-2],y[i-2]))
for i in range (1,n+1):
	
	d=func(x[i])
	e=abs(d-y[i])
	print(i,round(x[i],3),round(y[i],6),round(d,6),round(e,6))