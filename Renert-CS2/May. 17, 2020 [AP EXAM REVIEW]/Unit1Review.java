public class Unit1Review {
    public static void main(String[] args) {
        // Declaring a variable
        int n;
        // Initializing a variable
        n = 5;
        System.out.println(n);

        // Declaring and initializing at the same time
        int x = 1;
        double b = 2.4;
        double answer = x + b;
        System.out.println(answer);

        // Constant variables
        final int TEMP_NUM;
        TEMP_NUM = 10; // This variable is now a fixed value and cannot be changed

        // NOTE: Cannot name variables names that are keywords (public, int, etc.) in Java

        // Printing variables
        System.out.print("SUPYO"); // Print does not add a new character to the end of the line
        System.out.println("DUDE"); // Println does, hence println => "print line"

        // Compound variable operators
        int tempScore = 90;
        tempScore += 10;
        tempScore -= 10;
        tempScore *= 10;
        tempScore /= 10;
        tempScore %= 10;
        System.out.println(tempScore);

        // Math with multiple variables
        int numerator = 10;
        int denominator = 12;
        double result = (double) numerator / denominator;

        int roundedResult = (int)(result + 0.5);
        System.out.println(roundedResult);
    }
}
