package aula07.ex03;

public class Apartamento extends Alojamento{

    private int numeroQuartos;
    public Apartamento(String codigo, String nome, String local, double precoNoite, boolean disponivel,
            double avaliacao, int numeroQuartos) {
        super(codigo, nome, local, precoNoite, disponivel, avaliacao);
        this.numeroQuartos = numeroQuartos;
    }

    
    public int getNumeroQuartos() {
        return numeroQuartos;
    }

    public void setNumeroQuartos(int numeroQuartos) {
        this.numeroQuartos = numeroQuartos;
    }

    @Override
    public String toString() {
        return "Apartamento [numeroQuartos = " + numeroQuartos + "".concat(super.toString());
    }


    
}
