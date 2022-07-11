package aula02;

import java.util.Scanner;

public class temp {
    public static void main(String[] args){
        double c, f;
        Scanner sc = new Scanner(System.in);
        System.out.print("Temperatura graus Célcius: ");
        c = sc.nextDouble();
        f = 1.8*c+32;
        System.out.println(c + " Célsius são " + f + " Fahrenheit");
        sc.close();
    }
    
}
