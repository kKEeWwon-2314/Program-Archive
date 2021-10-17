import java.awt.*;
import java.util.ArrayList;

public class Triangle 
{
    // A triange needs three points
    public class Point {
        int x;
        int y;

        public Point(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }

    Point left;
    Point right;
    Point top;

    // Public Constructor
    public Triangle() {}

    // Set up the triangle
    public void setTop(int x, int y)
    {
        top = new Point(x, y);
    }
    public void setLeft(int x, int y)
    {
        left = new Point(x, y);
    }
    public void setRight(int x, int y)
    {
        right = new Point(x, y);
    }

    public Point getMidpoint(Point p1, Point p2)
    {
        int midFX = (p1.x + p2.x) / 2;
        int midFY = (p1.y + p2.y) / 2;

        return new Point(midFX, midFY);
    }

    public Triangle(Point left, Point right, Point top)
    {
        this.top = top;
        this.left = left;
        this.right = right;
    }

    public void DrawTriangle(Graphics2D g)
    {
        Polygon p = new Polygon();

        p.addPoint(top.x, top.y);
        p.addPoint(left.x, left.y);
        p.addPoint(right.x, right.y);

        g.fill(p);
    }

    public ArrayList<Triangle> getSubTriangles()
    {
        ArrayList<Triangle> triangles = new ArrayList<>();

        Point midFBase = getMidpoint(left, right);
        Point midFRSide = getMidpoint(right, top);
        Point midFLSide = getMidpoint(left, top);

        Triangle t1 = new Triangle(left, midFBase, midFLSide);
        Triangle t2 = new Triangle(midFBase, right, midFRSide);
        Triangle t3 = new Triangle(midFLSide, midFRSide, top);

        triangles.add(t1);
        triangles.add(t2);
        triangles.add(t3);

        return triangles;
    }
    public static void main(String[] args)
    {

    }
}
