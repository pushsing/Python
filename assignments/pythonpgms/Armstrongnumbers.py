l=int(input("Enter interval starting: "))
u=int(input("Enter interval ending: "))
for num in range(l, u + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)