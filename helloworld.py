# print('hello world')

counter = 0
myName = 'Edith'

# print(counter + myName)
# cannot add a number and a string

# print(counter, myName)

a = b = c = 1

d, e, f = 2, 3, "john"

# print('a', a)
# print('b', b)
# print('c', c)
# print('d', d)
# print('e', e)
# print('f', f)


#---------STRINGS---------------
str = 'Hello World!'

# print (str)          # Prints complete string
# print (str[0])       # Prints first character of the string
# print (str[2:5])     # Prints characters starting from 3rd to 5th
# print (str[2:])      # Prints string starting from 3rd character
# print (str * 2)      # Prints string two times
# print (str + "TEST") # Prints concatenated string


#---------LISTS---------------

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

# print (list)          # Prints complete list
# print (list[0])       # Prints first element of the list
# print (list[1:3])     # Prints elements starting from 2nd till 3rd 
# print (list[2:])      # Prints elements starting from 3rd element
# print (tinylist * 2)  # Prints list two times
# print (list + tinylist) # Prints concatenated lists


#---------TUPLE--------------

# a tuple is a finite ordered list of elements.
# it cannot be updated
# think of it as a read-only list
# uses parentheses instead of brackets 

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

# print (tuple)           # Prints complete tuple
# print (tuple[0])        # Prints first element of the tuple
# print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
# print (tuple[2:])       # Prints elements starting from 3rd element
# print (tinytuple * 2)   # Prints tuple two times
# print (tuple + tinytuple) # Prints concatenated tuple



#---------DICTIONARIES--------------
#basically an object

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
tinydict['myName'] = 'Edith'

# print (dict['one'])       # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (tinydict)          # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values



#--------------FUNCTIONS AND CONDITIONALS------------
#function
def sum( a, b ):
   "This adds 2 numbers together"
   sum = a + b
   print(sum)
#formatting is extremely important! indent indicates what is in the function
# sum(1,2)

#conditional

def cond( var ) :
    if ( var  == 100 ) : 
        return  ("Value of expression is 100")
    elif (var == 4 ) : 
        return ("Value of expression is 4")
    else: return  ("Good bye!")

# print(cond(4))

def reverseAString ( string ) :
    return string[::-1]
    
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
print(reverse('hello world'))


