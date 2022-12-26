package bird;

public class bird extends animal{
    public void fly(){
        System.out.println("i can fly");
    }
    public static void main(String[] args){
        bird obj = new bird();
        obj.walk();
        obj.fly();
    }
}
