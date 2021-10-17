public class Booleans {
    public static void main(String[] args)
    {
        int count = 6;
        int total = 8;

        // Java will stop the program in this if-statement if only one statement is false
        if ((count != 0) && (total / count > 0)) {
            System.out.println("Ladies and gentlemen, we GOT EM");
        }

        int n = 0;
        int m = 0;
        int k = 0;

        // boolean b1 = (n <= 4) || ((m == 5 || k < 2) && (n < 12));
        //boolean b2 = !(n <= 4) || ((m == 5 || k < 2) && (n < 12));

        /* DeMorgan's Law:
        b2 = (!(n >= 4) && !((m == 5 || k < 2) && (n < 12)));
        b2 = (!(n >= 4) && (!(m == 5 || k < 2) || !(n < 12)));
        b2 = (!(n >= 4) && ((m != 5) && !(k >= 2) || !(n <= 12)));
        */

       //  boolean b2_c = (n < 4) && (m != 5) && (k >= 2) || (n < 12);
    }
}
