package aula07.ex01;

public abstract class Forma {
    public String cor;

    public abstract double area();
    public abstract double perimetro();

    public static void setcor(String cor) {
    }

    public String getCor() {
        return cor;
    }

    public static String print(String cor) {
        return String.format("Cor - %s", cor);
    }   
    
}

