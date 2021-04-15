# fibonacci

## Description
* An exploration of functions used to calculate the fibonacci sequence

## Method 1 - Recursive
* n is input indicating the nth number asked for in the fibonacci sequence
* If n is 0, return 0 - the first number in the fib sequence
* If n is 1, return 1 - the second number in the fib sequence
* Now recursively call this function twice
  * Once for n-2
  * Once for n-1
  * Then add both recursive calls and return the result

## Method 2 - Iterative, Array
* n is input indicating the nth number asked for in the fibonacci sequence
* If n is 0, return 0 - the first number in the fib sequence
* If n is 1, return 1 - the second number in the fib sequence
* Create a array starting with the first two numbers in the fib sequence
* Starting from the 2nd index, loop until n is reached
  * Each time add the previous two array values and append them to the back
* Return the number at the last index in the array

## Method 3 - Iterative, Two Variables
* `n` is input indicating the nth number asked for in the fibonacci sequence
* If n is 0, return 0 - the first number in the fib sequence
* If n is 1, return 1 - the second number in the fib sequence
* Create two variables
  * `x` set to 0
  * `y` set to 1
* Starting from the 2nd index, loop until n is reached using index variable `i`
  * If i is even set x to x plus y
  * If i is odd set y to x plus y
* If n is even return x
* Else return y

## Method 4 - [Binet's formula](https://discover.hubpages.com/education/Fibonacci-Sequence-and-Binets-Formula)
* `n` is input indicating the nth number asked for in the fibonacci sequence
* return the result of n being input into in the binet function
  * Take the floor of the floating point result

```
                       n                 n
       ( 1 + sqrt(5) )   ( 1 - sqrt(5) )
       ( ----------- ) - ( ----------- )
       (      2      )   (      2      )
f(n) = -----------------------------------
                    sqrt(5)
```

## Code
```python
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
```

## Output
```
C:\Users\hrwaf\OneDrive\Desktop\Harrison\PROJECTS\BoxOfTricks\fibonacci>python fibonacci.py
BEGIN
Testing fibRecursive
--------------------
Help on function fibRecursive in module __main__:

fibRecursive(n)
    Return the n-th fibonacci number. Uses recursion to get the two previous entries

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



vvv 0 to 16: vvv
----------------
fibRecursive(0) = 0
fibRecursive(1) = 1
fibRecursive(2) = 1
fibRecursive(3) = 2
fibRecursive(4) = 3
fibRecursive(5) = 5
fibRecursive(6) = 8
fibRecursive(7) = 13
fibRecursive(8) = 21
fibRecursive(9) = 34
fibRecursive(10) = 55
fibRecursive(11) = 89
fibRecursive(12) = 144
fibRecursive(13) = 233
fibRecursive(14) = 377
fibRecursive(15) = 610
fibRecursive(16) = 987

vvv OTHER: vvv
---------------
isPowerOfTwo(50) = 12586269025

Testing fibIterative
--------------------
Help on function fibIterative in module __main__:

fibIterative(n)
    Return the n-th fibonacci number. Use an iterative method.

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



vvv 0 to 16: vvv
----------------
fibIterative(0) = 0
fibIterative(1) = 1
fibIterative(2) = 1
fibIterative(3) = 2
fibIterative(4) = 3
fibIterative(5) = 5
fibIterative(6) = 8
fibIterative(7) = 13
fibIterative(8) = 21
fibIterative(9) = 34
fibIterative(10) = 55
fibIterative(11) = 89
fibIterative(12) = 144
fibIterative(13) = 233
fibIterative(14) = 377
fibIterative(15) = 610
fibIterative(16) = 987

vvv OTHER: vvv
---------------
isPowerOfTwo(50) = 12586269025

Testing fibTwoVars
------------------
Help on function fibTwoVars in module __main__:

fibTwoVars(n)
    Return the n-th fibonacci number. Using an iterative method with two variables

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



vvv 0 to 16: vvv
----------------
fibTwoVars(0) = 0
fibTwoVars(1) = 1
fibTwoVars(2) = 1
fibTwoVars(3) = 2
fibTwoVars(4) = 3
fibTwoVars(5) = 5
fibTwoVars(6) = 8
fibTwoVars(7) = 13
fibTwoVars(8) = 21
fibTwoVars(9) = 34
fibTwoVars(10) = 55
fibTwoVars(11) = 89
fibTwoVars(12) = 144
fibTwoVars(13) = 233
fibTwoVars(14) = 377
fibTwoVars(15) = 610
fibTwoVars(16) = 987

vvv OTHER: vvv
---------------
isPowerOfTwo(50) = 12586269025

Testing fibBinet
----------------
Help on function fibBinet in module __main__:

fibBinet(n)
    Return the n-th fibonacci number. Use an iterative method.

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



vvv 0 to 16: vvv
----------------
fibBinet(0) = 0
fibBinet(1) = 1
fibBinet(2) = 1
fibBinet(3) = 2
fibBinet(4) = 3
fibBinet(5) = 5
fibBinet(6) = 8
fibBinet(7) = 13
fibBinet(8) = 21
fibBinet(9) = 34
fibBinet(10) = 55
fibBinet(11) = 89
fibBinet(12) = 144
fibBinet(13) = 233
fibBinet(14) = 377
fibBinet(15) = 610
fibBinet(16) = 987

vvv OTHER: vvv
---------------
isPowerOfTwo(50) = 12586269025

END
```


