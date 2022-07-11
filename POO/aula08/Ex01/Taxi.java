package aula08.Ex01;

public class Taxi extends AutoLigeiro{

    private int numLicenca;

    public Taxi(String marca, String modelo, int potencia, int numeroQuartos, int capacidadeBag, int numLicenca) {
        super( marca, modelo, potencia, numeroQuartos, capacidadeBag);
        this.numLicenca = numLicenca;
    }
    
    public int getNumLicenca(){
        return numLicenca;
    }

    public void setNumLicenca(int numLicenca){
        this.numLicenca = numLicenca;
    }

    @Override
    public String toString(){
        return "\nTaxi -\n \tNúmero licença = " + numLicenca + ",".concat(super.toString());
    }
}
