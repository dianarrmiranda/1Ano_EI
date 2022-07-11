package aula05.ex04;
import java.util.ArrayList;

public class Ex04 {
    public static void main(String[] args){
        Livro[] catalogo = new Livro[10];
        catalogo[0] = new Livro("Java 8", "Condicional");
        catalogo[1] = new Livro("POO em Java 8");
        catalogo[2] = new Livro("Java para totós", "Normal");
        catalogo[2].setTipoEmprestimo("Condicional");

        for(int i = 0; i < catalogo.length; i++){
            if(catalogo[i] != null){
                System.out.println("ID = " + catalogo[i].getId() + ", " + catalogo[i].getTitulo() + ", " + catalogo[i].getTipoEmprestimo());
            }
        }

        ArrayList<Utilizador> alunos = new ArrayList<>();

        alunos.add(new Utilizador("Catarina Marques", 80231, "MIEGI"));
        alunos.add(new Utilizador("João Silva", 90123, "LEI"));
        alunos.get(1).setnMec(80123);

        for(Utilizador u: alunos){
            System.out.println(u);
        }
    }
}
