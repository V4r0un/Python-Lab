num = (int(input("Enter a number = ")))
flag = 0
for i in range(1, num+1):
    if i * (i + 1) == num:
        flag = 1
        break
if flag == 1:
    print(f"{num} is a Pronic Number")
else:
    print(f"{num} is not a Pronic Number")