package aula10.Ex03;

import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.Scanner;

public class Ex03 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        System.out.print("Insira uma Frase: ");
        String s = sc.nextLine();
        sc.close();

        Map<Character, TreeSet<Integer>> posicoes = new TreeMap<>();

        for(int i = 0; i<s.length();i++){
            
            if(!posicoes.containsKey(s.charAt(i))){
                TreeSet<Integer> pos = new TreeSet<>();
                pos.add(i);
                posicoes.put(s.charAt(i), pos);
            }
            else{
                TreeSet<Integer> pos = posicoes.get(s.charAt(i));
                pos.add(i);
                posicoes.get(s.charAt(i)).addAll(pos);
            }   
        }

        System.out.println(posicoes);

        
    }
    
}
