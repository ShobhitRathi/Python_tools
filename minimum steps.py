x=int(input())
i=0
while x>i:
        if x>=5:
                x,y=x//5,x%5
                if 3<y<=4:
                        z=y//4
                        print(x+z)
                elif 2<y<=3:
                        z=y//3
                        print(x+z)
                elif 1<y<=2:
                        z=y//2
                        print(x+z)
                elif 0<y<=1:
                        z=y//1
                        print(x+z)
                else:
                        print(x)
        elif x<=4:
                print(x-(x-1))
        break
