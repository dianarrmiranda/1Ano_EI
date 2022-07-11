package aula04;
import java.util.Scanner;

public class ex01 {
    public static void main(String[] args){
        String str, min, maiu;
        Scanner sc = new Scanner(System.in);
        System.out.print("Inisira uma palavra, frase ou parágrafo: ");
        str = sc.nextLine();
        min = str.toLowerCase();
        maiu = str.toUpperCase();

        System.out.println("Em minusculas: " + min);
        System.out.println("Em maiúsculas: " + maiu);
        System.out.println("Último carater: "+ str.trim().charAt(str.length()-1));
        System.out.println("Primeiros 3 carateres: "+ str.substring(0, 3));
        System.out.println("Total de carateres: " + str.trim().length());
        for(int i=0; i<str.trim().length(); i++){
            System.out.print(str.charAt(i) + ", ");
        }

        
        sc.close();
    }
    
}
