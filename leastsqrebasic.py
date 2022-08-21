n = int(input('Enter n numbers: '))
x = [0 for i in range(n) ]; 
y = [0 for j in range(n)];
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
    
a=0
b=0 
c = 0
d=0
for i in range(n):
	a = a + x[i] 
	b = b+y[i]  
	c = c + (x[i]*x[i])
	d = d+ (x[i] * y[i])
a0 =( (c*b)-(d*a))/((n*c)-(a*a))
a1 =((n*d)-(a*b))/((n*c)-(a*a))
print(round(a0,6),round(a1,6))	