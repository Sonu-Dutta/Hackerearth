t=int(input())
while(t>0):
    n=int(input())
    if n%12==1:
        print(str(n+11)+" WS")
    elif n%12==0:
        print(str(n-11)+" WS")
    elif n%12==6:
        print(str(n+1)+" WS")
    elif n%12==7:
        print(str(n-1)+" WS")
    elif n%12==2:
        print(str(n+9)+" MS")
    elif n%12==11:
        print(str(n-9)+" MS")
    elif n%12==5:
        print(str(n+3)+" MS")
    elif n%12==8:
        print(str(n-3)+" MS")
    elif n%12==3:
        print(str(n+7)+" AS")
    elif n%12==10:
        print(str(n-7)+" AS")
    elif n%12==4:
        print(str(n+5)+" AS")
    elif n%12==9:
        print(str(n-5)+" AS")
    t=t-1