package aula06.ex01;
import aula07.ex02.DateYMD;

public class Aluno extends Pessoa {

	private final int NMec;
	private static int contador = 100;

	public Aluno(String nome, int cc, DateYMD dataNasc) { 
		super(nome, cc, dataNasc);
		this.NMec= contador++;
	}
	
	public int getNMec() {
		return NMec;
	}
    
	@Override
	public String toString() {
		return this.getNome() + ", NMec: " + this.getNMec();
	}
}
