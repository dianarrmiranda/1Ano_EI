package aula10.Ex04;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class Ex04 {
    public static void main(String[]args) throws IOException{
        Scanner input = new Scanner(new FileReader("words.txt"));
        TreeSet<String> maisde2 = new TreeSet<>();
        ArrayList<String> terminaS = new ArrayList<>();
        ArrayList<String> palavrasAll = new ArrayList<>();
        ArrayList<String> Soletras = new ArrayList<>();

        while(input.hasNext()){
            String word = input.next();

            palavrasAll.add(word);

            if(word.length()>2){
                maisde2.add(word);
            }

            int n = word.length();

            if(word.charAt(n-1) == 'S'){
                terminaS.add(word);
            }

        }

        for(int i = 0; palavrasAll.size() > i; i++){
            System.out.println(palavrasAll.get(i));
            if(palavrasAll.get(i).matches("[a-zA-Z]+")){
                Soletras.add(palavrasAll.get(i));
            }
        }

        System.out.println("Todas as palavras: ");
        System.out.println(palavrasAll + "\n");
        System.out.println("Palavras com mais de 2 caracteres: ");
        System.out.println(maisde2 + "\n");
        System.out.println("Palavras que terminam com s: ");
        System.out.println(terminaS + "\n");
        System.out.println("Palavras que só contém letras: ");
        System.out.println(Soletras + "\n");

    }
    
}
