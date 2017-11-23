package _java.rmi.client;

import _java.rmi.Listener;

public class ListenerImpl implements Listener {
    public void notify(String newValue) {
        System.out.println("Received:" + newValue);
    }
}
