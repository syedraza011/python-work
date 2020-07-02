x = int(input("Ente the value for x: "))
y = int(input("Ente the value for y: "))
z = int(input("Ente the value for z: "))
n = int(input("Ente the value for N: "))
a = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a+ b + c != n]
print(a)
             
