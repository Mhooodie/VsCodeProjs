package JavaMain;

import java.util.Scanner;

class Negative0Positive {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        long input = sc.nextInt();

        if (input > 0) {
            System.out.println("Positive");
        } else if (input < 0){
            System.out.println("Negative");
        } else {
            System.out.println("Zero");
        }   
        sc.close();
        return;
    }
}