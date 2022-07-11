package aula02;
import java.util.Scanner;

public class Miles {
    public static void main(String[] args) {
        double km;
        double miles;
        Scanner sc = new Scanner(System.in);
        System.out.print("Quilómetros: ");
        km = sc.nextDouble();
        miles = km/1.609;
        System.out.format("%.2f km em são %.2f milhas.", km, miles);
        sc.close();
    }
    
}
