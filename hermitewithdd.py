# Python3 program for implementing  
# Newton divided difference formula  

  
# Function to find the product term  

def proterm(i, value, x):  

    pro = 1;  

    for j in range(i):  

        pro = pro * (value - x[j]);  

    return pro;  

  
# Function for calculating  
# divided difference table  

def dividedDiffTable(x, y, n): 

  

    for i in range(1, n):  

        for j in range(n - i):  

            if (x[j]-x[i+j] ==0):
                   y[j][i]= y[j][i]
                   
            else:       
                   y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /  (x[j] - x[i + j])); 

    return y; 

  
# Function for applying Newton's  
# divided difference formula  

def applyFormula(value, x, y, n):  

  

    sum = y[0][0];  

  

    for i in range(1, n): 

        sum = sum + (proterm(i, value, x) * y[0][i]);  

      

    return sum;  

  
# Function for displaying divided  
# difference table  

def printDiffTable(y, n):  

  

    for i in range(n):  

        for j in range(n - i):  

            print(round(y[i][j], 6), "\t",  

                               end = " ");  

  

        print("");  

  
# Driver Code 

  
# number of inputs given  

n = 6;  

y = [[0 for i in range(10)]  

        for j in range(10)];  

x = [ 1.3,1.3,1.6,1.6,1.9,1.9 ];  

  
# y[][] is used for divided difference  
# table where y[][0] is used for input  

y[0][0] = 0.620086;  

y[1][0] = 0.620086;  

y[2][0] = 0.455402;  

y[3][0] = 0.455402; 

y[4][0] = 0.281819; 
  
y[5][0] = 0.281819; 

y[0][1] = -0.522023; 

y[2][1] = -0.569896; 

y[4][1] = -0.581157; 


  
# calculating divided difference table  

y=dividedDiffTable(x, y, n);  

  
# displaying divided difference table  
printDiffTable(y, n);  

  
# value to be interpolated  

value = 1.6;  

  
# printing the value  

print("\nValue at", value, "is", 

        round(applyFormula(value, x, y, n), 6))
