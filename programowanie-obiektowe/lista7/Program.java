// Dawid Pawliczek, 347081, lista 7

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class Shape {
    protected String color;
    protected boolean filled;

    public Shape(String color, boolean filled) {
        this.color = color;
        this.filled = filled;
    }

    @Override
    public String toString() {
        return "Shape{" +
                "color='" + color + '\'' +
                ", filled=" + filled +
                '}';
    }
}

class Circle extends Shape {
    protected double radius;
    protected double area = Math.PI * radius * radius;

    public Circle(String color, boolean filled, double radius) {
        super(color, filled);
        this.radius = radius;
    }

    @Override
    public String toString() {
        return super.toString() + ", radius=" + radius + '}';
    }
}

class Triangle extends Shape {
    protected double base;
    protected double height;
    protected double area = base * height / 2;

    public Triangle(String color, boolean filled, double base, double height) {
        super(color, filled);
        this.base = base;
        this.height = height;
    }

    @Override
    public String toString() {
        return super.toString() + ", base=" + base + ", height=" + height + '}';
    }
}

class ShapePanel extends JPanel {
    protected Shape shape;
    protected JTextField colorField;
    protected JCheckBox filledCheckBox;

    public ShapePanel(Shape shape) {
        this.shape = shape;
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        colorField = new JTextField(shape.color);
        filledCheckBox = new JCheckBox("Filled", shape.filled);

        colorField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                shape.color = colorField.getText();
            }
        });

        filledCheckBox.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                shape.filled = filledCheckBox.isSelected();
            }
        });

        add(new JLabel("Color:"));
        add(colorField);
        add(filledCheckBox);
    }

    public void setColor(String color) {
        colorField.setText(color);
        shape.color = color;
    }

    public void setFilled(boolean filled) {
        filledCheckBox.setSelected(filled);
        shape.filled = filled;
    }
}

class CirclePanel extends ShapePanel {
    private JTextField radiusField;

    public CirclePanel(Circle circle) {
        super(circle);

        radiusField = new JTextField(String.valueOf(circle.radius));
        radiusField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double radius = Double.parseDouble(radiusField.getText());
                    circle.radius = radius;
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(CirclePanel.this,
                            "Invalid format for radius.", "Input Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        add(new JLabel("Radius:"));
        add(radiusField);
    }
}

class TrianglePanel extends ShapePanel {
    private JTextField baseField;
    private JTextField heightField;

    public TrianglePanel(Triangle triangle) {
        super(triangle);

        baseField = new JTextField(String.valueOf(triangle.base));
        baseField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double base = Double.parseDouble(baseField.getText());
                    triangle.base = base;
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(TrianglePanel.this,
                            "Invalid format for base.", "Input Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        add(new JLabel("Base:"));
        add(baseField);

        heightField = new JTextField(String.valueOf(triangle.height));
        heightField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double height = Double.parseDouble(heightField.getText());
                    triangle.height = height;
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(TrianglePanel.this,
                            "Invalid format for height.", "Input Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        add(new JLabel("Height:"));
        add(heightField);
    }
}

class ShapesFrame extends JFrame {

    public ShapesFrame() {
        super("Shapes Editor");

        Circle circle = new Circle("red", true, 1.0);
        Triangle triangle = new Triangle("blue", false, 1.0, 1.0);

        CirclePanel circlePanel = new CirclePanel(circle);
        TrianglePanel trianglePanel = new TrianglePanel(triangle);                

        JTabbedPane tabbedPane = new JTabbedPane();
        tabbedPane.addTab("Circle", circlePanel);
        tabbedPane.addTab("Triangle", trianglePanel);        

        add(tabbedPane);

        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
}

public class Program {
    public static void main(String[] args) {
        new ShapesFrame();
    }
}