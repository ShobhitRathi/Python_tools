x=eval(input("enter list"))
print(x)
for i in range(1,len(x)):
        k=x[i]
        j=i-1
        while j>=0 and k<x[j]:
                x[j+1]=x[j]
                j=j-1
        else:
                x[j+1]=k
print("after sorting")
print(x)
