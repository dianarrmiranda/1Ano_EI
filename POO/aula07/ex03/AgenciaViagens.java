package aula07.ex03;

import java.util.ArrayList;
import java.util.Scanner;

public class AgenciaViagens {
    private ArrayList<Carro> carros;
    private ArrayList<Alojamento> alojamento;
    private String nome;
    private String endereco;
    private static Scanner input = new Scanner(System.in);

    public AgenciaViagens(String nome, String endereco, ArrayList<Carro> carros, ArrayList<Alojamento> alojamento) {
        this.nome = nome;
        this.endereco = endereco;
        this.carros = carros;
        this.alojamento = alojamento;
    }

    public ArrayList<Carro> getCarros() {
        return carros;
    }

    public void setCarros(ArrayList<Carro> carros) {
        this.carros = carros;
    }

    public ArrayList<Alojamento> getAlojamento() {
        return alojamento;
    }

    public void setAlojamento(ArrayList<Alojamento> alojamento) {
        this.alojamento = alojamento;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    //adicionar apartamento
    public void adicionarAlojamento() {
        double avaliacao = 0;
        System.out.println("Digite o codigo: ");
        String codigo = input.nextLine();
        System.out.println("Digite o nome: ");
        String nome = input.nextLine();
        System.out.println("Digite o local: ");
        String local = input.nextLine();
        System.out.println("Digite o preco por noite: ");
        double precoNoite = input.nextDouble();
        System.out.println("Está disponível? (Sim/Não)");
        String a = input.next();
        boolean disponivel = verificarDisponibilidade(a);
        do{
            System.out.println("Avaliação (1.0, 5.0): ");
            avaliacao = input.nextDouble();
        }while(!validateAvaliacao(avaliacao));
        System.out.println("Número de quartos: ");
        int numeroQuartos = input.nextInt();
        alojamento.add(new Apartamento(codigo, nome, local, precoNoite, disponivel, avaliacao, numeroQuartos));
    }

    public boolean validateAvaliacao(double avaliacao) {
        if (avaliacao >= 1.0 && avaliacao <= 5.0) {
            return true;
        } else {
            System.out.println("Avaliação inválida");
            return false;
        }
    }

    //adicionar quarto hotel
    public void adicionarQuarto() {
        System.out.println("Digite o codigo: ");
        String codigo = input.nextLine();
        
        System.out.println("Digite o nome: ");
        String nome = input.nextLine();
        System.out.println("Digite o local: ");
        String local = input.nextLine();
        System.out.println("Digite o preco por noite: ");
        double precoNoite = input.nextDouble();
        System.out.println("Está disponível? (Sim/Não)");
        boolean disponivel = input.nextBoolean();
        System.out.println("Avaliação (1.0, 5.0): ");
        double avaliacao = input.nextDouble();
        System.out.println("Tipo de quarto: ");
        String tipo = input.nextLine();
        alojamento.add(new QuartoHotel(codigo, nome, local, precoNoite, disponivel, avaliacao, tipo));
    }

    private boolean verificarDisponibilidade(String disponivel){
        return disponivel.equals("Sim") || disponivel.equals("sim");
    }

    public void adicionarCarro() {
        System.out.println("Classe: ");
        char classe =(char) input.next().charAt(0);
        input.nextLine();
        System.out.println("Motorização: ");
        String motorizacao = input.nextLine();
        carros.add(new Carro(classe,motorizacao));
    }

    public void verAlojamentos() {
        for (Alojamento alojamento : alojamento) {
            System.out.println(alojamento.toString());
        }
    }

    public void verCarros() {
        for (Carro c : carros) {
            System.out.println(c.toString());
        }
    }

    //emprestar carro
    public void emprestarCarro() {
        System.out.println("Código: ");
        int codigo = input.nextInt();

        if(carros.get(encontrarCarro(codigo)).isDisponivel()){
            carros.get(encontrarCarro(codigo)).setDisponivel(false);
            System.out.println("Carro emprestado com sucesso!");

        }else{
            System.out.println("Carro indisponível!");
        }
    }

    //encontrar Carro
    private int encontrarCarro(int codigo) {
        int i = 0;
        for (Carro c : carros) {
            if (c.getCodigo() == codigo) {
                return i;
            }
            i++;
        }
        return i;
    }

    //reservar alojamento

    public void reservarAlojamento() {
        System.out.println("Código: ");
        int codigo = input.nextInt();
        if(alojamento.get(encontrarAlojamento(codigo)).isDisponivel()){
            alojamento.get(encontrarAlojamento(codigo)).setDisponivel(false);
            System.out.println("Alojamento reservado com sucesso!");
        }else{
            System.out.println("Alojamento indisponível!");
        }
    }

    //encontrar alojamento
    private int encontrarAlojamento(int codigo) {
        int i = 0;
        for (Alojamento a : alojamento) {
            if (Integer.parseInt(a.getCodigo()) == codigo) {
                return i;
            }
            i++;
        }
        return i;
    }


    
}
