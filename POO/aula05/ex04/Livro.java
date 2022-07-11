package aula05.ex04;

public class Livro {
    private int id;
    private String titulo;
    private String tipoEmprestimo;
    private static int contador = 100;
    private String disp;
    private boolean status;

    public Livro(String titulo){
		this.titulo = titulo; 
        this.tipoEmprestimo = "Normal"; 
        this.id = contador++; 
	}
	public Livro(String titulo, String tipoLivro) {
		this(titulo); 
        this.tipoEmprestimo = tipoLivro; 
	}

    public boolean isStatus() {
		return status && !"Condicionado".equals(tipoEmprestimo);
	}

	public void setStatus(boolean status) {
		this.status = status;
        
	}

    public void setId(int id) {
        this.id = id;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    public void setTipoEmprestimo(String tipoEmprestimo) {
        this.tipoEmprestimo = tipoEmprestimo;
    }
    public void setDisp(String disp) {
        this.disp = disp;
    }
    public int getId() {
        return id;
    }
    public String getTitulo() {
        return titulo;
    }
    public String getTipoEmprestimo() {
        return tipoEmprestimo;
    }
    public String getDisp() {
        return disp;
    }
    public String toString() {
		return "Livro " + id + "; " + titulo + "; " + tipoEmprestimo;
	}
}
