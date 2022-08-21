def func(a):
	b = (2.71828182846)**a
	return b
# Reading number of unknowns
n = int(input('Enter n: '))


# Making numpy array of n & n x n size and initializing 
x = [0 for i in range(n+1) ]; 
y = [0 for i in range(1+n)]; 
h = [0 for i in range(n+1)]; 
a = [0 for i in range(n+1) ]; 
b = [0 for i in range(n+1) ]; 
c = [0 for i in range(n+1) ]; 
d = [0 for i in range(1+n)]; 
e = [0 for i in range(1+n)]; 
f = [0 for i in range(1+n)]; 
g = [0 for i in range(1+n)]; 
j = [0 for i in range(1+n)];
print('Enter data  ')
for i in range(1+n):
    x[i] = float(input( 'x['+str(i)+']='))
    
    #y[i] = float(input( 'y['+str(i)+']='))
for i in range(1+n):
	y[i] = func(x[i])
for i in range(n):
	h[i] = x[i+1] - x[i]
for i in range(n+1):	
	a[i] = y[i]
for i in range(1,n):
	e[i] = ((3/h[i])*(a[i+1] - a[i])) -( (3/h[i-1])*(a[i] - a[i-1]))
		
f[0] =1
g[0]=0
j[0]=0
for i in range(1,n):
	f[i] =(2*(x[i+1] - x[i-1]) - (h[i-1]*g[i-1]))
	g[i] = h[i]/f[i]
	j[i] = (e[i]- h[i-1]*j[i-1])/f[i]
    
f[n] = 1
j[n] = 0
c[n] = 0
for i in reversed(range(n)):
	c[i] = j[i] - g[i]*c[i+1]
	b[i] = (((a[i+1] - a[i])/h[i] )-(h[i]*(c[i+1] + 2*c[i])/3))
	d[i] = (c[i+1] -c[i])/(3*h[i])
	
for i in range(n):
	print(round(a[i],6),round(b[i],6),round(c[i],6),round(d[i],6))