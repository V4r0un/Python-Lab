num = [1,2,3,4,5,6,7,8,9,10]
lower = 0
upper = len(num) - 1
element = 5
mid = 0
flag = 0
while lower <= upper:
    mid = (lower + upper) // 2
    if num[mid] > element:
        upper = mid - 1
    elif num[mid] < element:
        lower = mid + 1
    elif num[mid] == element:
        flag = 1
        break

if flag == 1:
    print("Element found successfully")
else:
    print("Element not found")
