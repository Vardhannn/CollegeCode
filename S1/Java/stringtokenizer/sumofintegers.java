package stringtokenizer;

import java.util.Scanner;
import java.util.StringTokenizer;

public class sumofintegers {
    String number;
    void tokenizer(){
        Scanner obj = new Scanner(System.in);
        number = obj.nextLine();
        int sum = 0;
        StringTokenizer st = new StringTokenizer(number," ");
        while(st.hasMoreTokens()){
            String singleint = st.nextToken();
            int n = Integer.parseInt(singleint);
            sum = sum + n;
        }
        System.out.println(sum);
    }
    public static void main(String[] args){
        sumofintegers si = new sumofintegers();
        si.tokenizer();
    }
}
