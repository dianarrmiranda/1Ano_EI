package aula04;
import java.util.Scanner;

public class ex02 {
    public static void main(String[] args){
        String str;
        Scanner sc = new Scanner(System.in);
        System.out.print("Inisira uma frase: ");
        str = sc.nextLine();

        System.out.println("A string tem " + countDigits(str) + " carateres numéricos.");
        System.out.println("A string tem " + espacos(str) + " espaços");
        System.out.println("A string só tem minúsculas? " + minusculas(str));
        System.out.println("Sem espaços repetidos: " + umEspaco(str));
        System.out.println("A String é um palíndromo? " + palindromo(str));

        sc.close();
    }
    public static int countDigits(String s){
        int digit = 0;
        for(int i = 0; i<s.length(); i++ ){
            char c = s.charAt(i);
            if (Character.isDigit(c)){
                digit++;
            }
        }
        return digit;
    }
    public static int espacos(String s){
        int count = 0;
        for(int i = 0; i<s.length(); i++ ){
            if (s.charAt(i) == ' '){
                count++;
            }
        }
        return count;
    }
    public static boolean minusculas(String s){
        for(int i = 0; i<s.length(); i++ ){
            char c = s.charAt(i);
            if (Character.isUpperCase(c)){
                return false;
            }
        }
        return true;
    }
    public static String umEspaco(String s){
        s = s.replaceAll("\\s+", " ");
        return s;
    }
    public static boolean palindromo(String s){
        s = s.trim().replaceAll("\\s+", "").toLowerCase();
        for(int i = 0; i<s.length()/2; i++ ){
            char c = s.charAt(i);
            if (c != s.charAt(s.length()-(i+1))){
                return false;
            }
        }
        return true;
    }  
}
