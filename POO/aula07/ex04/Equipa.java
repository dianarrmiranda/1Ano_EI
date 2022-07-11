package aula07.ex04;

public class Equipa {
    private String nome, nomeResp;
    private int gm=0, gs=0;
    private Robo[] jogadores = new Robo[3];
    

    public Equipa(String nome, String nomeResp, Robo[] jogadores) {
        this.nome = nome;
        this.nomeResp = nomeResp;
        this.jogadores = jogadores;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNomeResp() {
        return nomeResp;
    }

    public void setNomeResp(String nomeResp) {
        this.nomeResp = nomeResp;
    }

    public int getGm() {
        return gm;
    }

    public void setGm(int gm) {
        this.gm = gm;
    }

    public int getGs() {
        return gs;
    }

    public void setGs(int gs) {
        this.gs = gs;
    }   

    public void setJogadores(Robo[] jogadores) {
        this.jogadores = jogadores;
    }

    public void marcarGolo(int idjogador){
        jogadores[idjogador].marcarGolo();
        gm++;
    }

    public void sofrerGolo(){
        gs++;
    }

    public String printJogadores(){
        String s = "";
        for(int i=0; i<jogadores.length; i++){
            s += jogadores[i].toString() + "\n";
        }
        return s;
    }

    @Override
    public String toString() {
        return "{ " + "nome = " + nome + ", nome Responsável = " + nomeResp + ", golos marcados = " + gm + ", golos sofridos = " + gs + ", jogadores = " + printJogadores() + " }";
    }

}
