import math as ma
def func(x):
	return (2/(x*x+4))
z=int(input('enter z:'));
n=int(input('enter n:'));
h=float(input('enter h:'));
x = [0 for i in range(n+1) ]; 
y = [0 for j in range(1+n)];
x[0]=float(input('enter x0:'));
for i in range(1,n+1):
	x[i]=x[i-1]+h
for i in range(n+1):
	y[i]=func(x[i])
a=0
c=0
e=0
g=0
if z==1:
	for i in range(n+1):
		if i==0 or i==n:
			a+=y[i];
		else:
			a+=2*y[i];
	b=(h/2)*a;
	print(round(b,6));
if z==2:
	for i in range(n+1):
		if i==0 or i==n:
			c+=y[i];
		elif i%2==1:
			c+=4*y[i];
		else:
			c+=2*y[i];
	d=(h/3)*c;			
	print(round(d,6));
if z==3:
	for i in range(n+1):
		if i==0 or i==n:
			e+=y[i];
		elif i%3==0:
			e+=2*y[i];
		else:
			e+=3*y[i];
	f=(3*h/8)*e;			
	print(round(f,6));
if z==4:
	for i in range(n+1):
		if i==0 or i==n:
			g+=7*y[i];
		elif i%4==0:
			g+=14*y[i];
		elif i%2==0:
			g+=12*y[i];
		else:
			g+=32*y[i];
	k=(2*h/45)*g;			
	print(round(k,6));