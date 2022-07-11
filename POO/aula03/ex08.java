package aula03;
import java.util.Scanner;

public class ex08 {
    public static void main(String[] args){
        double notaP;
        double notaT;
        double notaF;
        Scanner sc = new Scanner(System.in);
        Double[][] turma = new Double[16][3];

        for(int i=0; i<16; i++){
            notaP = Math.floor(Math.random() * 21);
            notaT = Math.floor(Math.random() * 21);
           
            notaF = (0.4*notaT) + (0.6*notaP);
            if(notaP < 7.0 || notaT < 7.0 ){
                notaF = 66;
            }
            turma[i][0] = (double) Math.round(notaP);
            turma[i][1] = (double) Math.round(notaT);
            turma[i][2] = (double) Math.round(notaF);

        }
        System.out.format("%-10s  %-10s %-10s %n", "NotaT", "NotaP", "Pauta" );
        for(int i=0; i<16; i++){
            System.out.format("%-10.1f  %-10.1f %-10.0f %n", turma[i][1], turma[i][0], turma[i][2]);
        }
        sc.close();
    }  
}
