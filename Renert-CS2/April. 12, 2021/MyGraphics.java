import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

public class MyGraphics extends JPanel implements MouseListener {

    /**
     *  Graphics program for our dangerous experiments with graphics.
     * 
     *  Date Created: 4/12/2021 [Monday]
     *  Author: Renert CS2
     */
    private static final long serialVersionUID = 1L;

    /**
     * For our program, the depth can only go up to 9 until the triangle will become very unclear.
     * For 600 x 600, the depth can only go up to 6
     * For 700 x 700, the depth can only go up to 7
     * 
     * And so on...
     */
    static int WIDTH = 850;
    static int HEIGHT = 850;

    public static void main(String[] args) {
        JFrame frame = new JFrame("CS2 Graphics Experiment [1]");

        MyGraphics graphics = new MyGraphics();
        frame.add(graphics);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(0, 0, WIDTH + 15, HEIGHT + 40);
        frame.setVisible(true);
    }

    public MyGraphics() {
        addMouseListener(this);
    }

    public void drawTriforceange(Graphics2D g, Triangle t, int Depth)
    {
        // Base case for our recursion; Our limit is exceeded then break
        if (Depth == 0) {
            g.setColor(Color.BLACK);
            t.DrawTriangle(g);
        }
        // Otherwise, initiate our recursive call
        else {
            ArrayList<Triangle> triangles = t.getSubTriangles();

            drawTriforceange(g, triangles.get(0), Depth - 1);
            drawTriforceange(g, triangles.get(1), Depth - 1);
            drawTriforceange(g, triangles.get(2), Depth - 1);
        }
    }

    public void paint(Graphics g) {
        // Code to draw things in the window goes here
        Graphics2D g2 = (Graphics2D) g; // Convert to a Graphics2D object, because Graphics2D has improved functionality
        Triangle t = new Triangle();

        t.setTop((WIDTH / 2), 0);
        t.setLeft(0, HEIGHT);
        t.setRight(WIDTH, HEIGHT);

        g2.setColor(Color.BLACK);
        drawTriforceange(g2, t, 5);
    }

    @Override
    public void mouseClicked(MouseEvent e) {}
    
    @Override
    public void mousePressed(MouseEvent e) {}

    @Override
    public void mouseReleased(MouseEvent e) {}
    
    @Override
    public void mouseEntered(MouseEvent e) {}
    
    @Override
    public void mouseExited(MouseEvent e) {}
}