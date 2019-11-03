a=0
b=1
s=0
print("###### WELCOME TO FIBONACCI CALCULATOR ######")
print("---------------------------------------------")
n=int(input("select your range for fibonacci serquence: "))

for i in range(n):
        s=a+b
        a=b
        b=s
        print(s, end=" ")
