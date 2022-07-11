package aula11;

import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;


public class Ex01 {
    public static void main(String[]args) throws IOException{
        Map<String, TreeMap<String, Integer>> pares = new HashMap<>();
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
            
            if(word.length()>2) {
                palavras.add(word);
            }
        }

        for(int i=0;i<palavras.size()-1;i++) {
            String palAtual = palavras.get(i);
            String parProxima = palavras.get(i+1);

            if(!pares.containsKey(palAtual)) {
                TreeMap<String, Integer> valores = new TreeMap<>();
                valores.put(parProxima, 1);
                pares.put(palAtual, valores);
            }else {
                if(pares.get(palAtual).containsKey(parProxima)) {
                    pares.get(palAtual).replace(parProxima, pares.get(palAtual).get(parProxima) , pares.get(palAtual).get(parProxima)+1);
                } else {
                    pares.get(palAtual).put(parProxima, 1);
                }
            }
        }
        input.close();
        for(int i = 0; i < pares.size(); i++) {
            System.out.println(pares.entrySet().toArray()[i].toString());
        }

    
    }
}
