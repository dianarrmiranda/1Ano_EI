package aula02;
import java.util.Scanner;

public class hora {
    public static void main(String[] args){
        int seg, hh, mm, ss,hhr;
        Scanner sc = new Scanner(System.in);
        System.out.print("Segundos? ");
        seg = sc.nextInt();
        
        hh = seg/3600;
        hhr = seg%3600;
        mm = hhr/60;
        ss = hhr%60;

        System.out.println(hh + ":" + mm + ":" + ss);
        sc.close();

    }
}
