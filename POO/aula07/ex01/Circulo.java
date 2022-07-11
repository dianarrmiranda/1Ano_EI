package aula07.ex01;

public class Circulo extends Forma {
	public double raio;

	public Circulo(double raio){
        this.raio = raio;
	
    }

	public void setCirculo(double raio){
        this.raio = raio;
    }
	
	public double getRaio() {
		return raio;
	}

	public static Boolean value(double raio){
        boolean valid = false;
        if(raio>0){
            valid = true;
        }
        return valid;
    }

	public String toString() {
		if(Boolean.TRUE.equals(value(raio)))
            return String.format("Raio - %s", raio);
        else{
            return "Raio inválido!";
        }
	}
	
	public double area () {
		return Math.PI * Math.pow(raio, 2);
	}
	
	public double perimetro () {
		return 2 * Math.PI * raio;
	}

	@Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
 
        if (!(o instanceof Circulo)) {
            return false;
        }

        Circulo c = (Circulo) o;

        return Double.compare(raio, c.raio) == 0;
    }


}
