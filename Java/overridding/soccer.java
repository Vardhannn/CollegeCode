package overridding;

public class soccer extends sports{


    void getname(String sportsname){
        System.out.println("this is soccer : "+sportsname);
    }
    void getnumberofteammembers(int numplayers){
        System.out.println("this is number of playeres : "+numplayers);
    }
    public static void main(String[] args){
        soccer obj = new soccer();
        obj.getname("virat kohil");
        obj.getnumberofteammembers(12);
    }
}
