package aula03;

import java.util.Scanner;

public class ex01Notas {
    public static void main(String[] args){
        double notaP;
        double notaT;
        double notaF;
        Scanner sc = new Scanner(System.in);
        System.out.print("Nota Componente Prática: ");
        notaP = sc.nextDouble();
        while((notaP < 0 || notaP > 20)){
            System.out.println("Insira uma nota válida! (Entre 0 e 20)");
            System.out.print("Nota Componente Prática: ");
            notaP = sc.nextDouble();
        }
        System.out.print("Nota Componente Teórica: ");
        notaT = sc.nextDouble();
        while((notaT < 0 || notaT > 20)){
            System.out.println("Insira uma nota válida! (Entre 0 e 20)");
            System.out.print("Nota Componente Teórica: ");
            notaT = sc.nextDouble();
        }
        if (notaP < 7.0 || notaT < 7.0 ){
            System.out.println("66 (reprovado por nota mínima");
        }
        else {
            notaF = (0.4*notaT) + (0.6*notaP);
            System.out.format("Nota final: %.0f", notaF);
        }
        sc.close();
    }
}
