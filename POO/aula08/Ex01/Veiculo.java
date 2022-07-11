package aula08.Ex01;

public abstract class Veiculo implements KmPercorridosInterface{
    private String matricula;
    private String marca;
    private String modelo;
    private int potencia;
    private int quilometros;
    private int distancia;
    

    public Veiculo(String marca, String modelo, int potencia) {
        this.marca = marca;
        this.modelo = modelo;
        this.potencia = potencia;
    }

    public String getMatricula() {
        return matricula;
    }

    public Veiculo setMatricula(String matricula) {
        if(matricula.matches("([0-9]{2}-[0-9]{2}-[A-Z]{2})|([0-9]{2}-[A-Z]{2}-[0-9]{2})|([A-Z]{2}-[0-9]{2}-[0-9]{2})")){
            this.matricula = matricula;
        }else{
            System.out.println("Matrícula Inválida");
        }
        return this;
    }
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }
    
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public int getPotencia() {
        return potencia;
    }

    public void setPotencia(int potencia) {
        this.potencia = potencia;
    }

    @Override
    public void trajeto(int quilometros) {
        this.quilometros = quilometros;
        distancia += quilometros;
    }

    @Override
    public int ultimoTrajeto() {
        return quilometros;
    }

    @Override
    public int distanciaTotal() {
        return distancia;
    }

    @Override
    public String toString() {
        return " " + "Matricula = " + matricula + ", Marca = " + marca + ", Modelo = " + modelo + ", Potencia = " + potencia + ", Último Trajeto = " + quilometros + "km " + ", Distancia total = " + distancia + "km. ";

    }

    
}
