package aula07.ex03;

public class QuartoHotel extends Alojamento {

    private String tipoQuarto;

    public QuartoHotel(String codigo, String nome, String local, double precoNoite, boolean disponivel,
            double avaliacao, String tipo) {
        super(codigo, nome, local, precoNoite, disponivel, avaliacao);
        tipoQuarto = tipo;
    }

    
    public String getTipoQuarto() {
        return tipoQuarto;
    }

    public void setTipoQuarto(String tipoQuarto) {
        this.tipoQuarto = tipoQuarto;
    }

    @Override
    public String toString() {
        return "Quarto Hotel [tipo=" + tipoQuarto + "".concat(super.toString());
    }


    
}
