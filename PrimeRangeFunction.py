def isPrime(num):
    is_prime = True
    if num <= 1:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            return True
        else:
            return False
        

number = (int(input("Enter a number = ")))
if isPrime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a prime number.")
