import java.util.Scanner;

/**
 * This class calculates the n-th Fibonacci number.
 */

public class Fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        int a = -1, b = 1, c = 0;
        for (int i = 0; i < n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        System.out.print(n + "-th Fibonacci number is: " + c);
        sc.close();
    }    
}
