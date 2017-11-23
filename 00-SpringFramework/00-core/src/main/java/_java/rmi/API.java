package _java.rmi;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface API extends Remote {
    void registerListener(Listener listener) throws RemoteException;
    void registerListener(String abcd) throws RemoteException;
}
