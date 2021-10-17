public class Unit10Review {
    // Recursive algorithms
    public static int factorial(int input) {
        // Base Case
        if (input == 1) {
            return 1;
        }

        // Recursive call
        return (input * factorial(input - 1));
    }
    public static void main(String[] args) {
        System.out.println(factorial(4));

        /**
         * Important recursive algorithms:
         * 
         * 1. Merge Sort
         * 2. Binary Search
         */
        
    }
}
