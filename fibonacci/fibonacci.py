# fibonacci.py
import math

def fibRecursive(n):
    """Return the n-th fibonacci number. Uses recursion to get the two previous entries
    
    This verstion is simplest to code, but by far the longest to run.
    Problems:
    * Runtime is exponential
    * the number of additions made for n is equal to n-2 + n-1.
    * runtime ~~ 0.7424 * 1.616^(input)
        * Note 1.616 is very close to the golden ratio
    * fibRecursive(n-1) already contains fibRecursive(n-2) so you're overrunning your own work

    Parameters
    ----------
    n : int
        The n-th number you want in the fibonacci sequence. 0,1,1,2,3,5,8,...
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibRecursive(n-2) + fibRecursive(n-1)

def fibIterative(n):
    """Return the n-th fibonacci number. Use an iterative method.

    Advantages:
    * Runtime is O(n) or linear time.
        * The number of additions is equal to the input number. 
        * As n grows so does the number of additions

    Problems:
    * Uses a giant array
    * Any number in the array that is not the last one is wasted memory space
    
    Parameters
    ----------
    n : int
        The n-th number you want in the fibonacci sequence. 0,1,1,2,3,5,8,...
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[len(arr)-1]
    
def fibTwoVars(n):
    """Return the n-th fibonacci number. Using an iterative method with two variables

    Advantages:
    * Runtime is O(n) or linear time.
        * The number of additions is equal to the input number. 
        * As n grows so does the number of additions
    * Memory is localized to only a small set of variables:
        * n - the number I want in the fib sequence
        * x - a var used to hold a number in the fib sequence
        * y - another var used to hold a number in the fib sequence

    Parameters
    ----------
    n : int
        The n-th number you want in the fibonacci sequence. 0,1,1,2,3,5,8,...
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = 0
    y = 1
    for i in range(2, n+1):
        if i % 2 == 0:
            x = x + y
        else:
            y = x + y
    if n % 2 == 0:
        return x
    else:
        return y

def fibBinet(n):
    """Return the n-th fibonacci number. Use an iterative method.

    Advantages:
    * Runtime is O(1) or constant time.

    Problems:
    * After number 71 this formula begins to produce incorrect results
        * Because (((1+math.sqrt(5)) / 2)**n) gets very large and ((1-math.sqrt(5)) / 2)**n) gets very small lopping off
    * TODO: find a better method of handling these numbers that require more precision

    Parameters
    ----------
    n : int
        The n-th number you want in the fibonacci sequence. 0,1,1,2,3,5,8,...
    """
    return round(((((1+math.sqrt(5)) / 2)**n) - ((1-math.sqrt(5)) / 2)**n) / math.sqrt(5))

def testFunction(f):
    print('Testing ' + str(f.__name__))
    print('-'*len('Testing ' + str(f.__name__)))
    print(str(help(f)).replace('None','').strip('\n'))
    print('')
    print('vvv 0 to 16: vvv')
    print('-'*len('vvv 0 to 16: vvv'))
    for i in range(16+1):
        print(str(f.__name__) + '('+str(i)+') = ' + str(f(i)))
    print('')

    print('vvv OTHER: vvv')
    print('-'*len('vvv RANDOM: vvv'))
    print('isPowerOfTwo(50) = ' + str(f(50)))
    print('')

def main():
    testFunction(fibRecursive)
    testFunction(fibIterative)
    testFunction(fibTwoVars)
    testFunction(fibBinet)

if __name__ == "__main__":
    print('BEGIN')
    main()
    print('END')
