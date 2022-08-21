import math as ma
def thirdder(x):
	return 8*(ma.e**(2*x))
def fourthder(x):
	return (ma.sin(x))	
x = [0 for i in range(3) ]; 
y = [0 for j in range(3)];
z = [0 for j in range(3)];
x[2]=3.2
x[0]=3.0
x[1]=3.1
y[2]=-2.596792

y[0]=-4.240058

y[1]=-3.496909
h = x[1] - x[0]
z[0] = ((4*y[1])-(3*y[0])-(y[2]))/(2*h)
z[1] = (y[2]-y[0])/(2*h)
z[2] = (y[0] +(3* y[2]) - (4*y[1]))/(2*h)
w= (y[2]+y[0]-(2*y[1]))/(h**2)
a=(h**2)*thirdder(x[0])/3
b=(h**2)*thirdder(x[2])/3
c=a/2
d=b/2
e=(h**2)*fourthder(x[0])/12
f=(h**2)*fourthder(x[2])/12
for i in range(3):
    print(round(z[i],6))
print('--------')
print(round(w,6))
print('--------')
print(round(a,6),round(b,6),'---',round(c,6),round(d,6))
print('---------')
print(round(e,6),round(f,6))

    