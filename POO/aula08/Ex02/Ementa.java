package aula08.Ex02;


public class Ementa {
    private String nome, local;
    private Prato[] pratos = new Prato[7];

    public Ementa(String nome,String local){
        this.nome = nome;
        this.local = local;
    }

    public void addPrato(Prato prato, DiaSemana diaSemana) {
        int index = diaSemana.ordinal();
        pratos[index] = prato;
    }

    @Override
    public String toString() {
        String s = "";
        for(int i = 0; i < 7; i++){
            s += pratos[i] + ", dia " + DiaSemana.values()[i] + "\n";
        }
        return nome +" - " + local +"\n"+ s;
    }
}


