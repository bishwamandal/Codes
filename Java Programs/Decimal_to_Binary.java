import java.util.Scanner;

/**
 * This class converts decimal numbers to binary and vice versa.
 */

public class Decimal_to_Binary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dec = 0, bin = 0, temp = 0, i = 0;
        System.out.print("1. Decimal to Binary\n2. Binary to Decimal\nEnter choice: ");
        int choice = sc.nextInt();
        switch (choice) {
            case 1:
                System.out.println("Enter decimal number: ");
                dec = sc.nextInt();
                temp = dec;
                while (temp > 0) {
                    bin = bin + (temp % 2) * (int) Math.pow(10, i);
                    temp /= 2;
                    i++;
                }
                System.out.println("Binary equivalent of " + dec + " is " + bin);
                break;
            case 2:
                System.out.println("Enter binary number: ");
                bin = sc.nextInt();
                temp = bin;
                while (temp > 0) {
                    dec = dec + (temp % 10) * (int) Math.pow(2, i);
                    temp /= 10;
                    i++;
                }
                System.out.println("Decimal equivalent of " + bin + " is " + dec);
                break;
            default:
                System.out.println("Invalid choice!");
        }
        sc.close();
    }
}
