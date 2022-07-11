package aula07.ex03;

public class Alojamento {
    String codigo;
    String nome;
    String local;
    double precoNoite;
    boolean disponivel;
    double avaliacao;


    public Alojamento(String codigo, String nome, String local, double precoNoite, boolean disponivel, double avaliacao) {
        this.codigo = codigo;
        this.nome = nome;
        this.local = local;
        this.precoNoite = precoNoite;
        this.disponivel = disponivel;
        this.avaliacao = avaliacao;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }

    public double getPrecoNoite() {
        return precoNoite;
    }

    public void setPrecoNoite(double precoNoite) {
        this.precoNoite = precoNoite;
    }

    public boolean isDisponivel() {
        return disponivel;
    }

    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }

    public double getAvaliacao() {
        return avaliacao;
    }


    public void setAvaliacao(double avaliacao) {
        System.out.print("Avaliação: " + avaliacao);
    }

    public void checkIn(String codigo) {
        if (this.codigo.equals(codigo)) {
            this.disponivel = false;
        }
    }
    public void checkOut(String codigo) {
        if (this.codigo.equals(codigo)) {
            this.disponivel = true;
        }
    }

    @Override
    public String toString() {
        return "Alojamento [codigo= " + codigo + ", nome= " + nome + ", local= " + local + ", precoNoite= " + precoNoite
                + ", disponivel= " + disponivel + ", avaliacao= " + avaliacao + "]";
    }



    
}
