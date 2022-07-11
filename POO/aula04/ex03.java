package aula04;
import java.util.Scanner;

public class ex03 {
    public static void main(String[] args){
        String str;
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduza uma frase: ");
        str = sc.nextLine();

        System.out.println("Acrónimo: "+ acronimo(str));
        sc.close();
    }

    public static String acronimo(String str){
        
        StringBuilder acro = new StringBuilder();
        
        String[] separar = str.split("\\s+");

        for(int i = 0; i<separar.length; i++ ){
            char c = separar[i].charAt(0);
            if((separar[i].length() >3) ){
                c = Character.toUpperCase(c);
                acro.append(c);
            }
        }
        return acro.toString();
    }
}
