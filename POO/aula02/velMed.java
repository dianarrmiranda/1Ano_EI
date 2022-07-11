package aula02;
import java.util.Scanner;

public class velMed {
    public static void main(String[] args){
        float v1, d1, v2, d2, vm, t1, t2;
        Scanner sc = new Scanner(System.in);
        System.out.print("Velocidade 1? ");
        v1 = sc.nextFloat();
        System.out.print("Distância 1? ");
        d1 = sc.nextFloat();
        System.out.print("Velocidade 2? ");
        v2 = sc.nextFloat();
        System.out.print("Distância 2? ");
        d2 = sc.nextFloat();

        t1= d1/v1;
        t2= d2/v2;

        vm= (d2+d1)/(t2+t1);

        System.out.println("Velocidade Média = " + vm);
        sc.close();

    }
    
}
