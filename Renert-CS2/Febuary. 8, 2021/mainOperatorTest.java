import static org.junit.Assert.*;

// import org.junit.After;
import org.junit.AfterClass;
// import org.junit.Before;    
import org.junit.BeforeClass;
import org.junit.Test;
public class mainOperatorTest {
    static mainOperator c1;

    @BeforeClass
    public static void setup() {
        mainOperator c1 = new mainOperator();
    }

    @Test
    public void firstTest() {
        int a1 = c1.add(7, 6);

        assertEquals(13, a1);
    }

    @Test
    public void secondTest() {
        assertTrue(c1.isEven(4));
        assertTrue(c1.isEven(11));
    }

    @Test
    public void thirdTest() {
        mainOperator c1 = new mainOperator();

        
    }

    @AfterClass
    public static void setup2() {
        System.out.println("Finished test");
    }
}