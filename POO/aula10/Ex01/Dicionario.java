package aula10.Ex01;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Dicionario {

    private String termo, significado, novoSig;
    private Scanner sc = new Scanner(System.in);
    private Map<String, String> dicionario = new HashMap<>();

    public void adicionar(){
        System.out.print("\nTermo? ");
        termo = sc.next();

        if(!dicionario.containsKey(termo)){
            System.out.print("\nSignificado? ");
            significado = sc.nextLine();
            significado = sc.nextLine();

            dicionario.put(termo.toLowerCase(), significado);

            System.out.println("\nTermo adicionado!");
        }else{
            System.out.println("\nEsse termo já existe");
        }
    }

    public void alterarSignificado(String t){
        if(dicionario.containsKey(t.toLowerCase())){
            System.out.print("\nNovo significado: ");
            novoSig = sc.nextLine();
            dicionario.put(t.toLowerCase(),novoSig);
            System.out.println("\nSignificado alterado.");
        }else{
            System.out.println("\nEsse termo ainda não existe no dicionário.");
        }
    }

    public void remover(String t){
        if(dicionario.containsKey(t.toLowerCase())){
            dicionario.remove(t.toLowerCase());
            System.out.println("\nTermo removido.");
        }else{
            System.out.println("\nEsse termo ainda não existe no dicionário.");
        }
    }

    @Override
    public String toString(){
        StringBuilder s = new StringBuilder();

        Set<String> termos = dicionario.keySet();

        termos.forEach(t -> {
            s.append(t);
            s.append(" : ");
            s.append(dicionario.get(t));
            s.append("\n");
        });

        return "\nDicionário  \n" + s.toString();
    }
    
}
