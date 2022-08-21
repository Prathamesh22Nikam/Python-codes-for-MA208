m = int(input('Enter no of points m: '))
n = int(input('Enter highest degree n: '))
x = [0 for i in range(m) ]; 
y = [0 for j in range(m)];
a = [0 for j in range(2*n+1)];
b = [0 for j in range(n+1)];
for i in range(m):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
for i in range(2*n+1):
     a[i] = 0
     for j in range(m):
     	a[i] = a[i] + (x[j]**i)
for i in range(n+1):
     b[i] = 0
     for j in range(m):
     	b[i] = b[i] +((y[j]) *(x[j]**i))
for i in range(2*n + 1):
    print(round(a[i],6))  
print('--------')       	
for i in range(n +1):
	print(round(b[i],6))    