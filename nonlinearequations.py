def f(x,y):
	return x**2+x*y+y**2-7

def g(x,y):
	return x**3+y**3-9
	
def fx(x,y):
	return 2*x+y
	
def fy(x,y):
	return x+2*y
	
def gx(x,y):
	return 3*x**2	
	
def gy(x,y):
	return 3*y**2
	
def function(x,y,e,N):
    
    step = 1
    flag = 1
    condition = True
    while condition:
        if fx(x,y)*gy(x,y)-fy(x,y)*gx(x,y)== 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x +((fy(x,y)*g(x,y)-gy(x,y)*f(x,y))/(fx(x,y)*gy(x,y)-fy(x,y)*gx(x,y)))
        y1=y+ ((gx(x,y)*f(x,y)-fx(x,y)*g(x,y))/(fx(x,y)*gy(x,y)-fy(x,y)*gx(x,y)))
        print('Iteration-%d, x1 = %0.6f, y1 = %0.6f, f(x1,y1) = %0.6f, g(x1,y1) = %0.6f' % (step, x1,y1, f(x1,y1), g(x1,y1)))
         
        x= x1
        y= y1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        if (abs(f(x1,y1)) <e and abs(g(x1,y1))< e):
        	break;
    
    if flag==1:
        print('\nRequired root is: %0.8f and %0.8f' % (x1,y1))
    else:
        print('\nNot Convergent.')

x=float(input("enter initial x"))
y=float(input("enter initial y"))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

function(x,y,e,N)