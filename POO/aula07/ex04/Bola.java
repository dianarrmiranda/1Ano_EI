package aula07.ex04;

public class Bola extends ObjetoMovel{

    private String cor;

    public Bola(String cor, int x, int y) {
        super(x, y);
        this.cor = cor;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    @Override
    public String toString() {
        return "[cor = " + cor + "] ".concat(super.toString());
    }


    
    
    
}
