import pdb
def palindrome(num):
    num = str(num)
    return num == num[::-1]
palin = 100
for i in range(100,999):
    for j in range(100,999):
        if palindrome(i*j) and (i*j) > palin:
            palin = i*j
print palin
"""
palins = [j for i in range(100,999) for j in range(100,999) if palindrome(i*j)]
pdb.set_trace()
print max(palins)
"""