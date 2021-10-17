public class Unit8Review {
    public static void main(String[] args) {
        // 2D Arrays
        int[][] __dArray = {{1, 2, 3}, 
                            {-3, -5, -8}, 
                            {0, 1, 34}};

        for (int col = 0; col < __dArray.length; col++) {
            for (int row = 0; row < __dArray[col].length; row++) {
                System.out.println(__dArray[col][row] + " ");
            }
            System.out.println();
        }

        System.out.println();
        System.out.println();

        for (int row = 0; row < __dArray.length; row++) {
            for (int col = 0; col < __dArray[row].length; col++) {
                System.out.println(__dArray[row][col] + " ");
            }
            System.out.println();
        }
    }
}