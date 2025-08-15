num = (int(input("Enter a Number = ")))
temp = num
reverse = 0
while temp != 0:
    reverse = reverse * 10 + (temp % 10)
    temp //= 10
if reverse == num:
    print(f"{num} is a Palindrome Number")
else:
    print(f"{num} is not a Palindrome Number") 