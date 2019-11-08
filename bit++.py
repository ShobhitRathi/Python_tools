n=int(input("enter no of opetation(s)"))
a="++"
b="--"
c=0
for i in range(n):
        x=input()
        if a in x:
                c=c+1

        elif b in x:
                c=c-1
        else:
                continue
print(c)             
