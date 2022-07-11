package aula08.Ex01;

public class Motociclo extends Veiculo{

    private String tipo;

    public Motociclo(String marca, String modelo, int potencia, String tipo) {
        super(marca, modelo, potencia);
        this.tipo = tipo;
    }

    public String getTipo(){
        return tipo;
    }

    public void setTipo(String tipo){
        this.tipo = tipo;
    }

    @Override
    public String toString(){
        return "\nMotociclo -\n \tTipo = " + tipo + ",".concat(super.toString());
    }
    
}
