package qcm;

public class Diplome {
	private Examen[] examen;
	
	public Diplome(Examen... exam) {
		this.examen = exam;
	}
	
	
	public Boolean isValide() {
		int moyenne = 0;
		for(Examen exam : examen) {
			moyenne += exam.getNote();
		}
		moyenne = moyenne / examen.length;
		if(moyenne >= 10) {
			return true;
		}
		else {
			return false;
		}
	}
}
