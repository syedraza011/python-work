def sum(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y!=0:
        return x / y
    else:
        return 0

y= True
while (y ==True):
    
    x=int(input("Enter the value for x: "))
    y=int(input("Enter the value for y: "))
    choice = input(" +,-,*,/ or press = to see all operation ")
    if choice== '+':
        print("The Sum of x and y is:", sum(x,y))
    
    elif choice== '-':
        print("The Subtraction of x and y is:", sub(x,y))
    elif choice== '*':
        print("The multiplication of x and y is:", mul(x,y))
    elif choice== '/':
        if div(x,y)==0:
            print("since y=0 that's y it is Undefined")
        else:
            print("The Division of x and y is:", div(x,y))
    elif choice== '=':
        print("The Sum of x and y is:", sum(x,y))
        print("The Subtraction of x and y is:", sub(x,y))
        print("The multiplication of x and y is:", mul(x,y))
        print("The Division of x and y is:", div(x,y))
    else:
        print("Make the proper choice dude") 
        y = input("to exit press any key or y to continue")
        if(y != 'y'):
            y= False
            
