x=input("enter a line:")
l=u=0
d=a=0

for i in x:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        d+=1
    if i.isalpha():
        a+=1

print("no. of uppercase letters:", u)
print("no. of lowercase letters:", l)
print("no. of digits:", d)
print("no. of alphabets:", a)
