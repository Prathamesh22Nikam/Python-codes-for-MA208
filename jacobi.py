f1 = lambda x,y,z: (85-3*y+2*z)/15
f2 = lambda x,y,z: (51-2*x-z)/10
f3 = lambda x,y,z: (5-x+2*y)/8

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration
print('\nCount\t     x\t          y\t            z\n')

condition = True

while (True):
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.6f\t%0.6f\t%0.6f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    if(e1<e and e2<e and e3<e):
    	break;

print('\nSolution: x=%0.6f, y=%0.6f and z = %0.6f\n'% (x1,y1,z1))