num = (int(input("Enter a Number = ")))
sum = 0
product = 1
temp = num
while temp != 0:
    digit = temp % 10
    sum += digit
    product *= digit
    temp //= 10
if sum == product:
    print(f"{num} is a Spy Number")
else:
    print(f"{num} is not a Spy Number")