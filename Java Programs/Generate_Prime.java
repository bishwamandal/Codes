import java.util.Scanner;

/**
 * This class generates prime numbers within a given range.
 */

public class Generate_Prime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i, j;
        System.out.print("Enter range (1 - n):");
        int n = sc.nextInt();
        for (i = 2; i <= n; i++) {
            for (j = 2; j <= i; j++) {
                if (i % j == 0)
                    break;
            }
            if (i == j)
                System.out.println(i);
        }
        sc.close();
    }
}