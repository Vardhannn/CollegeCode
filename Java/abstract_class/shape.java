package abstract_class;

abstract class shape {
    int numberofslides(){
        return 0;
    }
}

class Trapezoid extends shape{
    int numberofslides(){
        return 4;
    }
}
class Triangle extends shape{
    int numberofslides(){
        return 3;
    }
}

class Hexagon extends shape{
    int numberofslides(){
        return 6;
    }
}

class test{
    public static void main(String[] args){
        shape s;
        s = new Triangle();
        System.out.println(s.numberofslides());
        s = new Hexagon();
        System.out.println(s.numberofslides());
        s = new Trapezoid();
        System.out.println(s.numberofslides());
    }
}