##x=input("enter a string").lower()
s=0
q=0
x=input().lower()
y=input().lower()
a=list(x)
b=list(y)

for i in range(len(a)):
        r=((ord(a[i])))
        s=s+r

for j in range(len(b)):
        t=((ord(b[j])))
        q=q+t

if s==q:
        print("0")
elif s<q:
        print("-1")
else:
        print("1")

#alternate and easier one
'''m = input().lower()
n = input().lower()
if m == n:
    print("0")
elif m > n :
    print("1")
else:
    print ("-1")'''
