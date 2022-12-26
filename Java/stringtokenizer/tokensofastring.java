package stringtokenizer;

import java.util.Scanner;
import java.util.StringTokenizer;

public class tokensofastring {
    String str;
    void token(){
        Scanner sc = new Scanner(System.in);
        str = sc.nextLine();
        StringTokenizer st = new StringTokenizer(str,"#@$%&");
        while (st.hasMoreTokens()){
            System.out.println(st.nextToken());
        }
    }
    public static void main(String[] args){
        tokensofastring obj = new tokensofastring();
        obj.token();
    }
}
