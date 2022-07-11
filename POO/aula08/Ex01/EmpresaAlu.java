package aula08.Ex01;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EmpresaAlu {
    private String nome, email;
    private String cp;
    private Veiculo[] viaturas = new Veiculo[5];

    public EmpresaAlu(String nome, String cp, Veiculo[] viaturas){
        this.nome = nome;
        this.cp = cp;
        this.viaturas = viaturas;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    } 

    public String getEmail(){
        return email;
    }

    public EmpresaAlu setEmail(String email){
        if (email != null && email.length() > 0) {
            String expression = "^[\\w\\.-_]+@([\\w\\-]+\\.)+[A-Z]{2,4}$";
            Pattern pattern = Pattern.compile(expression, Pattern.CASE_INSENSITIVE);
            Matcher matcher = pattern.matcher(email);
            if (matcher.matches()) {
                this.email = email;
            }else{
                System.out.println("Email Inválido!");
            }
        }
        return this;
    } 

    public String getCP(){
        return cp;
    }

    public void setCP(String cp){
        this.cp = cp;
    } 

    public Veiculo[] getViaturas(){
        return viaturas;
    }
    
    public void setViaturas(Veiculo[] viaturas) {
        this.viaturas = viaturas;
    }

    public String[] compararDistancia(){
        int max = 0;
        String matricula = "";
        String marca = "";
        String[] veiculoMaxDist = new String[3];

        for(int i = 0; i < viaturas.length; i++){
            if(viaturas[i].distanciaTotal() >= max){
                max = viaturas[i].distanciaTotal();
            }

            if(max == viaturas[i].distanciaTotal()){
                matricula = viaturas[i].getMatricula();
                marca = viaturas[i].getMarca();
            }
        }
        veiculoMaxDist[0] = matricula;
        veiculoMaxDist[1] = marca;
        veiculoMaxDist[2] = Integer.toString(max);

        return veiculoMaxDist;
    }

    public String printViaturas(){
        String s = "";
        for(int i=0; i<viaturas.length; i++){
            s += viaturas[i].toString() + "\n";
        }
        return s;
    }

    @Override
    public String toString() {
        return printViaturas();
    }



}
