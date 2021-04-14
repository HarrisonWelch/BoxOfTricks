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
