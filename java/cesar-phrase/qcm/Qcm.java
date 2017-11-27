package qcm;

public class Qcm extends Examen {
	private int nQuestions;
	public Qcm(int nQuestions) {
		this.nQuestions = nQuestions;
	}
	public void setGoodAnswer(int n) {
		this.setNote(((n *20) / this.nQuestions));
	}
}
