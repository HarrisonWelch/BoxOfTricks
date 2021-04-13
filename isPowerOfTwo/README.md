# isPowerOfTwo

## Description
There is a very fast way to determine if a number is a power of two using bitwise AND

```python
x & (x-1) == 0
```

## Explanation
* Bitwise AND `&` serve to convert the integer into binary and compare each digit one-by-one.
  * If the 1 lines up with another 1, it will produce a 1. Otherwise return 0.
  * 1 & 1 = 1
  * 1 & 0 = 0
  * 0 & 1 = 0
  * 0 & 0 = 0

##### Example 1
* In this example, n = 6
* 6 in binary is 110
* 5 in binary is 101
```
  0 1 1 0
& 0 1 0 1
-----------
  0 1 0 0
```
* The result is 100 so the number 6 is **NOT** a power of two

##### Example 2
* In this example, n = 8
* 8 in binary is 1000
* 7 in binary is 111
```
  1 0 0 0
& 0 1 1 1
-----------
  0 0 0 0
```
* The result is 0 so the number 8 is a power of two

## Alternative
You can also use logarithms with a base of 2 and if the result is an integer, then the input was a power of two. The below code takes the log base 2 of x and then compares to the floor of itself. The floor being the number rounded down to the nearest whole number. If the two numbers in the comparison are equal than there was no difference and the number is whole. Thus the input is a power of two.

```python
math.log(x,2) == math.floor(math.log(x,2)
```

##### Example 1
* In this example, n = 6
* math.log(6,2) = 2.584962500721156...
* math.floor(math.log(6,2)) = 2
* Since 2.584... does not equal 2, 6 is **NOT** a power of two

##### Example 2
* In this example, n = 8
* math.log(3,2) = 3.0
* math.floor(math.log(8,2)) = 3
* Since 3.0 equals 3, 8 is a power of two

## Code
```python
import math

def isPowerOfTwo(x):
    """Return wether or not x is a power of two

    A simple function to see if an integer is a power of 2
    ex: 2^0 = 1, 2^1 = 2, 2^2 = 4, and so on...
    """
    return ( x != 0 ) and ( abs(x) & (abs(x)-1) == 0 )

def isPowerOfTwoV2(x):
    """Return wether or not x is a power of two using logarithms

    A simple function to see if an integer is a power of 2
    ex: 2^0 = 1, 2^1 = 2, 2^2 = 4, and so on...
    """
    return ( x != 0 ) and ( math.log(abs(x),2) == math.floor(math.log(abs(x),2)) )

def testFunction(f):
    print('Testing ' + str(f.__name__))
    print('-'*len('Testing ' + str(f.__name__)))
    print(str(help(isPowerOfTwo)).replace('None','').strip('\n'))
    print('')
    print('vvv 0 to 16: vvv')
    print('-'*len('vvv 0 to 16: vvv'))
    for i in range(16+1):
        print('isPowerOfTwo('+str(i)+') = ' + str(f(i)))
    print('')

    print('vvv 0 to -16: vvv')
    print('-'*len('vvv 0 to -16: vvv'))
    for i in range(0,-16-1,-1):
        print('isPowerOfTwo('+str(i)+') = ' + str(f(i)))
    print('')

    print('vvv OTHER: vvv')
    print('-'*len('vvv RANDOM: vvv'))
    print('isPowerOfTwo(63) = ' + str(f(63)))
    print('isPowerOfTwo(64) = ' + str(f(64)))
    print('isPowerOfTwo(127) = ' + str(f(127)))
    print('isPowerOfTwo(128) = ' + str(f(128)))
    print('isPowerOfTwo((2**1234567890)-1) = ' + str(f(pow(2,1234567890)-1)))
    print('isPowerOfTwo(2**1234567890) = ' + str(f(pow(2,1234567890))))
    print('')

def main():
    testFunction(isPowerOfTwo)
    # testFunction(isPowerOfTwoV2)

if __name__ == "__main__":
    print('-'*50)
    print('BEGIN')
    print('')
    print(str(help(isPowerOfTwo)).replace('None','').strip('\n'))
    print('')
    main()
    print('')
    print('END')
    print('-'*50)
```

## Output

```
--------------------------------------------------
BEGIN

Help on function isPowerOfTwo in module __main__:

isPowerOfTwo(x)
    Return wether or not x is a power of two

    A simple function to see if an integer is a power of 2
    ex: 2^0 = 1, 2^1 = 2, 2^2 = 4, and so on...



Testing isPowerOfTwo
--------------------
Help on function isPowerOfTwo in module __main__:

isPowerOfTwo(x)
    Return wether or not x is a power of two

    A simple function to see if an integer is a power of 2
    ex: 2^0 = 1, 2^1 = 2, 2^2 = 4, and so on...


vvv 0 to 16: vvv
----------------
isPowerOfTwo(0) = False
isPowerOfTwo(1) = True
isPowerOfTwo(2) = True
isPowerOfTwo(3) = False
isPowerOfTwo(4) = True
isPowerOfTwo(5) = False
isPowerOfTwo(6) = False
isPowerOfTwo(7) = False
isPowerOfTwo(8) = True
isPowerOfTwo(9) = False
isPowerOfTwo(10) = False
isPowerOfTwo(11) = False
isPowerOfTwo(12) = False
isPowerOfTwo(13) = False
isPowerOfTwo(14) = False
isPowerOfTwo(15) = False
isPowerOfTwo(16) = True

vvv 0 to -16: vvv
-----------------
isPowerOfTwo(0) = False
isPowerOfTwo(-1) = True
isPowerOfTwo(-2) = True
isPowerOfTwo(-3) = False
isPowerOfTwo(-4) = True
isPowerOfTwo(-5) = False
isPowerOfTwo(-6) = False
isPowerOfTwo(-7) = False
isPowerOfTwo(-8) = True
isPowerOfTwo(-9) = False
isPowerOfTwo(-10) = False
isPowerOfTwo(-11) = False
isPowerOfTwo(-12) = False
isPowerOfTwo(-13) = False
isPowerOfTwo(-14) = False
isPowerOfTwo(-15) = False
isPowerOfTwo(-16) = True

vvv OTHER: vvv
---------------
isPowerOfTwo(63) = False
isPowerOfTwo(64) = True
isPowerOfTwo(127) = False
isPowerOfTwo(128) = True
isPowerOfTwo((2**1234567890)-1) = False
isPowerOfTwo(2**1234567890) = True


END
--------------------------------------------------
```
