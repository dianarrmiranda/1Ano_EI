package aula07.ex04;

public class Robo extends ObjetoMovel{
    private String id, tpJogador;
    private int nGolos;

    public Robo(String id, String tpJogador, int x, int y) {
        super(x, y);
        this.id = id;
        this.tpJogador = tpJogador;
        this.nGolos = 0;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTpJogador() {
        return tpJogador;
    }

    public void setTpJogador(String tpJogador) {
        this.tpJogador = tpJogador;
    }

    public int getnGolos() {
        return nGolos;
    }

    public void setnGolos(int nGolos) {
        this.nGolos = nGolos;
    }

    public void marcarGolo(){
        nGolos++;
    }

    @Override
    public String toString() {
        return "Robo [id = " + id + ", tpJogador = " + tpJogador + ", nGolos = " + nGolos + " ".concat(super.toString());
    }
    
}
