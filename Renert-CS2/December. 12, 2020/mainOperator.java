public class mainOperator {
    public static void main(String[] args) {
        //Polygon p = new Polygon(); // Can't create objects from abstract classes

        Triangle t = new Triangle(2.0);
        Rectangle r = new Rectangle(4.0, 5.0);

        //System.out.println(t.num_sides);

        System.out.println(t.calculateArea());
        System.out.println(r.calculateCircumference());
        t.printNumSides();
    }
}