// Miller–Rabin primality test
import java.lang.*;

public class Main {
  public static boolean isPrime(int num){
    if ((num == 0) || (num == 1)){
      return true;
    }

    if ((num % 2 == 0) || (num % 3 == 0)){
      return false;
    }

    int sqrt_num = (int) Math.floor(Math.sqrt(num));

    // for i in range(sqrt_num, 1, -1):
    //     if num % i == 0:
    //         return False

    for (int i = sqrt_num; i > 2; i--){
      if (num % i == 0){
        return false;
      }
    }

    return false;
  }

  public static void main(String[] args) {
    System.out.println("isPrime(0) = " + isPrime(0));
    System.out.println("isPrime(1) = " + isPrime(1));
    System.out.println("isPrime(2) = " + isPrime(2));
    System.out.println("isPrime(3) = " + isPrime(3));
    System.out.println("isPrime(9) = " + isPrime(9));
    System.out.println("isPrime(49) = " + isPrime(49));
    System.out.println("isPrime(51) = " + isPrime(51));
    System.out.println("isPrime(7919) = " + isPrime(7919));
  }
}
