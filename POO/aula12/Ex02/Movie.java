package aula12.Ex02;

public class Movie implements Comparable<Object>{
    private String name, rating, genre;
    private double score;
    private int runTime;
    
    public Movie(String name, double score, String rating, String genre, int runTime){
        this.name = name;
        this.score = score;
        this.rating = rating;
        this.genre = genre;
        this.runTime = runTime;
    }

    public String getGenre(){
        return this.genre;
    }

    public String getName(){
        return this.name;
    }

    public Double getScore(){
        return this.score;
    }

    public int getRunTime(){
        return this.runTime;
    }


    @Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
 
        if (!(o instanceof Movie)) {
            return false;
        }

        Movie m = (Movie) o;

        return name.equalsIgnoreCase(m.name)
                && Double.compare(score, m.score) == 0
                && rating.equalsIgnoreCase(m.rating)
                && genre.equalsIgnoreCase(m.genre)
                && Integer.compare(runTime, m.runTime) == 0;
    }

    @Override
    public int compareTo(Object o){
        Movie m = (Movie) o;
        return this.name.toLowerCase().compareTo(m.name.toLowerCase());
    }
    
    @Override
    public String toString(){
        return String.format("%-40s %-10s %-10s %-15s %-10s", name, score,rating, genre, runTime);
    }

}