package calc;

import javax.swing.*;
import java.awt.*;

public class calculator {

    JFrame frame;
    JPanel panel;
    JTextField textfiled;
    JButton[] buttons;
    Font font = new Font("SF PRO DISPLAY", Font.BOLD,20);
    calculator(){

        frame = new JFrame("PROTOTYPE");
        textfiled = new JTextField();

        panel = new JPanel();
        panel.setBounds(10,80,400,400);
        panel.setBackground(Color.GRAY);

        textfiled.setBounds(10,30,400,40);
        textfiled.setFont(font);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(450,550);

        buttons = new JButton[2];
        buttons[0] = new JButton("1");
        buttons[0].setSize(50,50);



//        for(int i = 0;i<10;i++){
//            panel.add(new JButton(String.valueOf(i)));
//        }







//        b = new JButton("1");
//        b.setBounds(10,90,50,50);
//
//        b1 = new JButton("2");
//        b1.setBounds(70,90,50,50);
//
//        b2 = new JButton("3");
//        b2.setFont(font);
//        b2.setBounds(130,90,50,50);







        frame.add(textfiled);
        panel.add(buttons[0]);
        panel.setLayout(null);
        frame.add(panel);
        frame.setLayout(null);

//        panel.setLayout(new GridLayout(3,3));
        frame.setVisible(true);

    }
    public static void main(String args[]){
        new calculator();
    }

}
