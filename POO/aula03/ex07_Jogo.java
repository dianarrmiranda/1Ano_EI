package aula03;
import java.util.Scanner;
import java.lang.Math;

public class ex07_Jogo {
    public static void main(String[] args){
        int n, num, i;
        String c;
        i=0;
        Scanner sc = new Scanner(System.in);
        do{
            n = (int) Math.floor(Math.random() * 101);
            do{
                System.out.print("Número? ");
                num = sc.nextInt();
                if(num > n){
                    System.out.println("Demasiado Alta!");
                }else if (num < n){
                    System.out.println("Demasiado Baixa!");
                }else{
                    System.out.println("Certo!");
                }
                i++;
            }while(num != n);

            System.out.println("Fez " + i + " tentativas.");

            System.out.println("Pretende continuar? Prima(S)im ");
            c = sc.next();
            

        }while(c.equals("S") || c.equals("Sim"));
        
        sc.close();
    }
}
