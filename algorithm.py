#given function f(x)=x^4+7x^3+5x^2-17*X+3. Need to find the local minima of the function .
# From the graph expected minima should be between -4 and -6

x_i=0 #initialize a dummy variable
x_i1=-2 #initialize a starting point for the algorithm (try starting at - and see where you reach)
alpha=0.01 #choose a learning rate

prec=0.0001 #decide the precision needed for the solution

#define the derivative for function f(x), f'(x)
def f_prime(x):
    p=(4*x**3)+21*(x**2)+10*x-17
    return p
#run the algorithm until the required precision is achieved
while(abs(x_i1-x_i)>prec):
    x_i=x_i1
    x_i1=x_i1-alpha*f_prime(x_i)    #x1=x0-alpha*(gradient(f(x0)))
print("Minima is at x=",x_i1)