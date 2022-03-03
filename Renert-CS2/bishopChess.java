import java.util.Arrays;
import java.util.Scanner;

public class bishopChess {
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);

        int numCases = sc.nextInt();

        for (int i = 0; i < numCases; i++) {
            String _startingX = sc.next();
            int startingY = sc.nextInt();

            String _endingX = sc.next();
            int endingY = sc.nextInt();

            // convert column from string to int
            int startingX = _startingX.charAt(0);
            startingX -= 64;
            
            int endingX = _endingX.charAt(0);
            endingX -= 64;

            // check move validity
            int tileStart  = startingX + startingY;
            tileStart = tileStart % 2;

            int tileEnd  = startingX + startingY;
            tileEnd = tileEnd % 2;

            int xcoordiff = Math.abs(startingX - endingX);
            int ycoordiff = Math.abs(startingY - endingY);

            // check color of tile
            if (tileStart != tileEnd) {
                System.out.print("Impossible");
            }

            // possible in 0 moves      
            else if ((startingX == endingX) && (startingY == endingY)) {
                System.out.println("0 " + _startingX + " " + startingY);
            }

            // possible in 1 move
            else if (xcoordiff == ycoordiff) {
                System.out.print("1 " + _startingX + " " + startingY + _endingX);
            }

            // possible in 2 moves
            else {
                int x0 = startingX;
                int x1 = endingX;
                int y0 = startingY;
                int y1 = endingY;

                // find midpoint
                double midx = 0.5 * (x0 + x1 - y0 + y1);
                double midy = 0.5 * (x1 - x0 + y0 + y1);

                // another case
                if (!(midx > 0) && (midx < 9) && (midy > 0) && (midy < 9)) {
                    midx = 0.5 * (x0 + x1 + y0 - y1);
                    midy = 0.5 * (x0 - x1 + y0 + y1);
                }

                char x  = (char)(((int)midx) + 64);

                String start = _startingX + " " + startingY;
                String midPoint = x + " " + (int)midy;
                String end = endingX + " " + endingY;
            }
        }
        sc.close();
    }
}