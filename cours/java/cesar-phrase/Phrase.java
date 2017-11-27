public class Phrase {
	
	private String separateur = " ";
	private String laphrase = "";
	
    public String ajouter(String a, int b){
    	if(b != 0) {
	    	for(int i=0;i<b;i++) {
	    		this.laphrase+=a+this.separateur;
	    	}
    	}
    	return laphrase;
    }
    public String ajouter(String a){
    	this.laphrase+=a+this.separateur;
    	return laphrase;
    }
    public String ajouter(String... a){
    	for (String j : a) {
    		this.laphrase+=j+this.separateur;
    	}
    	return laphrase;
    }
    public String setSeparateur(String a){
    	this.separateur = a;
    	return separateur;
    }
    public String setSeparateur(char a){
    	this.separateur = ""+a;
    	return separateur;
    }
    public int getNbLettres(){
    	char[] tab = this.laphrase.toCharArray();
    	int nb = tab.length;
    	return nb;
    }
    public String toString() {
    	return this.laphrase;
    }
    public static void main(String[] args){
    	Phrase phrase = new Phrase();
    	phrase.ajouter("Une");
    	phrase.ajouter("classe");
    	phrase.ajouter("pour");
    	phrase.ajouter("ajouter");
    	phrase.ajouter("des mots");
    	phrase.setSeparateur(" et encore ");
    	phrase.ajouter("des mots", 3);
    	phrase.setSeparateur(' ');
    	phrase.ajouter("toujours", "et", "encore");

    	System.out.println(phrase);
    	System.out.println(phrase.getNbLettres());
    }
}