package aula08.Ex01;

public class PesadoPassEletrico extends PesadoPassa implements VeiculoEletrico {

    private int autonomia;
    private int autonomiaRest;

    public PesadoPassEletrico( String marca, String modelo, int potencia, int numQuadro, int peso,
            int maxNumPassa, int autonomia) {
        super( marca, modelo, potencia, numQuadro, peso, maxNumPassa);
        this.autonomia = autonomia;
        this.autonomiaRest = autonomia;  
    }

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
        return "\nPesado Passageiros Elétrico -\n \tAutonomia Total = " + autonomia + ", Autonomia Restante = " + autonomiaRest + ",".concat(super.toString());
    } 
    
}
