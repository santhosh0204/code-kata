print("WELCOME TO QUEUE")
l=[25,26,27,28]
while True:
    print("PLEASE SELECT THE OPERATION\n1.ENQUEUE,2.DEQUEUE,3.Size,4.Emptiness,5.Exit")
    a=input()
    a=int(a)
    b=len(l)
    if a==1:
        print("ENTER THE NUMBER YOU WANT TO ADD\n1.FRONT,2.REAR")
        c=input()
        c=int(c)
        element=input()
        if c==1:
            l.insert(0,element)
            print(l)
        elif c==2:
            l.append(element)
            print(l)
    elif a==2:
        if b==0:
            print("CANNOT REMOVE THE ELEMENT BECAUSE QUEUE IS EMPTY")
        else:
            print("ENTER WHERE YOU WANT TO REMOVE\n1.FRONT,2.REAR")
            d=input()
            d=int(d)
            if d==1:
                l.pop(0)
                print(l)
            elif d==2:
                l.pop()
                print(l)
    elif a==3:
            print("SIZE OF THE QUEUE")
            print(len(l))
            print(l)
    elif a==4:
        if b==0:
            print("QUEUE IS EMPTY")
        else:
            print("QUEUE IS NOT EMPTY")
    elif a==5:
            print("EXIT")
            break;
    elif a>=6:
            print("PLEASE SELECT THE ABOVE OPTION")
        

