package aula05.ex03;
import java.util.Scanner;

public class Ex03 {
	public static void main(String[] args) {
		int n;
        double r, comp, alt, l1, l2, l3;
        Scanner sc = new Scanner(System.in);
        Circulo circulo = new Circulo();
		Triangulo triangulo = new Triangulo();
		Retangulo retangulo = new Retangulo();

        do{
            
            System.out.println("------------------------------------------------------------------------------------------------------------");
            System.out.println("Opções: ");
            System.out.println("Circulo:                       | Retangulo                              | Triangulo");
			System.out.println("   1 - Inserir raio.           |   4 - Inserir comprimento e altura. 	|   7 - Inserir lados");
			System.out.println("   2 - Calcular area.          |   5 - Calcular area.                   |   8 - Calcular area");       
			System.out.println("   3 - Calcular perimetro.     |   6 - Calcular perimetro.              |   9 - Calcular perimetro");
            System.out.println("Opção? ");
            n = sc.nextInt();
        
            switch(n){
                case 0:
					System.out.println("----------------------------------");
                    System.out.println("Bye!");
                    break;
                case 1:
					System.out.println("----------------------------------");
                    System.out.print("Raio: ");
                    r = sc.nextDouble();
					circulo.setCirculo(r);
                    break;
                case 2:
					System.out.println(circulo.toString());
					System.out.printf("Area: %.2f %n", circulo.area());
                    break;
                case 3:
					System.out.println(circulo.toString());
					System.out.printf("Perimetro: %.2f %n", circulo.perimetro());
                    break;
                case 4:
					System.out.println("----------------------------------");
					System.out.print("Comprimento: ");
					comp = sc.nextDouble();
					System.out.print("Altura: ");
					alt = sc.nextDouble();
					retangulo.setRetangulo(comp, alt);
                    break;
				case 5:
					System.out.println(retangulo.toString());
					System.out.printf("Area: %.2f %n", retangulo.area());
					break;
				case 6:
					System.out.println(retangulo.toString());
					System.out.printf("Perimetro: %.2f %n", retangulo.perimetro());
					break;
				case 7:
					System.out.println("----------------------------------");
					System.out.print("Lado 1: ");
					l1 = sc.nextDouble();
					System.out.print("Lado 2: ");
					l2 = sc.nextDouble();
					System.out.print("Lado 3: ");
					l3 = sc.nextDouble();
					triangulo.setTriangulo(l1, l2, l3);
					break;
				case 8:
					System.out.println(triangulo.toString());
					System.out.printf("Area: %.2f %n", triangulo.area());
					break;
				case 9:
					System.out.println(triangulo.toString());
					System.out.printf("Perimetro: %.2f %n", triangulo.perimetro());
					break;
                default:
					System.out.println("----------------------------------");
                    System.out.println("Opção inválida!");
                    break;
        }
        }while(n!= 0);
        sc.close();
    }
}
