package aula05.ex02;
import aula05.ex01.*;
import java.util.Scanner;

public class ex02 {
    public static void main(String[] args) {
        int n, ano=0;
        int diaSemana=0;
        Scanner sc = new Scanner(System.in);
        Calendar calendar = new Calendar();
        Date date = new Date();

        do{
            
            System.out.println("----------------------------------");
            System.out.println("Calendar operations: ");
            System.out.println("1 - Create new calendar");
            System.out.println("2 - Print calendar month");
            System.out.println("3 - Print calendar");
            System.out.println("0 - Exit");
            System.out.println("Operation? ");
            n = sc.nextInt();

            switch(n){
                
                case 1:
                    System.out.println("----------------------------------");
                    System.out.print("Ano: ");
                    ano = sc.nextInt();
                    System.out.print("Dia da semana que começa (1 a 7): ");
                    diaSemana = sc.nextInt();
                    calendar.setCalendar(ano, diaSemana);
                    break;
                case 2:
                    System.out.println("----------------------------------");
                    System.out.print("Mes (número): ");
                    int m = sc.nextInt();
                    System.out.print("Dia da semana em que o mês começa (1 a 7): ");
                    int d = sc.nextInt();
                    System.out.print("Ano: ");
                    int a = sc.nextInt();
                    date.setDate(d, m, a);
                    calendar.printMes(m,a,d);
                    break;
                case 3:
                    System.out.println("----------------------------------");
                    calendar.printCalendar(ano, diaSemana);

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
