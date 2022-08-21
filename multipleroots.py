#actual function
def f(x):
    return x**3 - 5*x**2+7*x - 3

# First derivative of function
def g(x):
    return 3*x**2 - 10*x+7
#second derivative of function    
def h(x):
 	return 6*x-10
 
def multiple(x0,e,N):
    print('\n\n*** MULTIPLE ROOTS METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while(condition):
        if (g(x0)**2-(f(x0)*h(x0)))== 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 -( f(x0)*g(x0)/(g(x0)**2-(f(x0)*h(x0))))
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
 #condition will be true or false       
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.6f' % x1)
    else:
        print('\nNot Convergent.')
       

#inputs require to run program
x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Steps: '))

#Calling this Method
multiple(x0,e,N)
