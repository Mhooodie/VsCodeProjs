package JavaMain.CodingBatProblems;

import java.util.Scanner;

class String2WordEnds {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

    System.out.println("Enter Chars: ");    
    String str = sc.nextLine();
    System.out.println("Enter Main Word: ");
    String word = sc.nextLine();

  int slen = str.length();
  int wlen = word.length();
  String fin = "";

  for (int i = 0; i < slen-wlen+1; i++) {
    String tmp = str.substring(i,i+wlen);
    if (i > 0 && tmp.equals(word))
      fin += str.substring(i-1,i);
    if (i < slen-wlen && tmp.equals(word))
      fin += str.substring(i+wlen,i+wlen+1);
  }
  System.out.println("Result: " + fin);
  sc.close();
  return;
    }
}
