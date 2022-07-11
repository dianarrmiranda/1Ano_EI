package aula11.Ex02;
import java.util.Map;

public class Voos {
    private String hora, companhia, local, atraso, obs;
    private static Map<String,String> sigCompanhia;
    


    public Voos(String hora, String companhia, String local, String atraso){
        this.hora = hora;
        this.companhia = companhia;
        this.local = local;
        this.atraso = atraso;
        this.obs = horaPrev(hora, atraso);
    }

    

    public Voos(String hora, String companhia, String local){
        this.hora = hora;
        this.companhia = companhia;
        this.local = local;
        this.atraso = "";
        this.obs = "";
    }

    public String getCompanhia(){
        return this.companhia;
    }
    public String getlocal(){
        return this.local;
    }
    
    public String getAtraso(){
        return this.atraso;
    }

    public static void setCompanhias(Map<String,String> sigla){
        sigCompanhia = sigla;
    }

    public String horaPrev(String hora, String atraso){
        String[] horaMinuto = hora.split(":");
        String[] atrasoHoraMinuto = atraso.split(":");
        int atrasoMinuto = Integer.parseInt(atrasoHoraMinuto[1]) +  Integer.parseInt(horaMinuto[1]);
        int atrasoHora = Integer.parseInt(atrasoHoraMinuto[0]) + Integer.parseInt(horaMinuto[0]);

        while(atrasoMinuto>=60){
            atrasoHora += 1; 
            if(atrasoHora >23 ){
                atrasoHora=0;
            }
            atrasoMinuto = Integer.parseInt(atrasoHoraMinuto[1]) +  Integer.parseInt(horaMinuto[1]) - 60;

        }
        
        return String.format("%02d:%02d", atrasoHora, atrasoMinuto);
    }

    public static int stringToMinutos (String s) {
		String[] hm = s.split(":");
		int minutos = Integer.parseInt(hm[0]) * 60 + Integer.parseInt(hm[1]);
		return minutos;
	}

    public static String minutosToString (int m) {
		return String.format("%02d:%02d", (int)m/60, m%60);
	}

    @Override
	public String toString() {
		if (atraso.contentEquals("")) {
			return String.format("%-15s %-15s %-20s %-20s", hora, companhia,sigCompanhia.get(companhia.substring(0,2).trim()), local);
		} else {
			return String.format("%-15s %-15s %-20s %-20s     %-15s %-15s", hora, companhia,sigCompanhia.get(companhia.substring(0,2).trim()), local, atraso, "Previsto "+ obs);
		}
	}
}
