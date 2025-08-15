num = (int(input("Enter the limit = ")))
a = 0
b = 1
print(a)
print(b)
sum = 0
for i in range(3, num+1):
    sum = a + b
    print(sum)
    a = b
    b = sum