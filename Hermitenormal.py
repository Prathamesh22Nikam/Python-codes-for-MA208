
# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing 
x = [[0 for i in range(n)] 

        for j in range(n)]; 
y = [[0 for i in range(n)] 

        for j in range(n)]; 
z = [[0 for i in range(n)] 

        for j in range(n)]; 




# Reading data points
print('Enter data  ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
    z[i] = float(input( 'y['+str(i)+']='))


# Reading interpolation point
xp = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    p = 1
    q= 0
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
            q = q + float(1/(x[i]-x[j]))
    
    yp = yp + ((1-(2*(xp-x[i])*q))*(p**2) * y[i]  ) 
    print(round((1-(2*(xp-x[i])*q))*(p**2),6) )

for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + ((xp-x[i])*(p**2)* z[i]    )
    print(round((xp-x[i])*(p**2),6))

# Displaying output
print('Interpolated value at %.6f is %.6f.' % (xp, yp))