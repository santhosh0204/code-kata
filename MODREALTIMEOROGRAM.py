print("                                                                      ^^^^^^^^^^^WELCOME TO CARHUB^^^^^^^^^^^^^")
lis=[]
places=["Tambaram","Adayar","Ambathur"]
distance=[35,30,50]
print("            ************PLEASE SELECT YOUR DESTINATION*************\n1.Tamabaram,2.Adayar,3.Ambathur")
place=int(input())
if place==1:
    kms=distance[0]
elif place==2:
    kms=distance[1]
elif place==3:
    kms=distance[2]
print("            ~~~~~~~~~~~~~Please Select The Type Of Car~~~~~~~~~~~~~~~\n1.<<Nano>>,2.<<Micro>>,3.<<Mini>>,4.<<Prime>>")
cartype=["Nano","Micro","Mini","Prime"]
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
print("please conform booking\n 1.yes,2.no")
stat=int(input())
if stat==1:
    print("Yes")
else:
    print("No")
print("                                                                   price for your ride ",c)
print("                                                                  selected location",places[place-1])
print("                                                                   distance traveled",kms)
print("                                                                   selected cab ",cartype[choice-1])
