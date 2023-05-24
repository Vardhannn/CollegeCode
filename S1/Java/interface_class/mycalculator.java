package interface_class;

public class mycalculator implements AdvancedArithmetic{
    @Override
    public int divisor_sum(int n) {
        int sum = 0;
        if (n < 100) {
            for (int i = 1; i <= n; i++) {
                if (n % i == 0) {
                    sum = sum + i;
                }
            }

        } else {
            System.out.println("Enter a vaild input");
        }
        return sum;
    }
    public static void main(String[] args){
        mycalculator obj = new mycalculator();
        System.out.println(obj.divisor_sum(6));
    }
}
