package aula08.Ex02;

public class PratoVegetariano extends Prato {
    
    public PratoVegetariano(String nome) {
        super(nome);
    }
    @Override
    public boolean addIngrediente(Alimento alimento){
        if (alimento instanceof AlimentoVegetariano){
            return super.addIngrediente(alimento);
        }
        return false;
    }

    @Override
    public String toString() {
        return super.toString() + " - Prato Vegetariano ";
    }


    
}
