n= input("Please enter your String:")
smallAlpha =[]
capitalAlpha =[]
digit=[]
even =[]
odd =[]
for ch in n:
    if ch.isalpha():
        if ord(ch)>=65 and ord(ch)<=90:
            capitalAlpha.append(ch)
        else:
            smallAlpha.append(ch)
    else:
        if int(ch) % 2 == 0:
            even.append(ch)
        else:
            odd.append(ch)
       
#print(sorted(odd))
#print(sorted(even))
digit=''.join(sorted(odd)+sorted(even))

output=''.join(sorted(smallAlpha)+sorted(capitalAlpha)+list(digit))
print(output)


