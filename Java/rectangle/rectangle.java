package rectangle;

import java.util.Scanner;

public class rectangle {
    float length;
    float width;
    rectangle(){
    }
    void area(){
        float areaofrectangle = length * width;
        System.out.println("area of a rectangle is :"+areaofrectangle);

    }
    void perimeter(){
        float perimeterofrectangle = 2*(length+width);
        System.out.println("perimeter of a rectangle is:"+perimeterofrectangle);

    }
    public static void main(String[] args){
        rectangle obj = new rectangle();
        Scanner obj1 = new Scanner(System.in);
        obj.length = obj1.nextFloat();
        obj.width = obj1.nextFloat();
        obj.area();
        obj.perimeter();

    }
}
