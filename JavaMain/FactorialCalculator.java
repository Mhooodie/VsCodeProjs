package JavaMain;

import java.util.Scanner;

class FactorialCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number;
        long factorial = 1;
        String YoN = "";

        while (true) {
            System.out.print("Enter a number to calculate its factorial: ");
            if (sc.hasNextInt()) {
                number = sc.nextInt();
                for (int i = 1; i <= number; i++) {
                    factorial *= i;
                }
                System.out.printf("The factorial of %d is %d\n", number, factorial);
                System.out.print("Would you like to check another number? (Y or N): ");
                sc.nextLine();
                if (sc.hasNextLine()) {
                    YoN = sc.nextLine().trim();
                    if (YoN.equalsIgnoreCase("y")) {
                        factorial = 1;
                        continue;
                    } else if (YoN.equalsIgnoreCase("n")) {
                        break;
                    } else {
                        System.out.println("Invalid input. Please enter Y or N.");
                        break;
                    }
                } else {
                    System.out.println("Input is not a single character.");
                    break;
                }
            } else {
                System.out.println("Invalid input. Please enter a valid integer.");
                sc.next(); 
            }
        }
        System.out.println("Goodbye!");
        sc.close();
        return;
    }
}

