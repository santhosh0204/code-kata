s=int(raw_input())
a=0
for i in range(2,s//3):
    if(s%i==0):
        a=a+1
if(a<=0):
    print("yes")
else:
    print("no")
