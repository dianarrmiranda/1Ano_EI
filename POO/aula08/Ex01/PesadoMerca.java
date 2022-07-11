package aula08.Ex01;

public class PesadoMerca extends Pesado {

    private int maxCarga;

    public PesadoMerca(String marca, String modelo, int potencia, int numQuadro, int peso, int maxCarga) {
        super( marca, modelo, potencia, numQuadro, peso);
        this.maxCarga = maxCarga;
    }

    public int getCarga(){
        return maxCarga;
    }

    public void setCarga(int maxCarga){
        this.maxCarga = maxCarga;
    }

    @Override
    public String toString(){
        return "\nPesado de Mercadorias -\n \tNúmero máximo de carga = " + maxCarga + ",".concat(super.toString());
    }

}
