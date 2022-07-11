package aula03;
import java.util.Scanner;

public class ex05_Invest {
    public static void main(String[] args){
        double mInv, taxa, TF;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.print("Montante Investido: ");
            mInv = sc.nextInt();
            if (mInv<0 || mInv%1000 !=0){
                System.out.println("Insira um valor válido! (positivo e múltiplo de 1000)");
            }
        }while(mInv<0 || mInv%1000 !=0);
        do{
            System.out.print("Taxe de juro mensal: ");
            taxa = sc.nextDouble();
            if (taxa<0 || taxa>5){
                System.out.println("Insira um valor válido! (Entre 0% e 5%)");
            }
        }while(taxa<0 || taxa>5);

        for(int i = 1; i <= 12; i++){
            TF = mInv*(taxa/100);
            mInv += TF;
            System.out.format("Valor Total ao fim de %d meses = %.3f %n", i, mInv);
        }
        sc.close();
    }
    
}
