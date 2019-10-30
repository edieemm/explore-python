print "Hello World"

def fizzBuzz(num):
    if num % 15 == 0:
        return 'fizzBuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz'
    else:
        return num

print fizzBuzz(15)
print fizzBuzz(5)
print fizzBuzz(3)
print fizzBuzz(8)
print fizzBuzz(input())
