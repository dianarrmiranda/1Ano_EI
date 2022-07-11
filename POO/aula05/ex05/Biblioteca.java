package aula05.ex05;
import java.util.ArrayList;
import aula05.ex04.*;

public class Biblioteca {
    private ArrayList<Livro> livros = new ArrayList<>();

	private ArrayList<Utilizador> alunos = new ArrayList<>();

	public void addAluno(String nome, int nmec, String curso) {
		alunos.add(new Utilizador(nome, nmec, curso));
	}

	public void removeAluno(int nMec) {
		alunos.remove(findAluno(nMec));
	}

	private int findAluno(int nMec) {
		int i = 0;
		for (Utilizador aluno : alunos) {
			if (aluno.getnMec() == nMec) {
				break;
			} else {
				i++;
			}
		}
		return i;
	}

	public void printAluno() {
		System.out.println("Lista de alunos:");
		for (Utilizador aluno : alunos) {
			System.out.println(aluno.toString());
		}
	}

	public void addLivro(String titulo, String tipoLivro) {
		livros.add(new Livro(titulo, tipoLivro));
	}

	public void printLivro() {
		System.out.println("Lista de livros:");

		for (Livro livro : livros) {
			System.out.println(livro.toString());
		}
	}

	private int findLivro(int lI) {
		int i = 0;
		for (Livro livro : livros) {
			if (livro.getId() == lI) {
				break;
			} else {
				i++;
			}
		}
		return i;
	}

	

	public void emprestar(int idAluno, int idLivro) {

		Utilizador thisAluno = alunos.get(findAluno(idAluno));
		Livro thisLivro = livros.get(findLivro(idLivro));
		

		if (Boolean.TRUE.equals(thisAluno.podeRequisitar())) {
			thisLivro.setStatus(false);
			thisAluno.getLivros().add(thisLivro.getId());
			System.out.println("Livro emprestado com sucesso");
		}
		else{
			System.out.println("Não pode requisitar mais livros");
		}
	}

	public void devolver(int idAluno, int idLivro) {

		Utilizador thisAluno = alunos.get(findAluno(idAluno));
		Livro thisLivro = livros.get(findLivro(idLivro));
		
		thisLivro.setStatus(true);

		ArrayList<Integer> LA = thisAluno.getLivros();

		for(int i = 0; i < LA.size(); i++){
            
			if(LA.get(i) == idLivro){
                LA.remove(i);
            }
        }
		System.out.println("Livro devolvido com sucesso");
	}
	public void printEmprestimo(int idAluno) {
		Utilizador thisAluno = alunos.get(findAluno(idAluno));
		for (int idLivro : thisAluno.getLivros()) {
			Livro thisLivro = livros.get(findLivro(idLivro));
			System.out.println(thisLivro.toString());
		}
		
	}

}
