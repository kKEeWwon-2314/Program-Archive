import java.lang.Math;

public class Triangle extends Polygon {

    double side_length; // Assume equilateral triangle

    public Triangle() {
        num_sides = 3;
    }

    public Triangle(double s) {
        side_length = s;
        num_sides = 3;
    }

    @Override
    public double calculateArea() {
        // Calculate area of equilateral triangle:
        // side^2 * sqrt(3) / 4
        double a = (Math.pow(side_length, 2.0) * (Math.sqrt(3.0) / 4.0));
        return a;
    }

    @Override
    public double calculateCircumference() {
        double c = side_length * num_sides;
        return c;
    }
}
