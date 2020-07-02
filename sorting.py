n= input("Please enter your String:")
n = "".join(sorted( set(n.casefold().replace(' ',''))))
print(n)
