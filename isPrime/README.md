# isPrime

## Description
There exists an algorithm to quickly find whether or not an integer is a prime. If a number `n` is not prime there exists another number `m` less than or equal to the square root of `n`.

## Algorithm Basics
* If a number is 0 or 1, the number is prime
* If a number is divisibile by 2 or 3 return false as the number is not prime
  * This is to save time mostly, half of all integers are divisble by 2 and similary a third of numbers are divisible by 3
* Take the square root of the target number `n`
* Loop backwards from the square root `i` down to 4
  * Test if `n` is divisible by `i`
    * If it is return true immediately as we found a number `i` that divides the target number `n`
  * Decrement `i` by 1
  * Loop again

## Code
```python
# Miller–Rabin primality test
import math

def is_prime(num):
    if num == 0 or num == 1:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False

    sqrt_num = math.floor(math.sqrt(num))

    for i in range(sqrt_num, 1, -1):
        if num % i == 0:
            return False

    return True

def main():
    print('is_prime(0) = ' + str(is_prime(0)))
    print('is_prime(1) = ' + str(is_prime(1)))
    print('is_prime(2) = ' + str(is_prime(2)))
    print('is_prime(3) = ' + str(is_prime(3)))
    print('is_prime(9) = ' + str(is_prime(9)))
    print('is_prime(49) = ' + str(is_prime(49)))
    print('is_prime(51) = ' + str(is_prime(51)))
    print('is_prime(7919) = ' + str(is_prime(7919)))

if __name__ == "__main__":
    main()
```

## Output
```
is_prime(0) = True
is_prime(1) = True
is_prime(2) = False
is_prime(3) = False
is_prime(9) = False
is_prime(49) = False
is_prime(51) = False
is_prime(7919) = True
```
