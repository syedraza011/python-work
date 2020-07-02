if __name__ == '__main__':
    
    a=[]
    n = int(input("Enter a value: "))
    for i in range(n):
        a.append(int(input("Enter the Values: ")))
        a = list(set(list(a)))
        a.sort()

print(a[-2])



