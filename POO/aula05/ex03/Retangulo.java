package aula05.ex03;

public class Retangulo {
    public double comprimento, altura;

	public void setRetangulo(double c, double h){
        this.comprimento = c;
		this.altura = h;
    }
	
	public double getComprimento() {
		return comprimento;
	}

	public double getAltura() {
		return altura;
	}

	public static Boolean values(double comprimento, double altura){
        boolean valid = false;
        if(comprimento>0 && altura>0){
            valid = true;
        }
        return valid;
    }

	public String toString() {
		if(Boolean.TRUE.equals(values(comprimento, altura)))
			return String.format ("Comprimento - %s, Altura - %s", comprimento, altura);
		else{
			return "Valores inválidos!";
		}
	}
	
	public double perimetro () {
		return 2 * comprimento + 2 * altura;
	}

	public double area () {
		return comprimento * altura;
	}
}
