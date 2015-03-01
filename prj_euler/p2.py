a = 1
b = 2
fibo  = [b]
i = 2
while True:
    i += 1
    c = a + b
    if c < 4000000:
        a = b
        b = c
        if i % 2 == 0:
            fibo.append(c)
        print "{}th term is {}".format(i,c)
    else:
        break
print fibo
sum = 0
for h in fibo:
    sum = sum + h
print "SUm is {}".format(sum)

def sum_even_fib(n):
    sumfib = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b % 2 == 0:
            sumfib = sumfib + b
    return sumfib

print(sum_even_fib(4000000))
