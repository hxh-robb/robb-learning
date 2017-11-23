package _java.rmi.server;

import _java.rmi.API;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.rmi.AlreadyBoundException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class ServerEntry {
    public static void main(String[] args) throws IOException, AlreadyBoundException {
        LocateRegistry.createRegistry(8787);
//        String hostname = InetAddress.getLocalHost().getHostAddress();
//        System.out.println(hostname);

        Server server = new Server();
        // Server stub = (Server) UnicastRemoteObject.exportObject(server, 0);
        API stub = (API) UnicastRemoteObject.exportObject(server, 0);
        // Remote stub = UnicastRemoteObject.exportObject(server, 0);
        Registry registry = LocateRegistry.getRegistry(8787);
        registry.bind("API",  stub);

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while( ! (input=reader.readLine()).equals("exit") ) {
            System.out.println("Copy:" + input);
            server.doSomething(input);
        }
        System.out.println("Bye:Bye");
    }
}
