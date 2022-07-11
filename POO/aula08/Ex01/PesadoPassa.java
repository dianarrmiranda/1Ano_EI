package aula08.Ex01;

public class PesadoPassa extends Pesado {

    private int maxNumPassa;

    public PesadoPassa( String marca, String modelo, int potencia, int numQuadro, int peso, int maxNumPassa) {
        super(marca, modelo, potencia, numQuadro, peso);
        
    }

    public int getNumPassa(){
        return maxNumPassa;
    }

    public void setNumPassa(int maxNumPassa){
        this.maxNumPassa = maxNumPassa;
    }

    @Override
    public String toString(){
        return "\nPesado de Passgeiros -\n \tNúmero máximo de passageiros = " + maxNumPassa + ",".concat(super.toString());
    }


}
