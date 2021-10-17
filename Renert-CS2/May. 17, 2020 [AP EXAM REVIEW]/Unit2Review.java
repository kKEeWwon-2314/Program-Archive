// Objects and Classes
public class Unit2Review {
    public static void main(String[] args) {
        // A string is an object.
        String newString = "String is the class, and newString is the object.";

        // Non-static method
        newString.contains("s");

        // The math class is used very often
        Math.sqrt(16.0);

        // Primitives
        int newPrimitiveInt = 4;
        Integer newInt = new Integer(4); // This is the way an integer is created before
        Integer tempInt = Integer.valueOf(newPrimitiveInt); // You can do it more correctly this way
        System.out.println(tempInt);

        newInt += 5;
        newPrimitiveInt = newInt.intValue();

        // Comparing Objects (not primitives)
        int a = 5;
        int b = 5;
        if (a == b) {
            System.out.println("Equal");
        }
        else {
            System.out.println("Not Equal");
        }

        String newString2 = "String is the class, and newString is the object";
        newString2 += ".";
        if (newString == newString2) {
            System.out.println("Equal");
        }
        else {
            System.out.println("Not Equal");
        }
    }
}
