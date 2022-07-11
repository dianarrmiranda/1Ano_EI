package aula02;
import java.util.Scanner;

public class coords {
    public static void main(String[] args){
        double x1, y1,x2, y2, d, x, y;
        Scanner sc = new Scanner(System.in);
        System.out.print("Ponto 1 x: ");
        x1 = sc.nextDouble();
        System.out.print("Ponto 1 y: ");
        y1 = sc.nextDouble();
        System.out.print("Ponto 2 x: ");
        x2 = sc.nextDouble();
        System.out.print("Ponto 2 y: ");
        y2 = sc.nextDouble();

        x = Math.pow(x2-x1, 2);
        y =  Math.pow(y2-y1, 2);
        d = Math.sqrt(x+y); 

        System.out.println("Distância entre pontos: " + d);
        sc.close();

    }
    
}
