package aula08.Ex01;

public class Pesado extends Veiculo{

    private int numQuadro;
    private int peso;

    public Pesado( String marca, String modelo, int potencia, int numQuadro, int peso) {
        super( marca, modelo, potencia);
        this.numQuadro = numQuadro;
        this.peso = peso;
    }

    public int getNumQuadro(){
        return numQuadro;
    }
  
    public void setNumQuadro(int numQuadro){
        this.numQuadro = numQuadro;
    }

    public int getPeso(){
        return peso;
    }

    public void setPeso(int peso){
        this.peso = peso;
    }  
    
}
