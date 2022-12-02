package com.example;

import org.atsign.client.api.AtClient;
import org.atsign.common.AtSign;
import org.atsign.common.KeyBuilders;
import org.atsign.common.Keys.PublicKey;

public class App {
    public static void main(String[] args)
            throws Exception {
        String ROOT_URL = "root.atsign.org:64";
        AtSign atSign = new AtSign("@initialcomputer");
        AtSign pico = new AtSign("@5495runningalone");

        AtClient atClient = AtClient.withRemoteSecondary(ROOT_URL, atSign);

        PublicKey pk = new KeyBuilders.PublicKeyBuilder(pico).key("led").build(); // public:led@soccer0

        String previousValue = null;
        for (int i = 0; i < 50000; i++) {
            Thread.sleep(500);

            String key = "led";
            atClient.executeCommand("delete:cached:public:" + key + pico.toString(), false);

            String data = atClient.get(pk).get(); // data == 0, 1
            if (previousValue == null || !data.equals(previousValue)) {
                System.out.println("We got a new value! Value: " + data);
                previousValue = data;
            }
        }

    }
}