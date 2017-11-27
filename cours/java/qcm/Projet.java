package qcm;

public class Projet extends Examen {
	public void setNote(int noteW, int noteO) {
		this.setNote(noteW + noteO);
	}
}
