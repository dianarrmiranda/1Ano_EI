package aula03;

import java.util.Scanner;

public class ex02Decres {
    public static void main(String[] args){
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.print("Número: ");
        n = sc.nextInt();
        while(n<0){
            System.out.println("Insira um número válido!! (Positivo)");
            System.out.print("Número: ");
            n = sc.nextInt();
        }
        
        while (n>=0){
            System.out.println(n);
            n--;
        }
        sc.close();
    }
}
