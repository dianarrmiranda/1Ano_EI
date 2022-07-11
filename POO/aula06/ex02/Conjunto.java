package aula06.ex02;

public class Conjunto {

    private int[] vetor;

    public Conjunto(){
        this.vetor = new int[0];
    }

    public int[] getVetor(){
        return vetor;
    }
    public boolean contains(int n){
        for(int i=0; i<vetor.length; i++){
            if(vetor[i] == n){
                return true;
            }
        }
        return false;
    }
    
    public void insert(int n){
        if(this.contains(n)){
            return;}
        int newlen = vetor.length + 1;
        int[] newVetor = new int[newlen];
        
        for(int i=0; i<vetor.length; i++){
            newVetor[i] = vetor[i];
        }

        newVetor[newlen-1] = n;
        vetor = newVetor;
    }

    public void remove(int n){
        if(!this.contains(n)){return;}
        int newlen = vetor.length - 1;		
		int[] newVetor = new int[newlen];		
		boolean removed = false;		//variavél indica se o elemento já foi removido
		
		for(int i=0; i<vetor.length; i++) {
			if(vetor[i] == n) {
				removed = true;
				continue;
			}
			if(!removed) {
				newVetor[i] = vetor[i];
			} else {
				newVetor[i-1] = vetor[i];
			}
		}
		vetor = newVetor;
    }

    public void empty(){
        vetor = new int[0];
    }

    public int size(){
        return vetor.length;
    }

    public String toString(){
        String s = "{";
        for(int i=0; i<vetor.length; i++){
            s += vetor[i];
            if(i != vetor.length-1){
                s += ", ";
            }
        }
        s += "}";
        return s;
    }

    public Conjunto combine(Conjunto add){
        Conjunto c2 = new Conjunto();
        for(int i=0; i<vetor.length; i++){
            c2.insert(vetor[i]);
        }
        for(int i=0; i<add.getVetor().length; i++){
            c2.insert(add.getVetor()[i]);
        }
        return c2;
    }

    public Conjunto intersect(Conjunto inter){
        Conjunto c2 = new Conjunto();
        for(int i=0; i<vetor.length; i++){
            if(inter.contains(vetor[i])){
                c2.insert(vetor[i]);
            }
        }
        return c2;
    }

    public Conjunto subtract(Conjunto dif){
        Conjunto c2 = new Conjunto();
        for(int i=0; i<vetor.length; i++){
            if(!dif.contains(vetor[i])){
                c2.insert(vetor[i]);
            }
        }
        return c2;
    }




}
