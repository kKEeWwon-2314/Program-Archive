abstract class Polygon {
    
    int num_sides;

    public abstract double calculateArea();
    public abstract double calculateCircumference();

    public void printNumSides() {
        System.out.println("This polygon has " + num_sides + " sides.");
    }
}
