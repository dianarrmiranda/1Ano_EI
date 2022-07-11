package aula12.Ex02;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Menu {

    public static void main(String[]args) throws IOException{
		TreeSet<Movie> listaMovies = new TreeSet<>();
        Scanner input = null;
        String linha[];

        try{
			input = new Scanner(new FileReader("movies.txt", StandardCharsets.UTF_8));
        }
        catch(IOException e){
            System.out.println("Erro a abrir o ficheiro");
        }

		input.nextLine(); //salta a primeira linha
        while (input.hasNextLine()) {
			linha = input.nextLine().split("[\t]");
			listaMovies.add(new Movie(linha[0], Double.parseDouble(linha[1]), linha[2], linha[3], Integer.parseInt(linha[4])));
		}
		input.close();
        //Alinea a e b)
        System.out.printf("%-40s %-10s %-10s %-15s %-10s\n", "Name", "Score", "Rating", "Genre", "Running time");
        for(Movie m : listaMovies){
            System.out.println(m);
        }
        //Alinea c)
        Map<String, Double> scores = new HashMap<>();
        for(Movie m : listaMovies){
            scores.put(m.getName(), m.getScore());
        }

        scores = ordenarValCrescente(scores);
        scores = ordenarValDecrescente(scores);

        System.out.println("\nOrdenado por Score (Decrescente)\n");
        System.out.printf("%-40s %-10s %-10s %-15s %-10s\n", "Name", "Score", "Rating", "Genre", "Running time");
        for(String s : scores.keySet()){
            for(Movie m : listaMovies){
                if(m.getName() == s){
                    System.out.println(m);
                }
            }
        }

        //Alinea c - 2ª parte)
        Map<String, Double> runtime = new HashMap<>();
        for(Movie m : listaMovies){
            runtime.put(m.getName(), (double) m.getRunTime());
        }

        runtime = ordenarValCrescente(runtime);

        System.out.println("\nOrdenado por Runtime (Crescente)\n");
        System.out.printf("%-40s %-10s %-10s %-15s %-10s\n", "Name", "Score", "Rating", "Genre", "Running time");
        for(String s : runtime.keySet()){
            for(Movie m : listaMovies){
                if(m.getName() == s){
                    System.out.println(m);
                }
            }
        }

        //Alinea d)
        Set<String> genre = new TreeSet<>();
        for(Movie m : listaMovies){
            if(!genre.contains(m.getGenre())){
                genre.add(m.getGenre());
            }
        }
        System.out.println("\nGéneros de filmes existentes: ");
        for(String g : genre){
            System.out.println(g);
        }

        //Alinea e)
        PrintWriter ficheiro = new PrintWriter(new File("myselection.txt"));
        ficheiro.println("\nSeleção\n");
        ficheiro.printf("%-40s %-10s %-10s %-15s %-10s\n", "Name", "Score", "Rating", "Genre", "Running time");
        for(Movie m : listaMovies){
            if(m.getScore() > 60 && m.getGenre().equals("comedy")){
                ficheiro.println(m);
            }
        }
        ficheiro.close();
    }
    
	private static Map<String, Double> ordenarValCrescente(Map<String, Double> map) 
	{
	  LinkedHashMap<String, Double> sortedMap = new LinkedHashMap<>();
	  map.entrySet().stream().sorted(Map.Entry.comparingByValue())
		  .forEachOrdered(x -> sortedMap.put(x.getKey(), x.getValue()));
	
	  return sortedMap;
	}

	private static Map<String, Double> ordenarValDecrescente(Map<String, Double> map) 
	{  
	  LinkedHashMap<String, Double> reverseSortedMap = new LinkedHashMap<>();
	  map.entrySet().stream().sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
		  .forEachOrdered(x -> reverseSortedMap.put(x.getKey(), x.getValue()));

	  return reverseSortedMap;
	}

}