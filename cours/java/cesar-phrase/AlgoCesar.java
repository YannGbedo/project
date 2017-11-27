public class AlgoCesar {

  public String encrypte(String s) {
	  char alphabetMin[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z' };
	  char alphabetMaj[] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z' };
	  char[] tab = s.toCharArray();
	  String t = "";
	  char alphabet[] = alphabetMin;
	  for(int j=0;j<tab.length;j++) {
		  if(Character.isDigit(tab[j]) ){
			  t=s;
		  }else{
			  Boolean verif = false;
			  if(Character.isUpperCase(tab[j])) {
				  alphabet = alphabetMaj;
			  }else if(Character.isLowerCase(tab[j])){
				  alphabet = alphabetMin;
			  }else{
				  t+=tab[j];
				  verif=true;
			  }
			  if(verif==false) {
				  int compteur = new String(alphabet).indexOf(tab[j]);
				  compteur+=23;
				  if(compteur>25) {
					  compteur=compteur-26;
				  }
				  t = t + alphabet[compteur];
			  }
		  }
	  }
	  return t;
  }

  public static void main(String[] args) {
    AlgoCesar algoCesar = new AlgoCesar();

    String resultat = algoCesar.encrypte("");
    System.out.println("".equals(resultat));

    resultat = algoCesar.encrypte("az");
    System.out.println("xw".equals(resultat));
    

    
    resultat = algoCesar.encrypte("AZ");
    System.out.println("XW".equals(resultat));
    

    resultat = algoCesar.encrypte("1,000.00");
    System.out.println("1,000.00".equals(resultat));

    
    String phrase = "In cryptography, a Caesar cipher is one "
                    + "of the simplest and most widely known "
                    + "encryption techniques.";
    resultat = algoCesar.encrypte(phrase);

    String phraseAttendue = "Fk zovmqldoxmev, x Zxbpxo zfmebo fp lkb "
                            + "lc qeb pfjmibpq xka jlpq tfabiv hkltk "
                            + "bkzovmqflk qbzekfnrbp.";
    System.out.println(phraseAttendue.equals(resultat));
    
  }
}
