package aula08.Ex01;
import java.util.Scanner;

public class Ex01 {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int km, n, i = 0; 

        String[] veiculoMaxDist = new String[3];

        Veiculo[] viaturas = new Veiculo[7];

        viaturas[0] = new Motociclo( "Vespa", "Model t", 60, "desportivo").setMatricula("00-AA-00");
        viaturas[1] = new AutoLigeiro("Mercedes", "E", 2000, 100, 250).setMatricula("00-BB-00");
        viaturas[2] = new Taxi("Nissan", "FX",1400 ,201,100,450).setMatricula("00-FF-54");
        viaturas[3] = new PesadoPassa("Ferrari", "F-40", 1500 ,200,1000, 50).setMatricula("00-00-CC");
        viaturas[4] = new PesadoMerca("Toyota", "Y",700 ,202,3000,500).setMatricula("90-EA-54");
        viaturas[5] = new AutoLigEletrico("Tesla", "Model y", 980 ,101,300, 560).setMatricula("DD-00-00");
        viaturas[6] = new PesadoPassEletrico("NiKola", "Tre", 653 ,201,2500, 50,400).setMatricula("00-00-EE");


        EmpresaAlu empresa = new EmpresaAlu("Empresa Car", "2800-340", viaturas).setEmail("cart@gmail.com");

        boolean sair= false;
        while (!sair){
            System.out.println("Menu: ");
            System.out.println("1 - Adicionar um trajeto?");
            System.out.println("2 - Carregar um automóvel? ");
            System.out.println("3 - Ver Veiculos");
            System.out.println("0 - sair  ");
            n = sc.nextInt();
            switch(n){
                case 0:
                    sair = true;
                break;
                case 1:
                    System.out.println("1 - Motociclo");
                    System.out.println("2 - Automóvel Ligeiro");
                    System.out.println("6 - Taxi");
                    System.out.println("3 - Pesado Passageiros");
                    System.out.println("7 - Pesado Mercadorias");
                    System.out.println("4 - Automóvel Ligeiro Elétrico");
                    System.out.println("5 - Pesado de Passageiros Elétrico");
                    int x = sc.nextInt();
                    switch(x){
                        case 1:
                        case 2:
                        case 3:
                        case 4:
                        case 5:
                        case 6:
                        case 7:
                            i=1;
                            System.out.println("Insira 0 para parar.");
                            do{
                                System.out.println("Quilómetros percorridos na " + i++ + " viagem: ");
                                km = sc.nextInt();
                                if(km != 0){
                                    viaturas[x-1].trajeto(km);
                                }
                            }while(km!=0);
                        break;
                    }
                break;
                case 2:
                    System.out.println("1 - Automóvel Ligeiro Elétrico ");
                    System.out.println("2 - Pesado de Passageiros Elétrico");
                    int p = sc.nextInt();
                    switch(p){
                        case 1:  
                            System.out.println("Até que percentagem deseja carregar? ");
                            int carrega = sc.nextInt();
                            ((AutoLigEletrico)viaturas[3]).carregar(carrega);
                        break;
                        case 2:  
                            System.out.println("Até que percentagem deseja carregar? ");
                            carrega = sc.nextInt();
                            ((PesadoPassEletrico)viaturas[4]).carregar(carrega);
                        break;
                    }
                break;
                case 3:
                    System.out.println(empresa.toString());
                break;
                default:
                    System.out.println("    ");
                    System.out.println("Invalid option!");
                break;
            }
        }
       
        veiculoMaxDist = empresa.compararDistancia();

        System.out.println("A viatura com mais quilómetros percorridos é de matrícula " + veiculoMaxDist[0] + " que percorreu " + veiculoMaxDist[2] + "km.");
        
        sc.close();
    }

}
