package aula08.Ex02;

import java.util.ArrayList;

public class Prato {

    private String nome;
    private ArrayList<Alimento> alimentos = new ArrayList<>();

    public Prato(String nome){
        this.nome = nome;
    }

    public boolean addIngrediente(Alimento alimento){
        alimentos.add(alimento);
        return true;
    }

    @Override
    public String toString() {
        return "Prato '" + nome +"', composto por " + alimentos.size() 
        + " Ingredientes";
    }


}
