s,a=raw_input().split()
s=int(s)
a=int(a)
for num in range(s+1,a):
   if num > 1:
       for i in range(2,num):
           if(num % i== 0):
              break
       else:
           print(num),
          
