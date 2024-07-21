import java.util.*;

/**
 * This class checks if a given year is a leap year or not.
 */

public class Check_Leap_Year {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the year: ");
        int year = scan.nextInt();
        if (year % 4 == 0) {
            if (year % 100 == 0) {
                if(year % 400 == 0) {
                    System.out.println(year + " is a leap year.");
                }
                else {
                    System.out.println(year + " is not a leap year.");
                }
            }
            else {
                System.out.println(year + " is a leap year.");
            }
        }
        else {
            System.out.println(year + " is not a leap year.");
        }
        scan.close();
    }
}
