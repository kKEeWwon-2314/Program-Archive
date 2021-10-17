import java.util.Arrays;

public class mergeSort {
    public static void main(String[] args) {
        int[] unsorted = { 38, 27, 43, 3, 9, 82, 10 };
        int[] sorted = mergeSort(unsorted);

        System.out.println(Arrays.toString(sorted));

        int i = binarySearch(sorted, 0, sorted.length - 1, 52);
        System.out.println(i);
    }

    // returns the index where the element is located
    /* 
        NOTE: l and r describe the left and right bounds of the array we're currently considering
    */
    public static int binarySearch(int[] list, int l, int r, int elem) {
        int index = -1;
        
        // examine the array only with one element
        if (r < l) {
            // our element is not in the list
            return -1;
        }
        // find the midpoint of the array with the Midpoint Formula: int mid = (list.length - 1) / 2;

        int mid = l + (r - l) / 2;

        if (list[mid] == elem) {
            return mid;
        }
        // determine if the element we're searching for is on the left or right of the middle element
        if (list[mid] < elem) {
            // if the element is on the right side of the array, recursively search the right side
            index = binarySearch(list, mid + 1, r, elem);
            return index;
        }
        if (list[mid] > elem) {
            // element is in the left-hand side of the array
            index = binarySearch(list, l, mid - 1, elem);
            return index;
        }
        return index;
    }

    public static int[] mergeSort(int[] list) {
        /*
            System.out.println("Unsorted:");
            System.out.println(Arrays.toString(list));
        */
        
        // check for the base case of our recursive calls
        if (list.length == 1) {
            return list;
        }

        // split array into left and right, which will become our sub-arrays

        int middle = (list.length / 2) - 1;

        // create the left and right sub-arrays
        int left = middle + 1;
        int right = list.length - left;

        int[] L = new int[left];
        int[] R = new int[right];

        // copy the correct subsection of the original array into the sub-array
        for (int i = 0; i < left; i++) {
            L[i] = list[i];
        }
        for (int i = 0; i < right; i++) {
            R[i] = list[middle + 1 + i];
        }

        // further split the sub-arrays
        L = mergeSort(L);
        R = mergeSort(R);

        // merge sorted sub-arrays back together
        int left_index = 0;
        int right_index = 0;
        
        int i = 0;

        // sort the sub-arrays until the end of the array
        while ((left_index < L.length) && (right_index < R.length)) {
            int l_val = L[left_index];
            int r_val = R[right_index];

            if (l_val < r_val) {
                list[i] = l_val;
                left_index++;
            }
            else {
                list[i] = r_val;
                right_index++;
            }
            i++;
        }

        // add any remaining elements from the sub-arrays

        // NOTE: only one of these two while loops will ever run
        while (left_index < L.length) {
            list[i] = L[left_index];
            left_index++;
            i++;
        }

        while (right_index < R.length) {
            list[i] = R[right_index];
            right_index++;
            i++;
        }

        return list;
    }
}