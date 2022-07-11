package aula08.Ex02;

public class Carne extends Alimento{
    private VariedadeCarne variedade;

    public Carne(VariedadeCarne variedade, Double proteinas, Double calorias, Double peso) {
        super(proteinas, calorias, peso);
        this.variedade = variedade;
    }

    @Override 
    public String toString() {

        return "Carne " + variedade + super.toString();
    }
}
