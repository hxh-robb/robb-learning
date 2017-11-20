import _java.JdkVersion;
import spring.core.ConfigLoader;

public class Main {
    public static void main(String[] args) {
        // Display current JDK version
        JdkVersion.output();

        // Load spring configuration
        ConfigLoader.load();

        // TODO:spring framework practice - IOC container
        // TODO:spring framework practice - AOP programming
    }
}
