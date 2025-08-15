def isComposite(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return True
    return False

def isMagic(num):
    n = num
    sum = 0

    while n>0 or sum>9:
        if n == 0:
            n = sum
            sum = 0
      
        sum += n % 10
        n //= 10 

    return sum == 1
    
number = (int(input("Enter a Number = ")))
if isComposite(number) and isMagic(number):
    print(f"{number} is a Composite Magic Number")
else:
    print(f"{number} is not a Composite Magic Number")