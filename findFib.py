def findFib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return findFib(n-1) + findFib(n-2)

print findFib(9)
print findFib(8)
print findFib(7)
print findFib(6)
