package aula12;

import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public  class Ex01{
    public static void main(String[]args) throws IOException{
        Scanner input = null;

        ArrayList<String> palavras = new ArrayList<>();
        
        try{
            input = new Scanner(new FileReader("major.txt", StandardCharsets.UTF_8));
            input.useDelimiter("[\\p{Punct}\\s+]");
        }
        catch(IOException e){
            System.out.println("Erro a abrir o ficheiro");
        }


        while (input.hasNext()) {
            String word = input.next();
            if(word.length()>1){
                palavras.add(word);
            }   
        }
        Set<String> palavrasDiff = new HashSet<>();
        for(String p : palavras){
            palavrasDiff.add(p);
        }
        System.out.println("Número total de palavras: " + palavras.size());
        System.out.println("Número de Diferentes Palavras " + palavrasDiff.size());
    }
    
}