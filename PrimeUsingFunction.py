def isPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2 , num):
            if num % i == 0:
                return False
            return True
        
num = (int(input("Enter a number = ")))
if isPrime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")