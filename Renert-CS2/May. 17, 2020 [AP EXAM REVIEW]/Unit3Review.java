// Conditionals
public class Unit3Review {
    public static void main(String[] args) {
        // DeMorgan's Law
        boolean a = true;
        boolean b = true;

        boolean de1 = !(a && b);
        boolean de2 = !a || !b; // Turn and's into or's, and turn or's and and's.

        /**
         * Order of Operations in Java:
         * 
         * 1. Parentheses ()
         * 2. Yes or No Operators "!"
         * 3. Powers, Multiplication, Division, Modulus
         * 4. Addition, Subtraction
         * 5. Comparison Operators <, >, <=, >=
         * 6. Equality Operators =, ==, !=
         * 7. And &&
         * 8. Or ||
         * 9. Assignments *=, /=, +=, -=, %=
        **/

        // Variable Scopes
        if (de1 == de2) {
            int deletedInt = 5; // This integer will be deleted after the statement
        }
        // "deletedInt" is unaccessable because the variable scope is out of range
        // System.out.println(deletedInt);        

        // For loop termination and incrementation
        boolean end = false;
        for (int i = 0; (i < 10) && (end == false); i++) { // Repeats 10 times, increment (i++) is 1
            System.out.print(i);
            if (i == 5) { // Limiting our range, since (i < 10) is like a while loop
                end = true;
            }
        }

    }
}
