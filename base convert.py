x=int(input("enter a number:"))
a=[]

while x>0:
        y=x%8
        a.append(y)
        x=x//8
        
a.reverse()

for i in a:
        print(i, end="")

