package aula08.Ex02;

public class PratoDieta extends Prato{

    private double maxCal;

    public PratoDieta(String nome, double maxCal) {
        super(nome);
        this.maxCal = maxCal;
    }


    public String toString() {
        return super.toString() + " - Prato Dieta (" + maxCal + " Calorias) ";
    }




    
}
