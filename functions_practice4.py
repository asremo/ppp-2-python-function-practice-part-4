""" 1   Write a Python function called max_num()to 
find the maximum of three numbers.  """

def max_num(x, y, z):
    return max([x, y, z])

print(max_num(1, 2, 4))
print(max_num(10, 20, 30))

""" 2   Write a Python function called mult_list() to
multiply all the numbers in a list.    """

def mult_list(list):
    total = 1
    for x in list:
        total *= x
    return total

print(mult_list((2, 4, 6)))
print(mult_list((1, 1, 1)))
print(mult_list((1, 0, 1)))

# OR

def mult_list(list):
    if len(list) == 0:    # if list is empty
        return 0
    num = list[0]   # start with index 0 of list
    if len(list) > 1:
        for i in list[1:]:
            num = num * i
    return num

print(mult_list([2, 4, 6]))
print(mult_list([1, 1, 1]))

""" 3   Write a Python function called rev_string() to reverse a string. """

def rev_string(str):
    return str[::-1]    # [::-1] is a slice statement
    #   means start at the end of the string and end at position 0, move with 
    #   the step -1, negative one, which means one step backwards.

print(rev_string("Hello"))
print(rev_string("Amanda"))

""" 4   Write a Python function called num_within() to check whether a number
falls in a given range. """
""" The function accepts the number, beginning of range, and end of range
(inclusive) as arguments.   """
""" Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, 
num_within(10,2,5) returns False.   """ 
# because num_within(3, 1, 3) returns true then the range of y has to be + 1 -> range(x, y + 1)
# without the + 1, it will be false because the range of 3 is 0, 1, 2
# range of 4 is 0, 1, 2, 3 so 3 will be in range making it false
 
def num_within(a, x, y):
    return a in range(x, y + 1)     #   range(beginning, end)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

""" 5   Write a Python function called pascal() that prints out the first 
n rows of Pascal's triangle.    """
""" The function accepts the number n, the number of rows to print. """




