import javax.swing.*;
import java.awt.*;

public class GUI {
    // Constructor param
    public GUI(){
        JFrame frame = new JFrame();

        JButton button = new JButton("Check for report");

        JLabel label = new JLabel("Status:");

        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(100,100,50,100));
        panel.setLayout(new GridLayout(0 ,1));
        panel.add(button);

        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Crash Report");
        frame.pack();
        frame.setVisible(true);
    }
    public static void main(String[] args){
        new GUI();
    }
}
