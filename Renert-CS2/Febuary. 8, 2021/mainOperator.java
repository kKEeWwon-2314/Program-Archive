import org.junit.BeforeClass;

class mainOperator {
    public int add(int a, int b) {
        return a + b;
    } 

    public boolean isEven(int x) {
        boolean even = false;
        if (x % 2 == 0) {
            even = true;
        }

        return even; 
    }

    public double squareRoot(int y) throws Exception {
        double r = 0;
            if (y < 0) {
                throw new Exception("Cannot find result r where {r E R}");
            }

            r = Math.sqrt(y);
            System.out.println(r);

        return r;
    }
}