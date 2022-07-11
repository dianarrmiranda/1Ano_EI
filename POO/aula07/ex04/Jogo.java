package aula07.ex04;

public class Jogo {
    private long comeco; 
    private long tempDecorrido;
    private long tempoJogo;
    private Bola bola;
    private Equipa eq1, eq2;
    private boolean done = false;

    public Jogo (Equipa eq1, Equipa eq2, Bola bola, long tempoJogo) {
        this.eq1 = eq1;
        this.eq2 = eq2;
        this.tempoJogo = tempoJogo;
        this.bola = bola;
    }

    public boolean isDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }

    public void comeco() {
        comeco = (System.currentTimeMillis()/1000);
    }

    public void atualizar(){
        tempDecorrido = (System.currentTimeMillis()/1000) - comeco;
        if(tempDecorrido >= tempoJogo){
            done = true;
        }
    }

    public void marcar(int eqId, int jogId){
        if(eqId == 1){
            eq1.marcarGolo(jogId);
            eq2.sofrerGolo();
        }else{
            eq2.marcarGolo(jogId);
            eq1.sofrerGolo();
        }
    }

    @Override
    public String toString() {
        return "Jogo { " + "Começo = " + comeco + ", Tempo Decorrido = " + tempDecorrido + ", Tempo de Jogo (s) = " + tempoJogo + ", bola = " + bola + ", Equipa 1 = " + eq1 + ", Equipa 2 = " + eq2 + '}';
    }







}
