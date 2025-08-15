num = (int(input("Enter a number = ")))
temp = num
count = 0
square = num * num

while temp != 0:
    temp = temp // 10
    count+=1

end = square % pow(10, count)

if num == end:
    print(f"{num} is an Automorphic Number")
else:
    print(f"{num} is not an Automorphic Number")