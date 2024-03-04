package JavaMain;

import java.util.Scanner;

class _3ValSumChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Sum 20 Checker");
        System.out.println("--------------------");


        System.out.println("Enter Num of Sum to Check: ");
        int sum = sc.nextInt();

        System.out.println("Enter Num 1: ");
        int a = sc.nextInt();
        System.out.println("Enter Num 2: ");
        int b = sc.nextInt();
        System.out.println("Enter Num 3: ");
        int c = sc.nextInt();
        boolean track = true; 
        
        boolean ab = false;
        boolean bc = false;
        boolean ca = false;


        if (a + b == sum) {
            track = true;
            ab = true;
        } else if (b + c == sum) {
            track = true;
            bc = true;
        } else if (c + a == sum) {
            track = true;
            ca = true;
        } else {
            track = false;
        }
        if (track == true) {
            System.out.println("2 of your values add up to " + (sum) + "!");
            if (ab == true) {
                System.out.println("The values that add to " + (sum) + " are: " + (a) + " and " + (b) + ".");
            } else if (bc == true) {
                System.out.println("The values that add to " + (sum) + " are: " + (b) + " and " + (c) + ".");
            } else if (ca == true) {
                System.out.println("The values that add to " + (sum) + " are: " + (c) + " and " + (a) + ".");
            } else {
                System.out.println("ERROR - RESETART APPLICATION!");
            }
        } else {
            System.out.println("none of your values add up to " + (sum) + ".....");
        }
        sc.close();
        return;
    }
}