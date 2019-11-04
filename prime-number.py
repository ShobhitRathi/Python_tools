x=int(input("enter"))

for i in range(2,x):
        z=x%i
        if z!=0:
                f=0
        else:
                f=1
                break

if f==0:
        print("prime")
else:
        print("composite")
