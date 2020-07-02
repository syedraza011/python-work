#print("Welcome to the calculator")
#string n;
#while (n == 'y'):
x = int (input("Enter your value: "))
y = int (input("Enter your value: "))




print("Please make a choice \n +,-,*,/")
choice = input("Enter your value: ")

if(choice=='+'):
    add=x + y
    print(add)

elif(choice=='-'):
    sub= x - y
    print(sub)
elif(choice=='*'):
    mul=x * y
    print(mul)
elif(choice=='/'):
    if(y==0):
        div=0
    else:
        div=x / y
    print(div)
else:
    print("Make the right choice choice")

#n = str (input("To continue press n: "))
#n = n.lower()



