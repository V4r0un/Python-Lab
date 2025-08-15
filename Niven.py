num = (int(input("Enter a Number = ")))
temp = num
sum = 0
while temp != 0:
    sum += (temp%10)
    temp //= 10
if num % sum == 0:
    print(f"{num} is a Niven Number")
else:
    print(f"{num} is not a Niven Number") 