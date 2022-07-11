package aula08.Ex02;

public class AlimentoVegetariano extends Alimento {
    private String nome;
    public AlimentoVegetariano(Double proteinas, Double calorias, Double peso, String nome) {
        super(proteinas, calorias, peso);
        this.nome = nome;
    }

    @Override
    public String toString() {
        return nome + super.toString();
    }
    
}
