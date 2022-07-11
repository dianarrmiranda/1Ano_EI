package aula05.ex04;

import java.util.ArrayList;

public class Utilizador {
    private String nome;
    private int nMec;
    private String curso;
    private ArrayList<Integer> livros = new ArrayList<>();

    public Utilizador(String nome, int nMec, String curso) {
		this.nome = nome; 
        this.nMec = nMec; 
        this.curso = curso; 
    }

    public ArrayList<Integer> getLivros() {
		return livros;
	}
    
    public boolean podeRequisitar() {
		return livros.size() < 3;
	}

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setnMec(int nMec) {
        this.nMec = nMec;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }
    public String getNome() {
        return nome;
    }
    public int getnMec() {
        return nMec;
    }
    public String getCurso() {
        return curso;
    }
    
    public String toString() {
		return "Aluno: " + nMec + "; " + nome + "; " + curso;
	}
}
