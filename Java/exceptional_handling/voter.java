package exceptional_handling;

import java.util.Scanner;

public class voter {
    int age;
    void eligible() throws Exception {
        Scanner sc = new Scanner(System.in);
        age = sc.nextInt();
        if (age >= 18){
            System.out.println("you are eligible");
        }
        else{
            throw new ArithmeticException("you are not eligible");
        }
    }
    public static void main(String[] args) throws Exception {
        voter obj = new voter();
        obj.eligible();
    }
}
