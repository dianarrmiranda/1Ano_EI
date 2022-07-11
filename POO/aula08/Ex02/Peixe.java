package aula08.Ex02;

public class Peixe extends Alimento {
    private TipoPeixe tipo;

    public Peixe(TipoPeixe tipo, Double proteinas, Double calorias, double peso) {
        super(proteinas, calorias, peso);
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "Peixe " + tipo + super.toString();
    }
    
}
