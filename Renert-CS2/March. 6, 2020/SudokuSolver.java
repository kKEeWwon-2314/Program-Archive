import java.util.ArrayList;
import java.util.Arrays;

public class SudokuSolver{

    Integer[][] puzzle;
    CellKeeper[] solvePuzzle;
    MyGraphics graphics;
    int backtrackCoords = 0;

    public SudokuSolver(Integer[][] puzzle) {
        this.puzzle = puzzle;
        this.solvePuzzle = new CellKeeper[81];

        initializeBoard();
    }

    public void initializeBoard() {
        int count = 0;

        for (int i = 0; i < 9; i++) {
            Integer[] row = puzzle[i];
            for (int j = 0; j < 9; j++) {
                Integer value = row[j];
                solvePuzzle[count] = new CellKeeper(i, j, value, this, graphics);
                count++;
            }
        }
    }

    ArrayList<Integer> findPossibilities(int row_num, int col_num) {
        // get value at any particular cell
        // get all numbers in any row, column, box

        Integer[] row = getRow(row_num);
        Integer[] col = getCol(col_num);
        Integer[] box = getBox(row_num, col_num);

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

        // return remaining list
        return possibilities;
    }

    Integer[] getRow(int row_num) {
        return puzzle[row_num];
    }

    Integer[] getCol(int col_num) {
        Integer[] col = new Integer[9];
        for (int i = 0; i < 9; i++) {
            col[i] = puzzle[i][col_num];
        }
        return col;
    }

    Integer[] getBox(int row_num, int col_num) {
        Integer[] box = new Integer[9];

        // use integer division to find the top-left corner of the box the cell is inside
        
        // find top-left cell in the current cell's box
        int box_row = (row_num / 3) * 3;
        int box_col = (col_num / 3) * 3;

        int index = 0;
        for (int i = box_row; i < (box_row + 3); i++) {
            for (int j = box_col; j < (box_col + 3); j++) {
                box[index] = puzzle[i][j];
                index++;
            }
        }

        return box;
    }

    // Check if the specified value can be placed at this coordinate
    boolean isValid(int row_num, int col_num, int value) {

        boolean valid = true;

        Integer[] r = getRow(row_num);
        Integer[] c = getCol(col_num);
        Integer[] b = getBox(row_num, col_num);

        ArrayList<Integer> row = new ArrayList<Integer>(Arrays.asList(r));
        ArrayList<Integer> col = new ArrayList<Integer>(Arrays.asList(c));
        ArrayList<Integer> box = new ArrayList<Integer>(Arrays.asList(b));
        
        if (row.contains(value) || col.contains(value) || (box.contains(value))) {
            valid = false;
        }
        return valid;
    }

    void checkRow(int row_num) {
        // Checks if there is exactly one cell in the row that can contain a certain value - if so, fill that cell 

        // iterate through values 1-9, count the number of cells where that value is a valid placement
        ArrayList<Integer> row = new ArrayList<Integer>(Arrays.asList(getRow(row_num)));

        // Iterating through each possible value 
        for (int val = 1; val <= 9; val++) {
            if (!row.contains(val)) {
                int valid_count = 0;
                int valid_cell;

                // Iterate through each cell in the row to check for a valid placement
                for (int j = 0; j < 9; j++) {
                    if (puzzle[row_num][j] == 0) {
                        if (isValid(row_num, j, val)) {
                            valid_count++;
                            valid_cell = j;
                        }
                    }
                }
            }
        }
    }
    void decrementCell(CellKeeper cell) {
        // go back to the lastest filled in cell
        while (cell.currentIndex == cell.possibilities.size() - 1) {
            cell.number = 0;
        cell.currentIndex = 0;
        puzzle[cell.row_num][cell.col_num] = 0;
        
        // continue to backtrack until we reach a fresh cell
        backtrackCoords--;
            while (solvePuzzle[backtrackCoords].solved) {
                backtrackCoords--;
            }
        cell = solvePuzzle[backtrackCoords];
        }
        cell.currentIndex++;
    }

    public void findSolution() {
        // BACKTRACKING ALGORITHM
        while (backtrackCoords < solvePuzzle.length) {
            // find next empty cell and put the next possible value; repeat
            while (solvePuzzle[backtrackCoords].solved) {
                backtrackCoords++;
            }
            if ((backtrackCoords < solvePuzzle.length) && (solvePuzzle[backtrackCoords].solved)) {
                break;  
            }
        }
        
        // put first possible value
        CellKeeper cell = solvePuzzle[backtrackCoords];
        // cell.setNumber();
        cell.findValue();

        // continue or backtrack
        if (cell.isValid()) {
            // continue

        }
        else {
            // if not possible valid solution, then backtrack
            decrementCell(cell);
        }
        // continue with algorithm

    }

/*
    Integer[][] findSolution() {

        
        //Solve the puzzle

        // logic rules:
        // has to be a different integer (1-9) in each row, column, and 3x3 box

        // check a row - if there's only one empty box, find the missing value and fill that in 
        // same for columns and 3x3 boxes

        -----
        iterate through every cell
        
        int num_changes = -1;

        while (num_changes != 0) {
            num_changes = 0;

            for (int row = 0; row < 9; row++) {
                for (int col = 0; col < 9; col++) {
                    if (puzzle[row][col] == 0) {
                        ArrayList<Integer> possibilities = findPossibilities(row, col);
                        // Check if there is only one possibility - if so, we can just fill that cell
                        if (possibilities.size() == 1) {
                            puzzle[row][col] = possibilities.get(0);
                            num_changes++;
                        }
                    }
                }
            }
        }


        // if in any row, column or box, there is only one cell that can possibly contain a certain value, place that value there
        // once we place a value in a cell, update the possible values of the surrounding affected cells 

        //return puzzle;
    }
*/
}
