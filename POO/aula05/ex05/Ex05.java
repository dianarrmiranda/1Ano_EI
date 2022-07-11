package aula05.ex05;
import java.util.Scanner;

public class Ex05 {
    public static void main(String[] args) {
		int n;
        Scanner scan = new Scanner(System.in);
        Biblioteca biblioteca = new Biblioteca();

        do{
            
            System.out.println("    ");
            System.out.println("Opções: ");
            System.out.println("1 - Inscrever utilizador");
            System.out.println("2 - Remover Utilizador");
            System.out.println("3 - Imprimir lista de utilizadores");
            System.out.println("4 - Registar um novo livro");
            System.out.println("5 - Imprimir lista de livros");
            System.out.println("6 - Emprestar");
            System.out.println("7 - Devolver");
            System.out.println("8 - Imprimir lista de emprestimos");
            System.out.println("9 - Sair");
            System.out.println("Opção? ");
            n = scan.nextInt();

            
        
            switch(n){
                
                case 1:
                    System.out.println("----------------------------------");
                    System.out.print("Nome: ");
                    String nome = scan.nextLine();
                    nome = scan.nextLine();
                    System.out.print("Nº Mecanográfico: ");
                    int nMec = scan.nextInt();
                    System.out.print("Curso: ");
                    String curso = scan.nextLine();
                    curso = scan.nextLine();
                    biblioteca.addAluno(nome, nMec, curso);
                    break;
                case 2:
                    System.out.print("Nº Mecanográfico: ");
                    int id = scan.nextInt();
                    biblioteca.removeAluno(id);
                    break;
                case 3:
                    biblioteca.printAluno();
                    break;
                case 4:
                    System.out.print("Título do Livro: ");
                    String titulo = scan.nextLine();
                    titulo = scan.nextLine();
                    System.out.print("Tipo de Livro: ");
                    String tipoLivro = scan.nextLine();
                    biblioteca.addLivro(titulo, tipoLivro);
                    break;
                case 5:
                    biblioteca.printLivro();
                    break;
                case 6:
                    System.out.print("Nº Mec: ");
                    int idAluno = scan.nextInt();
                    System.out.print("Id Livro: ");
                    int idLivro = scan.nextInt();
    
                    biblioteca.emprestar(idAluno, idLivro);
                    break;
                case 7:
                    System.out.print("Nº Mec: ");
                    int idA = scan.nextInt();
    
                    System.out.print("Id Livro: ");
                    int idL = scan.nextInt();
    
                    biblioteca.devolver(idA, idL);
                break;
                case 8:
                    System.out.print("Nº Mec: ");
                    int idal = scan.nextInt();
                    biblioteca.printEmprestimo(idal);
                    break;
                case 9:
                    System.out.println("----------------------------------");
                    System.out.println("Bye!");
                    break;
                default:
                    System.out.println("    ");
                    System.out.println("Invalid option!");
                    break;
        }
        }while(n!= 9);
        scan.close();
    }
}

