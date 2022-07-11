package aula07.ex01;
import java.util.Scanner;

public class Ex03 {
	public static void main(String[] args) {
		int n, x = 0;
		String cor;
        double r = 0, comp = 0, alt= 0, l1 = 0, l2=0, l3=0;
        Scanner sc = new Scanner(System.in);
		Forma retangulo, circulo, triangulo;
		
		retangulo = new Retangulo(comp, alt);
		circulo = new Circulo(r);
		triangulo = new Triangulo(l1,l2,l3);
		do{
			System.out.print("Cor da forma: ");
			cor = sc.nextLine();
			if(cor.isEmpty()){
				System.out.println("Cor inválida!");
			}
			else{
				break;
			}
		}while(cor.isEmpty());

		Forma.setcor(cor);

        do{

            System.out.println("------------------------------");
            System.out.println("Forma?");
			System.out.println("1 - Circulo");
			System.out.println("2 - Retangulo");
			System.out.println("3 - Triangulo");
            System.out.println("Opção? ");
			System.out.println("------------------------------");
            n = sc.nextInt();

			if( n == 1){
				System.out.println("Circulo:");
				System.out.println("   1 - Inserir raio. ");
				System.out.println("   2 - Calcular area.  ");       
				System.out.println("   3 - Calcular perimetro. ");
				System.out.println("   4 - Ver cor. ");
				System.out.println("   0 - Sair");
				System.out.println("------------------------------");
				x = sc.nextInt();

			}else if(n == 2){
				System.out.println("Retangulo:");
				System.out.println("   5  - Inserir comprimento e altura. ");
				System.out.println("   6  - Calcular area.  ");       
				System.out.println("   7  - Calcular perimetro. ");
				System.out.println("   8  - Ver cor. ");
				System.out.println("   0  - Sair");
				System.out.println("------------------------------");
				x = sc.nextInt();
			}else if (n == 3){
				System.out.println("Triangulo:");
				System.out.println("   9  - Inserir lados. ");
				System.out.println("   10 - Calcular area.  ");       
				System.out.println("   11 - Calcular perimetro. ");
				System.out.println("   12 - Ver cor.");
				System.out.println("   0  - Sair");
				System.out.println("------------------------------");
				x = sc.nextInt();
			}

            switch(x){
                case 0:
					System.out.println("----------------------------------");
                    System.out.println("Bye!");
                    break;
                case 1:
					System.out.print("Raio: ");
					r = sc.nextDouble();
					retangulo = new Retangulo(comp, alt);
					((Circulo)circulo).setCirculo(r);
					break;
                case 2:
					System.out.println(circulo.toString());
					System.out.printf("Area: %.2f %n", circulo.area());
					break;
                case 3:
					System.out.println(circulo.toString());
					System.out.printf("Perimetro: %.2f %n", circulo.perimetro());
                    break;
                case 5:
					System.out.println("----------------------------------");
					System.out.print("Comprimento: ");
					comp = sc.nextDouble();
					System.out.print("Altura: ");
					alt = sc.nextDouble();
					((Retangulo)retangulo).setRetangulo(comp, alt);
					break;
				case 6:
					System.out.println(retangulo.toString());
					System.out.printf("Area: %.2f %n", retangulo.area());
					break;
				case 7:
					System.out.println(retangulo.toString());
					System.out.printf("Perimetro: %.2f %n", retangulo.perimetro());
					break;
				case 9:
					System.out.println("----------------------------------");
					System.out.print("Lado 1: ");
					l1 = sc.nextDouble();
					System.out.print("Lado 2: ");
					l2 = sc.nextDouble();
					System.out.print("Lado 3: ");
					l3 = sc.nextDouble();
					((Triangulo)triangulo).setTriangulo(l1, l2, l3);
					break;
				case 10:
					System.out.println(triangulo.toString());
					System.out.printf("Area: %.2f %n", triangulo.area());
					break;
				case 11:
					System.out.println(triangulo.toString());
					System.out.printf("Perimetro: %.2f %n", triangulo.perimetro());
					break;
				case 4:
				case 8:
				case 12:
					System.out.println(Forma.print(cor));
					break;
                default:
					System.out.println("----------------------------------");
                    System.out.println("Opção inválida!");
                    break;
        }
        }while(x!= 0);
        sc.close();
    }
}
