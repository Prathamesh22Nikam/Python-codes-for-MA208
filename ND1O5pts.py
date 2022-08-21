import math as ma
def fifthder(x):
	return (ma.sin(x))
x = [0 for i in range(5) ]; 
y = [0 for j in range(5)];
z = [0 for j in range(5)];
x[0]=0
x[1]=1
x[2]=2
x[3]=3
x[4]=4
y[0]=0
y[1]=1
y[2]=2
y[3]=3
y[4]=4
h = x[1] - x[0]
z[0] = ((48*y[1])-(25*y[0])-(36*y[2])+(16*y[3])-(3*y[4]))/(12*h)
z[1] = (-(10*y[1])-(3*y[0])+(18*y[2])-(6*y[3])+(y[4]))/(12*h)
z[3] = (-(3*y[4])-(10*y[3])+(18*y[2])-(6*y[1])+(y[0]))/(12*h*(-1))
z[4] =  (-(16*y[1])+(3*y[0])+(36*y[2])-(48*y[3])+(25*y[4]))/(12*h)
z[2] = (y[0] +(8* y[3]) - (8*y[1])-y[4])/(12*h)
for i in range(5):
	print(round(z[0],6))
a=(h**4)*fifthder(x[0])/5
b=(h**4)*fifthder(x[4])/5
c=a/4
d=b/4
e=a/6
f=b/6
print('--------')
print(round(a,6),round(b,6),'---',round(c,6),round(d,6),'---',round(e,6),round(f,6))