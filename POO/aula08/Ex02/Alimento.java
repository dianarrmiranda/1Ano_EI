package aula08.Ex02;

public class Alimento {
    private double proteinas, calorias, peso;

    public Alimento(Double proteinas, Double calorias, Double peso){
        this.proteinas = proteinas;
        this.calorias = calorias;
        this.peso = peso;
    }

    @Override
    public String toString() {
        return ", Proteinas " + proteinas + ", calorias " + calorias + ", Peso " + peso;
    }

}
