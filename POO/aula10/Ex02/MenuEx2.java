package aula10.Ex02;
import java.util.Scanner;

public class MenuEx2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n;
        String termo;

        Dic dic = new Dic();

        do{
            System.out.println(" ");
            System.out.println("Menu: ");
            System.out.println("-------------------------");
            System.out.println("1 - Adicionar termo. ");
            System.out.println("2 - Alterar termo.");
            System.out.println("3 - Remover Termo.");
            System.out.println("4 - Adicionar significado.");
            System.out.println("5 - Alterar significado.");
            System.out.println("6 - Remover significado.");
            System.out.println("7 - Ver dicionário.");
            System.out.println("8 - Ver um significado");
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
                    System.out.println("A que termo deseja adicionar um novo significado? ");
                    termo = sc.next();
                    dic.adicionarSignificado(termo);
                break;
                case 5:
                    System.out.println("A que termo deseja alterar um significado? ");
                    termo = sc.next();
                    dic.alterarSignificado(termo);
                break;
                case 6:
                    System.out.println("A que termo deseja remover um significado? ");
                    termo = sc.next();
                    dic.removerSignificado(termo);
                    break;
                case 7:
                    System.out.println(dic.toString());
                    break;
                case 8:
                    System.out.println("De que termo deseja ver um significado? ");
                    termo = sc.next();
                    dic.verSignificado(termo);
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
