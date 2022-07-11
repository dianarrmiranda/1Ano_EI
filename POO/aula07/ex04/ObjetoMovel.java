package aula07.ex04;

public abstract class ObjetoMovel {
    private int x, y, dist = 0;

    public ObjetoMovel(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getDist() {
        return dist;
    }

    public void mover(int x, int y) {
        this.x += x;
        this.y += y;
        dist+=(x+y);
    }

    @Override 
    public String toString() {
        return "[ x = " + x + ", y = " + y + ", dist = " + dist + " ] " + " ".concat(super.toString());
    }
  
}
