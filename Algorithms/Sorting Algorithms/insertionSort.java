public class insertionSort {
    public static int[] insertion_sort(int[] my_list) {
           for (int i = 1; i < my_list.length; i++) {
                // compare the element to the elements in the sorted portion of the array with indicides < i
                int index = i; // index of element we are swapping

                for (int j = i - 1; j >= 0; j--) {
                    if (my_list[j] > my_list[index]) {
                        // swap elements
                        int temp = my_list[j];
                        my_list[j] = my_list[index];
                        my_list[index] = temp;

                        index--;
                    }
                    else { // we have reached the correct point in the sorted section of the array
                        break;
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
        int[] sorted_list = insertion_sort(my_list);
        System.out.println(Arrays.toString(sorted_list));
    }
}