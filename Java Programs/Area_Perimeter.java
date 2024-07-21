import java.util.Scanner;

/**
 * This class calculates the area and perimeter of a circle.
 */

public class Area_Perimeter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float area = 0, peri = 0;
        System.out.print("Enter the radius of the circle: ");
        float r = sc.nextInt();
        area = (float) (Math.PI * r * r);
        peri = (float) (2 * Math.PI * r);
        System.out.println("Area of the circle: " + area);
        System.out.println("Perimeter of the circle: " + peri);
        sc.close();
    }
}
