package qcm;

public class Programme {
	public static void main(String[] args) {
		
		Qcm qcm = new Qcm(50);
		qcm.setGoodAnswer(50);
		Projet projet = new Projet();
		projet.setNote(10, 10);
		Examen exam = new Examen();
		exam.setNote(10);
		Diplome diplome = new Diplome(qcm, projet, exam);
		System.out.println(diplome.isValide());		
	}
}
