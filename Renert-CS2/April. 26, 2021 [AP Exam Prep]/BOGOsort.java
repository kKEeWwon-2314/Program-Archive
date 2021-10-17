import java.util.*;

public class BOGOsort {

    public static boolean isSorted(int[] list) {
        int previous = -1;
        for (int element : list) {
            if (element < previous) {
                return false;
            }
            previous = element;
        }
        return true;
    }

    public static void Shuffle(int[] values) {
        for (int i = values.length - 1; i >= 1; i--) {
            int index = (int)(Math.random() * values.length);
            int swap = values[i];

            values[i] = values[index];
            values[index] = swap;
        }
    }

    public static int[] createNewList(int length) {
        int[] myList = new int[length];

        for (int i = 0; i < length; i++) {
            // generate random
            int number = (int)(Math.random() * 100);
            myList[i] = number;
        }

        return myList;
    }
    public static void main(String[] args) {
        int[] list1 = createNewList(10);
        double start = System.currentTimeMillis();

        System.out.println("Before: ");
        System.out.println(Arrays.toString(list1));

        int shuffleCount = 0;

        while(!isSorted(list1)) {
            Shuffle(list1);
            shuffleCount++;
        }

        double end = System.currentTimeMillis();

        System.out.println("After: ");
        System.out.println(Arrays.toString(list1));

        System.out.println("Number of times shuffled " + shuffleCount + " times");

        double total = (end - start) / 1000;
        System.out.print("Time took to sort: " + total + " seconds");
    }
}
