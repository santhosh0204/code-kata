print("                                                                 ^^^^^^^^^^^WELCOME TO CARHUB^^^^^^^^^^^^^")
place=["tambaram","adayar","ambathur"]
distance=[35,30,50]
print("PLEASE SELECT YOUR DESTINATION\n1.tamabaram,2.adayar,3.ambathur")
place=int(input())
if place==1:
    kms=distance[0]
elif place==2:
    kms=distance[1]
elif place==3:
    kms=distance[2]
print("please select the type of car\n 1.nano,2.micro,3.mini,4.prime")
nano=5
micro=8
mini=9
prime=15
choice=int(input())
if choice==1:
    c=kms*nano
if choice==2:
    c=kms*micro
if choice==3:
    c=kms*mini
if choice==4:
    c=kms*prime
print("the price for your ride is",c)

