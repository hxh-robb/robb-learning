package _java.rmi.server;

import _java.rmi.API;
import _java.rmi.Listener;

import java.rmi.RemoteException;

public class Server implements API {

    private Listener listener;

    protected Server() throws RemoteException {
    }

    public void registerListener(Listener listener) {
        this.listener = listener;
    }

    public void registerListener(String abcd) {
        // this.listener = listener;
        System.out.println(abcd);
    }

    public void doSomething(String value) throws RemoteException {
        if( null != listener ) {
            listener.notify(value);
        }
    }
}
