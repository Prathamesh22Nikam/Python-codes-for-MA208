f1 = lambda x,y,z: (w*(24-3*y)/4)+(1-w)*x
f2 = lambda x,y,z:(w*(30-3*x+z)/4)+(1-w)*y
f3 = lambda x,y,z: (w*(-24+y)/4)+(1-w)*z

# Initial setup
x0 = 1
y0 = 1
z0 = 1
w=1.25
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\t    x\t           y\t            z\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.9f\t%0.9f\t%0.9f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    if(e1<e and e2<e and e3<e):
    	break;

print('\nSolution: x=%0.9f, y=%0.9f and z = %0.9f\n'% (x1,y1,z1))