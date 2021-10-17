public class Rectangle extends Polygon {
    
    double length;
    double width;

    public Rectangle() {
        num_sides = 4;
    }

    public Rectangle(double l, double w) {
        length = l;
        width = w;
        num_sides = 4;
    }

    @Override
    public double calculateArea() {
        double a = length * width;
        return a;
    }

    @Override
    public double calculateCircumference() {
        double c = (length * 2.0) + (width * 2.0);
        return c;
    }
}
