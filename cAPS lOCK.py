x=input()

if x[0].islower() and x[1:].isupper():
        y=x[0].upper()
        z=x[1:].lower()
        print(y+z)

elif x[0].islower() and x[1:].islower() and x[1:].isupper():
        y=x[0].upper()
        print(y+x[1:])

elif x.isupper():
        y=x.lower()
        print(y)

elif x[0].islower() and len(x)==1:
        print(x[0].upper())

else:
        print(x)
