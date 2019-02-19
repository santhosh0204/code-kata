s,a=raw_input().split()
s=int(s)
a=int(a)
for num in range(s+1,a):
    order = len(str(num))
    sum = 0
    temp = num
    while temp >0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num),
