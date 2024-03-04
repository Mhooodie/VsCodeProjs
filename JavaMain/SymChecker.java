package JavaMain;

import java.util.Scanner;

class SymChecker {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        String num = sc.nextLine();
        int numlen = num.length();
        int numlen2 = (numlen / 2);
        int numFront = 0;
        int numBack = numlen - 1;
        int numScore = 0;

        for (int i = 0; i < numlen2; i++) {
            if (num.charAt(numFront) == num.charAt(numBack)) {
                numFront++;
                numBack--;
                numScore++;
            } else {
                break;
            }

        }

        if (numScore == numlen2) {
            System.out.println("It is Symetrica!");
        } else {
            System.out.println("It is not Symetrical");
        }
        sc.close();
        return;
    }
}