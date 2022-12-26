package exceptional_handling;

import java.util.Scanner;

public class zero_divison {
    int a;
    int b;
    float result;
    float add(){
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        try{
            result = a / b;
        }
        catch (ArithmeticException e){
            System.out.println("Can't divide by zero");
        }
        return result;
    }
    public static void main(String[] args){
        zero_divison obj = new zero_divison();
        obj.add();





    }
}
