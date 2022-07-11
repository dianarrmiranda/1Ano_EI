package aula10.Ex01;
import java.util.Scanner;

public class Menu {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n;
        String termo;

        Dicionario dic = new Dicionario();

        do{
            System.out.println(" ");
            System.out.println("Menu: ");
            System.out.println("-------------------------");
            System.out.println("1 - Adicionar termo. ");
            System.out.println("2 - Alterar termo.");
            System.out.println("3 - Remover Termo.");
            System.out.println("4 - Ver lista de termos.");
            System.out.println("0 - Sair");
    
            System.out.print("Opção?  ");
            n = sc.nextInt();

            switch(n){
                
                case 1:
                    dic.adicionar();
                    break;
                case 2:
                    System.out.println("Que termo deseja alterar? ");
                    termo = sc.next();
                    dic.alterarSignificado(termo);
                    break;
                case 3:
                    System.out.println("Que termo deseja remover? ");
                    termo = sc.next();
                    dic.remover(termo);
                    break;
                case 4:
                    System.out.println(dic.toString());
                    break;
                case 0:
                    System.out.println("----------------------------------");
                    System.out.println("Bye!");
                    break;
                default:
                    System.out.println("    ");
                    System.out.println("Invalid option!");
                    break;
        }
        }while(n!= 0);
        sc.close();
    } 


}
