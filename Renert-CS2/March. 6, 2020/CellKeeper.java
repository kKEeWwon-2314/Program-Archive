// Cell information variables
import java.util.ArrayList;
import java.util.Arrays;

public class CellKeeper {
    int number;
    int row_num;
    int col_num;
    public boolean solved;

    ArrayList<Integer> possibilities;
    int currentIndex;
    SudokuSolver game;
    MyGraphics graphics;

    public CellKeeper(int rowNumber, int columnNumber, int value, SudokuSolver game, MyGraphics g) {
        this.row_num = rowNumber;
        this.col_num = columnNumber;
        this.number = value;
        this.game = game;
        this.currentIndex = 0;
        this.graphics = g;

        if (value > 0) {
            solved = true;
        }
        else {
            solved = false;
        }

        // fill in possible cell values; if it is already solved, it will be set up as an empty list
        if (solved) {
            possibilities = new ArrayList<Integer>(Arrays.asList());
        }
        else {
            possibilities = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
            // find actuall possibilities
            findPossibilities();
        }
    }
    
    void findPossibilities() {
        // get value at any particular cell
        // get all numbers in any row, column, box

        Integer[] row = game.getRow(row_num);
        Integer[] col = game.getCol(col_num);
        Integer[] box = game.getBox(row_num, col_num);

        // create a list of values 1-9
        ArrayList<Integer> possibilities = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));

        // check row, col, box - if a value in any of those is in the list of possibilities, remove it
        for (Integer val : row) {
            if (possibilities.contains(val)) {
                possibilities.remove(val);
            }
        }

        // Check all values in the column
        for (Integer val : col) {
            if (possibilities.contains(val)) {
                possibilities.remove(val);
            }
        }

        // Check all values in the box
        for (Integer val : box) {
            if (possibilities.contains(val)) {
                possibilities.remove(val);
            }
        }
    }

    void setNumber() {
        number = possibilities.get(currentIndex);
        game.puzzle[row_num][col_num] = number;

        // call graphics in
        graphics.updateBoard();
    }

    void findValue () {
        // valid or not?
        setNumber();

        // valid then increment
        while (!isValid() && currentIndex < (possibilities.size() - 1)) {
            currentIndex++;
            setNumber();
        }

    }

    boolean checkArea(Integer[] area) {
        // checks, a row, column or box, then returns true if the value is valid\
        for (int i = 0; i < area.length; i++) {
            if (area[i] > 0) {
                int value = area[i];
                for (int j = i+ 1; i < area.length; j++) {
                    if (value == area[j]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    boolean isValid() {
        // checks if valid
        if (!checkArea(game.getRow(this.row_num))) {
            return false;
        }
        if (!checkArea(game.getCol(this.row_num))) {
            return false;
        }
        if (!checkArea(game.getBox(this.row_num, this.col_num))) {
            return false;
        }
        return true;
    }
}
