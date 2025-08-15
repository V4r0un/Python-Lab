def SumofDigits(num):
    sum = 0
    while num > 0:
        sum += (num % 10)
        num //= 10
    return sum

def SumofPrimeFactor(num):
    i = 2
    sum = 0
    while num > 1:
        if num % i == 0:
            sum += SumofDigits(i)
            num //= i
        else:
            i+=1
    return sum

number = (int(input("Enter a Number = ")))
a = SumofDigits(number)
b = SumofPrimeFactor(number)
print("Sum of Digits = ", a)
print("Sum of Prime Factors = ", b)
if a == b:
    print(f"{number} is a Smith Number")
else:
    print(f"{number} is not a Smith Number")