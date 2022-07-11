package aula03;

import java.util.Scanner;

public class ex03Primo {
    public static void main(String[] args){
        int n, nn;
        int div = 0;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.print("Número: ");
            n = sc.nextInt();
            if (n<0){
                System.out.println("Insira um número válido! (Inteiro positivo)");
            }
        }while (n<0);
        nn = n;
        while(n>0){
            if (nn%n == 0){
                div++;
            } 
            n--;
        }
        if (div == 2){
            System.out.println("É primo!");
        }else{
            System.out.println("Não é primo!");
        }
        sc.close();
    }
}
