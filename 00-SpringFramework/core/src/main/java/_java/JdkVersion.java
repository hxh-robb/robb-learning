package _java;

import java.util.logging.Logger;

/**
 * Display JDK Version
 */
public class JdkVersion {

    /**
     * output jdk version
     */
    public static final void output(){
        // System.out.println(System.getProperty("java.version"));
        String v = System.getProperty("java.version");
        Logger.getLogger(JdkVersion.class.getName()).info(v);
    }
}
