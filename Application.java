package com.example;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

import org.atsign.client.api.AtClient;
import org.atsign.common.AtSign;
import org.atsign.common.KeyBuilders;
import org.atsign.common.Keys.PublicKey;


public class Application extends JFrame {
    JLabel modeLabel; 
    JLabel input;
    JPanel formPanel;
    JPanel mainPanel; 
    int b = 0; 
    final private Font mainFont = new Font("Times New Roman", Font.BOLD, 25); 

    public void init() {

        modeLabel = new JLabel("Detecting Collisions...");
        modeLabel.setFont(mainFont); 
        JLabel layer = new JLabel("------------------------------"); 
        JLabel layer2 = new JLabel(""); 
        layer.setFont(mainFont); 

        input = new JLabel(""); 
        input.setFont(mainFont);

        formPanel = new JPanel(); 
        formPanel.setLayout(new GridLayout(4, 1, 5, 5));
        formPanel.setOpaque(false);
        formPanel.add(modeLabel);
        formPanel.add(layer);
        formPanel.add(layer2);
        formPanel.add(input);

        JButton obstacles = new JButton("Obstacle Detection"); 
        obstacles.setFont(mainFont);
        obstacles.setBackground(new Color(255, 255, 0));
        obstacles.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                modeLabel.setText("Obstacle Detection:");
                b = 1; 
            }
        }); 

        JButton crash = new JButton("Crash Detection"); 
        crash.setFont(mainFont);
        crash.setBackground(new Color(255, 0, 0));
        crash.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                modeLabel.setText("Crash Detection:");
                b = 2; 
            }
        }); 

        JPanel buttonsPannel = new JPanel(); 
        buttonsPannel.setLayout(new GridLayout(1, 2, 5, 5));
        buttonsPannel.add(obstacles);
        buttonsPannel.add(crash);

        mainPanel = new JPanel(); 
        mainPanel.setLayout(new BorderLayout());
        mainPanel.setBackground(new Color(117, 216, 230));
        mainPanel.add(formPanel, BorderLayout.NORTH); 
        mainPanel.add(buttonsPannel, BorderLayout.SOUTH); 

        add(mainPanel); 

        setTitle("Collison Detector"); 
        setSize(600, 300); 
        setMinimumSize(new Dimension(300, 200));
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) throws Exception {
        Application myFrame = new Application(); 
        myFrame.init(); 

        String ROOT_URL = "root.atsign.org:64";
        AtSign atSign = new AtSign("@initialcomputer");
        AtSign pico = new AtSign("@5495runningalone");
        AtClient atClient = AtClient.withRemoteSecondary(ROOT_URL, atSign);

        PublicKey pk = new KeyBuilders.PublicKeyBuilder(pico).key("crash").build(); // public:led@soccer0
        int x = 0; 
        int c = 0; 
        String previousValue = null;
        for (int i = 0; i < 50000; i++) {
            Thread.sleep(1000);
            
            String key = "crash";
            atClient.executeCommand("delete:cached:public:" + key + pico.toString(), false);

            String data = atClient.get(pk).get(); // data == 0, 1
                if (myFrame.b == 1 && data.equals("Obstacles Detected.")) {
                    myFrame.input.setText("Obstacle was detected for " + x++ + " seconds.");
                }
                if (myFrame.b == 2 && data.equals("Crash detected.") && !data.equals(previousValue)) {
                    previousValue = "Crash detected."; 
                    myFrame.input.setText("Crash detected " + ++c + " times.");
                }
                if (data.equals("No Obstacles Detected.")) {
                    myFrame.input.setText(data);
                    previousValue = ""; 
                    x = 0; 
                }
            
                //System.out.println("What was detected?\n " + data + '\n');
        }
    }
}
