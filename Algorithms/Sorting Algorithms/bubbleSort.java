import java.util.Arrays;

public class bubbleSort {
    public static int[] bubble_sort(int[] my_list) {

        boolean has_swap = true; // this boolean tracks swaps

        while (has_swap) {

            has_swap = false;
            // scan through the array
            for (int i = 0; i < my_list.length - 1; i++) {
                // compare the elements
                int e1 = my_list[i];
                int e2 = my_list[i + 1];

                if (e1 > e2) { // swap elements
                    my_list[i] = e2;
                    my_list[i + 1] = e1;
                    has_swap = true;
                }
            }
        }
        return my_list;
    }
    
    public static void main(String[] args) {
        int[] my_list = { 38, 43, 3, 82, 10 };

        /*
        int[] sorted_list = bubble_sort(my_list);
        int[] sorted_list = insertion_sort(my_list);
        */
        int[] sorted_list = bubble_sort(my_list);
        System.out.println(Arrays.toString(sorted_list));
    }