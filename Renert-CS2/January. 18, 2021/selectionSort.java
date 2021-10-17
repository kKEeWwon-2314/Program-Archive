public class selectionSort {
     public static int[] selection_sort(int[] my_list) {

        // track the beginning of the unsorted portion
        int unsorted_index = 0;

        // repeat until the unsorted portion of the array is the last element of the array
        while (unsorted_index < my_list.length - 1) { 

            int smallest_index = unsorted_index;
            int smallest_value = my_list[unsorted_index];

            // run through the unsorted portion of the array and find the smallest number
            for (int i = unsorted_index; i < my_list.length; i++) {
                if (my_list[i] < smallest_value) {
                    smallest_value = my_list[i];
                    smallest_index = i;
                }
            }

            // swap the smallest number with the number at the beginning of the unsorted sub-array
            my_list[smallest_index] = my_list[unsorted_index];
            my_list[unsorted_index] = smallest_value;

            unsorted_index++;
        }
        return my_list;
    }
    
    public static void main(String[] args) {
        int[] my_list = { 38, 43, 3, 82, 10 };

        /*
        int[] sorted_list = bubble_sort(my_list);
        int[] sorted_list = insertion_sort(my_list);
        */
        int[] sorted_list = selection_sort(my_list);
        System.out.println(Arrays.toString(sorted_list));
    }
}