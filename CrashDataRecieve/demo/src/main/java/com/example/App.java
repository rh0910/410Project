// Ronaldo Herrera
package com.example;

import org.atsign.client.api.AtClient;
import org.atsign.common.AtSign;
import org.atsign.common.KeyBuilders;
import org.atsign.common.Keys.PublicKey;

public class App {
    public static void main(String[] args)
            throws Exception {
        // A lot of the code here was provided by atSign with some small changes.
        String ROOT_URL = "root.atsign.org:64";
        AtSign atSign = new AtSign("@initialcomputer"); // One of my atKeys
        AtSign pico = new AtSign("@5495runningalone"); // Another atKey which is the key that is on the pico which sends data to the atkey above it

        AtClient atClient = AtClient.withRemoteSecondary(ROOT_URL, atSign);
        // code provided by atSign
        PublicKey pk = new KeyBuilders.PublicKeyBuilder(pico).key("crash").build(); // public:crash@5495runningalone
        // 
        String previousValue = null;
        for (int i = 0; i < 50000; i++) {
            Thread.sleep(500);// used to delay the for loop execution so it does not execute right away.

            String key = "crash"; // the key to connect to our pico
            atClient.executeCommand("delete:cached:public:" + key + pico.toString(), false); // the tutorial told us not worry about what this does. but it is needed so the code works

            String data = atClient.get(pk).get(); // data == values sent from the pico
            if (previousValue == null || !data.equals(previousValue)) {
                System.out.println("What was detected?\n " + data + '\n'); // displays what was detected in terminal. This for loop code was transferred to the GUI code.
                previousValue = data;
            }
        }

    }
}
