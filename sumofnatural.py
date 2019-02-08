S = int(raw_input())
if S < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(S > 0):
       sum += S
       S -= 1
   print(sum)
