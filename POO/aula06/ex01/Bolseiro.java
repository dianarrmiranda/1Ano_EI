package aula06.ex01;
import aula07.ex02.DateYMD;

public class Bolseiro extends Aluno{
    private int bolsa;
	
	//construtores

	public Bolseiro(String nome, int cc, DateYMD dataNasc) {
		super(nome, cc, dataNasc);
	}

	public Bolseiro(String nome, int cc, DateYMD dataNasc, int bolsa) {
		super(nome, cc, dataNasc);
		this.bolsa = bolsa;
	}

	//getters e setters

	public int getBolsa() {
		return bolsa;
	}

	public void setBolsa(int bolsa) {
		this.bolsa = bolsa;
	}

    @Override
	public String toString() {
		return this.getNome() + ", NMec: " + this.getNMec() + ", Bolsa: " + bolsa;
	}
}
