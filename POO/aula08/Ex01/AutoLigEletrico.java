package aula08.Ex01;

public class AutoLigEletrico extends AutoLigeiro implements VeiculoEletrico {
    
    private int autonomia;
    private int autonomiaRest;
    
    public AutoLigEletrico( String marca, String modelo, int potencia, int numQuadro,
            int capacidadeBag, int autonomia) {
        super( marca, modelo, potencia, numQuadro, capacidadeBag);
        this.autonomia = autonomia;
        this.autonomiaRest = autonomia;        
    }

    @Override
    public void trajeto(int quilometros) {
        super.trajeto(quilometros);
        autonomiaRest -= quilometros;
    }

    @Override
    public int autonomia() {
        return autonomiaRest;
    }

    @Override
    public void carregar(int percentagem) {
        double carregamento = percentagem * autonomia / 100;
        
        if(carregamento > autonomiaRest){
            autonomiaRest = (int) carregamento;
        }else{
            System.out.println("O automóvel tem mais do que " + percentagem + "% de autonomia"); 
        }        
    }
    @Override
    public String toString(){
        return "\nAutomóvel Ligeiro Elétrico -\n \tAutonomia Total = " + autonomia + ", Autonomia Restante = " + autonomiaRest + ",".concat(super.toString());
    } 
}
