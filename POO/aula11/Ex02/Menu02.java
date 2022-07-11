package aula11.Ex02;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Menu02 {
    public static void main(String[]args) throws IOException{
        Map<String, String> companhias = new TreeMap<>();
		ArrayList<Voos> listaVoos = new ArrayList<>();
        Scanner inputVoos = null, inputCompanhias = null;
        String linha[];
        try{
			inputVoos = new Scanner(new FileReader("voos.txt", StandardCharsets.UTF_8));
			inputCompanhias = new Scanner(new FileReader("companhias.txt", StandardCharsets.UTF_8));
        }
        catch(IOException e){
            System.out.println("Erro a abrir o ficheiro");
        }

		inputCompanhias.nextLine(); //salta a primeira linha
        while (inputCompanhias.hasNextLine()) {
			linha = inputCompanhias.nextLine().split("[\t]");
			companhias.put(linha[0], linha[1]);
		}

		Voos.setCompanhias(companhias);

		inputCompanhias.close();
		
        linha = null;

		inputVoos.nextLine();
        while(inputVoos.hasNextLine()){
            linha = inputVoos.nextLine().split("[\t]");
            if (linha.length == 4) {
				listaVoos.add(new Voos(linha[0], linha[1], linha[2], linha[3]));
			} else {
				listaVoos.add(new Voos(linha[0], linha[1], linha[2]));
			}
        }
        inputVoos.close();

        Map<String, int[]> mapAtrasos = new HashMap<>();

		for (Voos v : listaVoos) {
			if (v.getAtraso() != "") {
				int[] late;
				if (mapAtrasos.containsKey(v.getCompanhia().substring(0, 2).trim())) {
					late = mapAtrasos.get(v.getCompanhia().substring(0, 2).trim());
				} else {
					late = new int[2];
				}
				late[0]++; //quantidade de atrasos
				late[1] += Voos.stringToMinutos(v.getAtraso()); //soma atrasos
				mapAtrasos.put(v.getCompanhia().substring(0, 2).trim(), late);
			}
		}
        Map<String, Integer> mapAtrasosTable = new HashMap<>();
		for (String c : mapAtrasos.keySet()) {
			int[] a = mapAtrasos.get(c);
			mapAtrasosTable.put(c, (int) a[1] / a[0]);
		}
		mapAtrasosTable = ordenarValCrescente(mapAtrasosTable);

        PrintWriter ficheiro2 = new PrintWriter(new File("atrasos.txt"));
		ficheiro2.printf("%-20s %-15s\n", "Companhia", "Voos");
		for (String k : mapAtrasosTable.keySet()) {
			ficheiro2.printf("%-20s %-15s\n", companhias.get(k), Voos.minutosToString(mapAtrasosTable.get(k)));
		}
		ficheiro2.close();
		
        Map<String, Integer> mapaVoos = new HashMap<>();

		for(Voos v : listaVoos){
			String origem = v.getlocal();
			int nVoo =0;
			if(!mapaVoos.containsKey(origem)){
				mapaVoos.put(origem, nVoo+1);
			}else{
				mapaVoos.put(origem, mapaVoos.get(origem) +1);
			}
		}

		mapaVoos = ordenarValCrescente(mapaVoos);
		mapaVoos = ordenarValDecrescente(mapaVoos);

		PrintWriter ficheiro3 = new PrintWriter(new File("cidades.txt"));
		ficheiro3.printf("%-20s %-15s\n", "Origem", "Voos");
		for (String k : mapaVoos.keySet()) {
			ficheiro3.printf("%-20s %-15s\n", k, mapaVoos.get(k));
		}
		ficheiro3.close();
    
        PrintWriter ficheiro = new PrintWriter(new File("Infopublico.txt"));
        ficheiro.printf("%-15s %-15s %-20s %-20s %-15s %-15s\n", "Hora", "Voo", "Companhia", "Origem", "    Atraso", "     Obs");
        for (Voos v : listaVoos) {
			ficheiro.println(v);
		}
		ficheiro.println(
				"---------------------------------------------------------------------------------------------------");
        ficheiro.close();
		
    }

	private static Map<String, Integer> ordenarValCrescente(Map<String, Integer> map) 
	{
	  LinkedHashMap<String, Integer> sortedMap = new LinkedHashMap<>();
	  map.entrySet().stream().sorted(Map.Entry.comparingByValue())
		  .forEachOrdered(x -> sortedMap.put(x.getKey(), x.getValue()));
	
	  return sortedMap;
	}

	private static Map<String, Integer> ordenarValDecrescente(Map<String, Integer> map) 
	{  
	  LinkedHashMap<String, Integer> reverseSortedMap = new LinkedHashMap<>();
	  map.entrySet().stream().sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
		  .forEachOrdered(x -> reverseSortedMap.put(x.getKey(), x.getValue()));

	  return reverseSortedMap;
	}

    
}
