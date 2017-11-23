package _java.rmi.client;

import _java.rmi.API;
import _java.rmi.Listener;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.rmi.NotBoundException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class ClientEntry {
    public static void main(String[] args) throws IOException, NotBoundException {
        Registry registry = LocateRegistry.getRegistry(8787);

        Listener listener = new ListenerImpl();
        API api = (API) registry.lookup("API");

        /* Option 1:Listener will run remotely */
//        api.registerListener(listener);

        /* Option 2:Listener will run locally */
        Listener stub = (Listener) UnicastRemoteObject.exportObject(listener,0);
        registry.rebind("Callback", stub);
        api.registerListener(stub);

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while( ! (input=reader.readLine()).equals("exit") ) {
            System.out.println("Copy:" + input);
        }
        System.out.println("Bye:Bye");
    }
}
