package aula03;

import java.util.Scanner;

public class ex04 {
    public static void main(String[] args){
        float n, n2, med, max, min;
        int i = 1;
        Scanner sc = new Scanner(System.in);
        System.out.print("Número: ");
        n = sc.nextFloat();
        med = n;
        max = n;
        min = n;
        do{
            System.out.print("Número: ");
            n2 = sc.nextFloat();
            if (n2>max){
                max = n2;
            }
            if (n2<min){
                min = n2;
            }
            med += n2;
            i++;
        }while(n2 != n);
        System.out.println("Valor máximo: " + max);
        System.out.println("Valor minímo: " + min);
        System.out.format("Média: %.1f %n", med/i);
        System.out.println("Total números: " + i);
        sc.close();
    }
    
}
