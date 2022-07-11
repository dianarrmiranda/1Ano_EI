package aula09.Ex01;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import aula07.ex02.*;
import aula06.ex01.*;


public class AlDemo {

    public static void main(String[] args) {
        ArrayList<Integer> c1 = new ArrayList<>();
        for (int i = 10; i <= 100; i+=10)
            c1.add(i);
        System.out.println("Size: " + c1.size());
        
        for (int i = 0; i < c1.size(); i++)
            System.out.println("Elemento: " + c1.get(i));
        
        ArrayList<String> c2 = new ArrayList<>();
        c2.add("Vento");
        c2.add("Calor");
        c2.add("Frio");
        c2.add("Chuva");
        List<String> c22 = c2.subList(1, 3);
        System.out.println(c2);
        System.out.println(c22);
        Collections.sort(c2);
        System.out.println(c2);
        c2.remove("Frio");
        c2.remove(0);
        System.out.println(c2);
        System.out.println(c2.contains("Vento"));
        c1.set(3,30);
        System.out.println(c1);
        System.out.println(c1.indexOf(30));
        System.out.println(c1.lastIndexOf(30));
        

        Set<Pessoa> c3 = new HashSet<>();

        Pessoa p1 = new Pessoa("diana", 22222,new DateYMD(1, 4, 2000));
        Pessoa p2 = new Pessoa("ze", 22222,new DateYMD(30, 5, 2000));
        Pessoa p3 = new Pessoa("marta", 22222,new DateYMD(30, 5, 2000));
        Pessoa p4 = new Pessoa("diogo", 22222,new DateYMD(30, 5, 2000));
        Pessoa p5 = new Pessoa("sara", 22222,new DateYMD(30, 5, 2000));
        Pessoa p6 = new Pessoa("sara", 22222,new DateYMD(30, 5, 2000));
        
        c3.add(p1);
        c3.add(p2);
        c3.add(p3);
        c3.add(p4);
        c3.add(p5);
        c3.add(p3);
        c3.add(p6);

        Iterator<Pessoa> i=c3.iterator();
        while(i.hasNext())  
        {  
            System.out.println(i.next());  
        }  


        Set<DateND> c4 = new TreeSet<>();

        c4.add(new DateND(1,2,2000));
        c4.add(new DateND(5,6,2022));
        c4.add(new DateND(7,11,1990));
        c4.add(new DateND(30,1,2004));
        c4.add(new DateND(1,2,2006));

        for(DateND d: c4)
            System.out.println(d);
    }


    
}
