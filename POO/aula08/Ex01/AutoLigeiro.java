package aula08.Ex01;

public class AutoLigeiro extends Veiculo {

    private int numQuadro;
    private int capacidadeBag;

    public AutoLigeiro( String marca, String modelo, int potencia, int numQuadro, int capacidadeBag) {
        super(marca, modelo, potencia);
        this.numQuadro = numQuadro;
        this.capacidadeBag = capacidadeBag;
    }

    public int getNumQuadro(){
        return numQuadro;
    }
    
    public void setNumQuadro(int numQuadro){
        this.numQuadro = numQuadro;
    }

    public int getCapacidadeBag(){
        return capacidadeBag;
    }
    
    public void setCapacidadeBag(int capacidadeBag){
        this.capacidadeBag = capacidadeBag;
    }

    @Override
    public String toString(){
        return "\nAutomóvel ligeiro -\n \tNúmero de quadro = " + numQuadro + ", Capaciade de bagagem = " + capacidadeBag +  "," + super.toString();
    }
}
