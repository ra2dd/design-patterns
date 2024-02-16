package patterns;

public class Main {
    public static void main(String[] args) {
        SimpleSingleton s1 = SimpleSingleton.getInstance("First");
        SimpleSingleton s2 = SimpleSingleton.getInstance("Second");

        System.out.println("s1 value: " + s1.value);
        System.out.println("s2 value: " + s2.value);
    }
}
