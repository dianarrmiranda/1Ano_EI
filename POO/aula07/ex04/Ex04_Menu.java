package aula07.ex04;
import java.util.Scanner;

public class Ex04_Menu {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        Robo[] roboseq1 = new Robo[3];
        Robo[] roboseq2 = new Robo[3];

        System.out.println("Nome equipa 1: ");
        String eq1name = input.nextLine();
        System.out.println("Responsável equipa 1: ");
        String eq1resp = input.nextLine();
        
        for(int i = 0; i < 3; i++){
            System.out.println("Id jogador " + (i+1) + ": ");
            String idjogador = input.next();
            System.out.println("Tipo jogador " + (i+1) + ": ");
            String tipojogador = input.next();
            System.out.println("Posição x " + (i+1) + ": ");
            int posx = input.nextInt();
            System.out.println("Posição y " + (i+1) + ": ");
            int posy = input.nextInt();
            roboseq1[i] = new Robo(idjogador, tipojogador, posx, posy);
        }

        Equipa eq1 = new Equipa(eq1name, eq1resp, roboseq1);
        
        System.out.println("Nome equipa 2: ");
        String eq2name = input.next();
        System.out.println("Responsável equipa 2: ");
        String eq2resp = input.next();

        for(int i = 0; i < 3; i++){
            System.out.println("Id jogador " + (i+1) + ": ");
            String idjogador = input.next();
            System.out.println("Tipo jogador " + (i+1) + ": ");
            String tipojogador = input.next();
            System.out.println("Posição x " + (i+1) + ": ");
            int posx = input.nextInt();
            System.out.println("Posição y " + (i+1) + ": ");
            int posy = input.nextInt();
            roboseq2[i] = new Robo(idjogador, tipojogador, posx, posy);
        }
        
        Equipa eq2 = new Equipa(eq2name, eq2resp, roboseq2);

        Bola bola = new Bola("azul", 0,0);

        Jogo jogo = new Jogo(eq1, eq2, bola, 5400);

        boolean sair= false;
        while (!sair){
            System.out.println("    ");
            System.out.println("Menu: ");
            System.out.println("1 - Marcar");
            System.out.println("2 - Mover");
            System.out.println("0 - Sair");
            System.out.println("Opção? ");
            int n = input.nextInt();

            switch(n){
                case 0:
                    sair = true;
                    break;
                case 1:
                    System.out.println("Equipa (1 ou 2): ");
                    int ideq = input.nextInt();
                    System.out.println("Jogador (0 a 3): ");
                    int idjogador = input.nextInt();
                    jogo.marcar(ideq, idjogador);
                    break;
                case 2:
                    System.out.println("1 - Mover Robo");
                    System.out.println("2 - Mover Bola");
                    System.out.println("Opção? ");
                    int op = input.nextInt();

                    switch(op){
                        case 1:
                            System.out.println("Equipa (1 ou 2): ");
                            int ideq1 = input.nextInt();
                            System.out.println("Jogador (0 a 3): ");
                            int idjogador1 = input.nextInt();
                            System.out.println("Posição x: ");
                            int posx1 = input.nextInt();
                            System.out.println("Posição y: ");
                            int posy1 = input.nextInt();
                            
                            if(ideq1 == 1){
                                roboseq1[idjogador1].mover(posx1, posy1);
                            } else {
                                roboseq2[idjogador1].mover(posx1, posy1);
                            }
                            break;
                        case 2:
                            System.out.println("Posição x: ");
                            int posx2 = input.nextInt();
                            System.out.println("Posição y: ");
                            int posy2 = input.nextInt();
                            bola.mover(posx2, posy2);
                            break;
                    }
                    break;

                default:
                    System.out.println("    ");
                    System.out.println("Invalid option!");
                    break;
            }

        }

        System.out.println(jogo.toString());
        
        input.close();
    

    }
}
