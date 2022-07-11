package aula05.ex01;
import java.util.Scanner;


public class Ex01 {
    public static void main(String[] args) {
		int n;
        int d = 0, m = 0,a = 0;
        Scanner sc = new Scanner(System.in);
        Date date = new Date();

        do{
            
            System.out.println("    ");
            System.out.println("Date operations: ");
            System.out.println("1 - Create a new date");
            System.out.println("2 - Show current date");
            System.out.println("3 - Increment date");
            System.out.println("4 - Decrement date");
            System.out.println("0 - Exit");
            System.out.println("Operation? ");
            n = sc.nextInt();
        
            switch(n){
                case 0:
                    System.out.println("    ");
                    System.out.println("Bye!");
                    break;
                case 1:
                    System.out.println("    ");
                    System.out.println("Enter the date: ");
                    System.out.print("Enter the day: ");
                    d = sc.nextInt();
                    System.out.print("Enter the month: ");
                    m = sc.nextInt();
                    System.out.print("Enter the year: ");
                    a = sc.nextInt();
                    date.setDate(d, m, a);
                    break;
                case 2:
                    System.out.println("    ");
                    System.out.println("Current Date: " + date.printt());
                    break;
                case 3:
                    date.incrementDate();
                    System.out.println("    ");
                    System.out.println("Current date: " + date.printt());
                    break;
                case 4:
                    date.decrementDate();
                    System.out.println("    ");
                    System.out.println("Current date a : " + date.printt());
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