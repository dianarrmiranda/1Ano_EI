package aula05.ex02;
import aula05.ex01.*;

public class Calendar {
    public int diaSemana, ano, mes;
    
    public void setCalendar(int diaSemana, int ano){
        this.diaSemana = diaSemana;
        this.ano = ano;
    }

    public boolean validMonth(int m){ 
        return Date.validMonth(m);
    }

    public int diasNoMEs(int mes, int ano){
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
    public String NomeMes(int mes){
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
    public void printMes(int mes, int ano, int dia) {
        if(Boolean.TRUE.equals(validMonth(mes))) {
            System.out.println("");
		    System.out.format("%s   %s   %s   %s   %s   %s   %s    %n", "  ","  ",NomeMes(mes), ano,"","","");
            System.out.println("");
            System.out.format("%s   %s   %s   %s   %s   %s   %s   %n", "Su", "Mo", "Tu", "We", "Th", "Fr", "Sa");
		    int counter = dia;
		
		    int j = 0;
		
		    while (j < dia-1) {
			    System.out.print("     ");
			    j++;
		    }

            if (counter % 8 == 0) {
                System.out.print("\n");
            }
            System.out.printf("%02d   ", 1);

		    for (int i = 2; i <= diasNoMEs(mes, ano); i++) {

			    if (counter % 7 == 0) {
				    System.out.print("\n");
			    }
                System.out.printf("%02d   ", i);

			    counter++;
		    }

            System.out.printf("%n");

        }else{
            System.out.println("Mês inválido");
        }
        
	}
    public void printCalendar(int ano, int dia) {
        int m = 1;

        while (m <= 12) {
            printMes(m, ano, dia);
            m++;
            dia++;
            

            if(dia > 7){
                dia = 1;
            }
            
        }
	}
    
}
