package aula03;
import java.util.Scanner;

public class ex06_data {
    public static void main(String[] args){
        int ano, mes, dias;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.print("Mês: ");
            mes = sc.nextInt();
            if (mes<0 || mes>12){
                System.out.println("Insira um mês válido!");
            }
        }while(mes<0 || mes>12);
        do{
            System.out.print("Ano: ");
            ano = sc.nextInt();
            if (ano<0){
                System.out.println("Insira um ano válido!");
            }
        }while(ano<0);
        switch (mes){
            case 1:
            case 3:dias = 31; break;
            case 2: 
                if((ano%4 == 0) && ((ano%100 != 0) || (ano%400 == 0))){
                    dias = 29;
                }else{dias = 28;
                }break;
            case 5:
            case 7:
            case 8:
            case 10:
            case 12: dias = 31; break;
            default: dias = 30;
        }

        System.out.println("O mês " + mes + " do ano " + ano + " tem " + dias + " dias.");
        sc.close();
    }
    
}
