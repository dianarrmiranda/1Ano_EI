package aula10.Ex02;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.lang.Math;

public class Dic {
    private String termo, significado, novoSig;
    private Scanner sc = new Scanner(System.in);
    private Map<String, HashSet<String>> dicionario = new TreeMap<>();

    public void adicionar(){
        HashSet<String> significados = new HashSet<>();
        System.out.print("\nTermo? ");
        termo = sc.next();

        if(!dicionario.containsKey(termo)){
            System.out.print("Significado? ");
            significado = sc.nextLine();
            significado = sc.nextLine();
            significados.add(significado);
            dicionario.put(termo.toLowerCase(), significados);

            System.out.println("\nTermo adicionado!");
        }else{
            System.out.println("\nEsse termo já existe");
        }
    }

    public void adicionarSignificado(String t){
        HashSet<String> significados = dicionario.get(t.toLowerCase());
        if(dicionario.containsKey(t.toLowerCase())){
            System.out.print("\nNovo significado? ");
            novoSig = sc.nextLine();
            if(!significados.contains(novoSig)){
                significados.add(novoSig);
                dicionario.get(t.toLowerCase()).addAll(significados);
                System.out.println("\nSignificado adicionado!");
            }else{
                System.out.println("\nO termo já tem esse significado");
            }
        }else{
            System.out.println("\nEsse termo ainda não existe no dicionário.");
        }
    }

    public void alterarSignificado(String t){
        HashSet<String> significados = dicionario.get(t.toLowerCase());
        if(dicionario.containsKey(t.toLowerCase())){
            System.out.println(printSignificados(t.toLowerCase()));
            System.out.println("\nQue significado quer alterar? ");
            String s = sc.nextLine();
    
            if(significados.contains(s)){
                System.out.print("\nNovo significado: ");
                novoSig = sc.nextLine();
                significados.remove(s);
                significados.add(novoSig);
                System.out.println("\nSignificado alterado.");
            }else{
                System.out.println("\nEste termo ainda não tem esse significado.");
            }
        }else{
            System.out.println("\nEsse termo ainda não existe no dicionário.");
        }

    }

    public void removerSignificado(String t){
        HashSet<String> significados = dicionario.get(t.toLowerCase());
        if(dicionario.containsKey(t.toLowerCase())){
            System.out.println(printSignificados(t.toLowerCase()));
            System.out.println("\nQue significado quer remover? ");
            String s = sc.nextLine();
    
            if(significados.contains(s)){
                significados.remove(s);
                System.out.println("\nSignificado removido.");
            }else{
                System.out.println("\nEste termo ainda não tem esse significado.");
            }
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

    public void verSignificado(String t){
        if(dicionario.containsKey(t.toLowerCase())){
            HashSet<String> significados = dicionario.get(t.toLowerCase());
            int n =  (int) (Math.random() * significados.size());
            int i = 0;
            for(String s : significados){
                if (i==n){
                    System.out.println("\nSignificado: " + s);
                    break;
                }
                i++;
            }
        }else{
            System.out.println("\nEsse termo ainda não existe no dicionário.");
        }
    }

    @Override
    public String toString(){
        StringBuilder s = new StringBuilder();

        Set<String> termos = dicionario.keySet();
        

        for (String t : termos){
            HashSet<String> significados = dicionario.get(t);
            s.append(t + ":\n");
            for(String sig : significados){
                s.append(" - " + sig + "\n");
            }
        }


        return "\nDicionário  \n" + s.toString();
    }

    public String printSignificados(String t){
        StringBuilder s = new StringBuilder();

        HashSet<String> significados = dicionario.get(t);

        for(String sig : significados){
            s.append(sig);
            s.append("\n");
        }
        return "\nSignificados  \n" + s.toString();
    }
    
}
