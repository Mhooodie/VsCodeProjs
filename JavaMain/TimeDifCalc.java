package JavaMain;

import java.util.Scanner;

class TimeDifCalc {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter Hour 1:");
        int hour1 = scanner.nextInt();
        System.out.println("Enter Minute 1:");
        int minute1 = scanner.nextInt();
        System.out.println("Enter Second 1:\n");
        int second1 = scanner.nextInt();

        System.out.println("Enter Hour 2:");
        int hour2 = scanner.nextInt();
        System.out.println("Enter Minute 2:");
        int minute2 = scanner.nextInt();
        System.out.println("Enter Second 2:");
        int second2 = scanner.nextInt();

        long totsec1 = (hour1 * 60 * 60) + (minute1 * 60) + second1;
        long totsec2 = (hour2 * 60 * 60) + (minute2 * 60) + second2;

        if (totsec1 >= totsec2) {
            long difsec = totsec1 - totsec2;  
            System.out.println("The difference in seconds is:");
            System.out.println(difsec);
            scanner.close();
        } else {
            long difsec = totsec2 - totsec1;
            System.out.println("The difference in Seconds is:");   
            System.out.println(difsec); 
            scanner.close();
        }
        return;
    }
}
