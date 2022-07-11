package aula04;
import java.util.Scanner;

public class ex04 {
    public static void main(String[] args){
        int mes, ano, dia, diasdoMes;
        Scanner sc = new Scanner(System.in);

        do{
            System.out.print("Mês: ");
            mes = sc.nextInt();
            if (mes<=0 || mes>12){
                System.out.println("Mês inválido! (Entre 1 e 12)");
            }
        }while(mes<=0 || mes>12);
        do{
            System.out.print("Ano: ");
            ano = sc.nextInt();
            if (ano<0){
                System.out.println("Ano inválido! (Tem de ser positivo)");
            }
        }while(ano<0);
        do{
            System.out.print("Dia da semana: ");
            dia = sc.nextInt();
            if (dia<=0 || dia>7){
                System.out.println("Dia inválido! (Entre 1 e 7)");
            }
        }while(dia<=0 || dia>7);
    
        diasdoMes = diasNoMEs(mes, ano);

        String month = NomeMes(mes);

        printCalendario(diasdoMes, ano, dia, month);
		
        sc.close();
    }
    public static int diasNoMEs(int mes, int ano){
        int dias;
        switch (mes){
            case 1: 
            case 3:dias = 31; break;
            case 2: 
                if((ano%4 == 0) && ((ano%100 != 0) || (ano%400 == 0))){
                    dias = 29;
                }else{dias = 28;
                }break;
            case 5:
            case 7:
            case 8:
            case 10:
            case 12: dias = 31; break;
            default: dias = 30;
        }
        return dias;
    }
    public static String NomeMes(int mes){
        String nomeM;
        switch (mes){
            case 1: nomeM = "Janeiro"; break;
            case 2: nomeM = "Fevereiro"; break;
            case 3: nomeM = "Março"; break;
            case 4: nomeM = "Abril"; break;
            case 5: nomeM = "Maio"; break;
            case 6: nomeM = "Junho"; break;
            case 7: nomeM = "Julho"; break;
            case 8: nomeM = "Agosto"; break;
            case 9: nomeM = "Setembro"; break;
            case 10: nomeM = "Outubro"; break;
            case 11: nomeM = "Novembro"; break;
            case 12: nomeM = "Dezembro"; break;
            default: nomeM = "Mês inválido";
        }
        return nomeM;
    }
    static void printCalendario(int mes, int ano, int dia, String month) {
        System.out.println("");
		System.out.format("%s   %s   %s   %s   %s   %s   %s    %n", "  ","  ",month, ano,"","","");
        System.out.println("");
        System.out.format("%s   %s   %s   %s   %s   %s   %s   %n", "Su", "Mo", "Tu", "We", "Th", "Fr", "Sa");
		int counter = dia;
		
		int j = 0;
		
		while (j < dia) {
			System.out.print("     ");
			j++;
		}

		for (int i = 1; i <= mes; i++) {

			if (counter % 7 == 0) {
				System.out.print("\n");
			}
            System.out.printf("%02d   ", i);

			counter++;
		}

	}

}
