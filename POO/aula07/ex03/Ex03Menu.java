package aula07.ex03;
import java.util.ArrayList;
import java.util.Scanner;


public class Ex03Menu {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = 0;
        AgenciaViagens agencia = new AgenciaViagens("Agencia", "Rua", new ArrayList<Carro>(), new ArrayList<Alojamento>());


        do{
            System.out.println("    ");
            System.out.println("Menu: ");
            System.out.println("1 - Adicionar apartamento");
            System.out.println("2 - Adicionar Quarto");
            System.out.println("3 - Adicionar Carro");
            System.out.println("4 - Ver alojamentos");
            System.out.println("5 - Ver Carros");
            System.out.println("6 - Emprestar Carro");
            System.out.println("7 - Reservar Alojamento");
            System.out.println("0 - Sair");
            System.out.println("Opção? ");
            n = input.nextInt();

            switch(n){
                case 0:
                    System.out.println("    ");
                    System.out.println("Bye!");
                    break;
                case 1:
                    agencia.adicionarAlojamento();
                    break;
                case 2:
                    agencia.adicionarQuarto();
                    break;
                case 3:
                    agencia.adicionarCarro();
                    break;
                case 4:
                    agencia.verAlojamentos();
                    break;
                case 5:
                    agencia.verCarros();
                    break;
                case 6:
                    agencia.emprestarCarro();
                    break;
                case 7:
                    agencia.reservarAlojamento();
                    break;
                default:
                    System.out.println("    ");
                    System.out.println("Invalid option!");
            }

        }while(n != 0);
        input.close();

    }
    
}
