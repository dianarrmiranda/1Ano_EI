package aula02;
import java.util.Scanner;

public class fundoInv {
    public static void main(String[] args){
        float MI, TJM, TF;
        Scanner sc = new Scanner(System.in);
        System.out.print("Investimento? ");
        MI = sc.nextFloat();
        System.out.print("Taxa de juros mensal fixa? ");
        TJM = sc.nextFloat();

        for(int i = 1; i <= 3; i++){
            TF = MI*(TJM/100);
            MI += TF;
        }

        System.out.println("Valor Total ao fim de 3 meses = " + MI);
        sc.close();

    }
    
}
