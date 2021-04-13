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
