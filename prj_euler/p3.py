import math

def is_prime(num):
    for i in range(3,num):
        if num % i == 0:
            return False
    return True


num = int(raw_input("Enter the number: "))
sqroot = int(math.sqrt(num) + 1)
result = 1
for i in range(2, sqroot):
    if num%i == 0 and is_prime(i):
        result = i
print result

