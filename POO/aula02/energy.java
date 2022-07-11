package aula02;

import java.util.Scanner;

public class energy {
    public static void main(String[] args){
        double M, finalTemperature, initialTemperature, Q;
        Scanner sc = new Scanner(System.in);
        System.out.print("Insira a Quantidade de Água: ");
        M = sc.nextDouble();
        System.out.print("Insira a Temperatura Inicial: ");
        initialTemperature = sc.nextDouble();
        System.out.print("Insira a Temperatura Final: ");
        finalTemperature = sc.nextDouble();

        Q = M *(finalTemperature - initialTemperature) + 4184;

        System.out.println("A energia necessária é " + Q + "j");
        sc.close();

    }
    
}
