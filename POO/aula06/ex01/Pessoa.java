package aula06.ex01;

import aula07.ex02.DateYMD;

public class Pessoa {
    private String nome;
    private int cc;
    private DateYMD dataNasc;

    public Pessoa(String nome, int cc, DateYMD dataNasc) {
		this.nome = nome; this.cc = cc; this.dataNasc = dataNasc;
	}

	public String getNome() {
		return nome;
	}

	public int getCc() {
		return cc;
	}

	public DateYMD getDataNasc() {
		return dataNasc;
	}
    @Override
	public String toString() {
		return nome + ", CC: " + cc + ", Data de Nascimento: " + dataNasc.toString();
	}



}


