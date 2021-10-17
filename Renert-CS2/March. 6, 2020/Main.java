// import java.util.ArrayList;

public class Main {

    static Integer[][] puzzle = {{8, 7, 4, 0, 0, 0, 5, 9, 0},
    {0, 6, 9, 0, 0, 0, 0, 0, 8},
    {0, 1, 0, 9, 2, 0, 7, 0, 4},

    {0, 0, 0, 4, 6, 0, 0, 0, 5},
    {5, 4, 0, 0, 0, 0, 0, 3, 6},
    {6, 0, 0, 0, 5, 9, 0, 0, 0},

    {7, 0, 2, 0, 8, 1, 0, 4, 0},
    {4, 0, 0, 0, 0, 0, 2, 5, 0},
    {0, 5, 6, 0, 0, 0, 1, 8, 3}};

    public static void main(String[] args) {
        SudokuSolver s = new SudokuSolver(puzzle);
        s.findSolution();

/*
        // print the sudoku puzzle nicely
        ArrayList<ArrayList<Integer>> solution = new ArrayList<ArrayList<Integer>>();

        for (Integer[] row : sol) {
            ArrayList<Integer> r = new ArrayList<Integer>();
            for (Integer cell: row) {
                r.add(cell);
            }
            solution.add(r);
        }

        for (ArrayList<Integer> row : solution) {
            System.out.println(row);
        }
*/
    }
}