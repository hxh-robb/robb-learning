package _java.rmi;

import java.io.Serializable;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Listener extends Remote,Serializable {
    void notify(String newValue) throws RemoteException;
}
