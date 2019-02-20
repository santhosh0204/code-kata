print("WELCOME TO STACK")
l=[]
while True:
    print("PLEASE SELECT THE OPERATION\n1.Push,2.Pop,3.Size,4.Emptiness,5.Exit")
    a=input()
    a=int(a)
    b=len(l)
    if a==1:
        print("ENTER THE NUMBER YOU WANT TO ADD")
        element=input()
        l.append(element)
        print(l)
    elif a==2:
        if b==0:
            print("POP THE NUMBER")
        else:
            print("pop the number")
            l.pop()
            print(l)
    elif a==3:
            print("SIZE OF THE STACK")
            print(len(l))
            print(l)
    elif a==4:
        if b==0:
            print("STACK IS EMPTY")
        else:
            print("STACK IS NOT EMPTY")
    elif a==5:
            print("EXIT")
           
    elif a>=6:
            print("PLEASE SELECT THE ABOVE OPTION")
