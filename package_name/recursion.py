def sum_array(array):
    '''Return sum of all items in array'''
    sum = 0
    for num in array:
        sum += num
    return sum;


def Fibonacci(n):
    ''' Return nth term in fibonacci sequence'''
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b

def factorial(n):
    '''Return n!'''
    if n <1:   # base case
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

def reverse(word):
     '''Return word in reverse'''
     return word[-1::-1]
