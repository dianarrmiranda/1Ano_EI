package aula02;
import java.util.Scanner;

public class catetos {
    public static void main(String[] args){
        double A, B, C, ang;
        Scanner sc = new Scanner(System.in);
        System.out.print("Cateto A: ");
        A = sc.nextDouble();
        System.out.print("Cateto B: ");
        B = sc.nextDouble();

        C = Math.sqrt(Math.pow(A, 2) +Math.pow(B, 2)); 
        ang = Math.toDegrees(Math.asin(A/C));

        System.out.format("C = %.2f %n", C);
        System.out.format("Angulo = %.2fº", ang);
        sc.close();

    }
}

