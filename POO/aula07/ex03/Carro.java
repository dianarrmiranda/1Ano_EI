package aula07.ex03;

public class Carro {
    char classe;
    String motorizacao;
    private int codigo;
    private static int counter = 0;

    public Carro(char classe, String motorizacao) {
        this.classe = classe;
        this.motorizacao = motorizacao;
        codigo = counter++;
    }

    public char getClasse() {
        return classe;
    }

    public void setClasse(char classe) {
        this.classe = classe;
    }

    public String getMotorizacao() {
        return motorizacao;
    }

    public void setMotorizacao(String motorizacao) {
        this.motorizacao = motorizacao;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public static int getCounter() {
        return counter;
    }

    public static void setCounter(int counter) {
        Carro.counter = counter;
    }

    public boolean isDisponivel() {
        return false;
    }

    public void setDisponivel(boolean b) {
    }






}
