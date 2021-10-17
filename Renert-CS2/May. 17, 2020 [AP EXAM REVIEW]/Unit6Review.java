import java.util.ArrayList;

public class Unit6Review {
    public static void main(String[] args) {
        // Arraylist declaring
        ArrayList<String> newArrayList;
        // Initialize and Arraylist
        newArrayList = new ArrayList<>();

        // Add strings to the Arraylist
        newArrayList.add("Hello");
        newArrayList.add("Shrek");

        // Adding other objects to an Arraylist
        newArrayList.get(0);
        newArrayList.set(1, "World");

        System.out.println(newArrayList);

        // Reference variables in Arraylists: ArrayList<String, Integer, Boolean, etc.> someArrayList;
        int a = 5;
        ArrayList<Integer> intArrayList = new ArrayList<>();

        intArrayList.add(a);
        System.out.println(intArrayList);
    }
}
