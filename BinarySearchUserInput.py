input_list = input("Enter sorted numbers separated by spaces: ")
arr = list(map(int, input_list.strip().split()))
arr.sort()
target = int(input("Enter the number to search for: "))
low = 0
high = len(arr) - 1
found = False
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print(f"Number found at index {mid}")
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Number not found in the list")
