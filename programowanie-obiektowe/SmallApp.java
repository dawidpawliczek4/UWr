import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

class Figura implements Serializable
{
    private double Pole;
    private double Obw;
    private String Nazwa;

    public Figura(double Pole,double Obw,String Nazwa)
    {
        this.Pole = Pole;
        this.Obw = Obw;
        this.Nazwa = Nazwa;
    }

    public Figura() 
    {
        this(0,0,"");
    }

    public String Kod()
    {
        return (Pole + "") + "-" + (Obw + "") + "-" + Nazwa;
    }

    public class FiguraEdit 
    {
        private JFrame okno;
        private JTextField area,circ,name;
        private JButton save,cancel;

        public  FiguraEdit()
        {
            okno = new JFrame("FIGURA EDIT");
            okno.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            okno.setSize(500,400);
            okno.setLocationRelativeTo(null);

            Container kontener = okno.getContentPane();
            GridLayout uklad = new GridLayout(4,2);
            kontener.setLayout(uklad);

            area = new JTextField(String.valueOf(Pole));
            circ = new JTextField(String.valueOf(Obw));
            name = new JTextField(Nazwa);

            kontener.add(new JLabel("Pole"));
            kontener.add(area);
            kontener.add(new JLabel("Obwod"));
            kontener.add(circ);
            kontener.add(new JLabel("Nazwa"));
            kontener.add(name);

            save = new JButton("ZAPISZ");
            cancel = new JButton("ANULUJ");

            kontener.add(save);
            kontener.add(cancel);

            save.addActionListener(
                new ActionListener() 
                {
                    public void actionPerformed(ActionEvent event)
                    {
                        try
                        {
                            Pole = Double.parseDouble(area.getText());
                            Obw = Double.parseDouble(circ.getText());
                            Nazwa = name.getText();
                        }
                        catch (NumberFormatException except)
                        {
                            System.err.println("Blad : nieprawidlowy format danych w okienku");
                            Pole = 0.0;
                            Obw = 0.0;
                            Nazwa = "";
                        }
                        try
                        {
                            FileOutputStream fileOut = new FileOutputStream("figura.ser");
                            ObjectOutputStream out = new ObjectOutputStream(fileOut);
                            out.writeObject(Figura.this);
                            out.close();
                            fileOut.close();
                        }
                        catch(FileNotFoundException e)
                        {
                            System.err.println("Nie można znaleźć pliku i nie udało się utworzyć nowego: ");
                        }
                        catch(IOException e)
                        {
                            System.err.println("Błąd we/wy: ");
                        }
                    }
                }
            );

            cancel.addActionListener(
                new ActionListener() 
                {
                    public void actionPerformed(ActionEvent event)
                    {
                        area.setText(String.valueOf(Pole));
                        circ.setText(String.valueOf(Obw));
                        name.setText(Nazwa);

                        okno.dispose();
                    }
                }
            );
            okno.pack();
            okno.setVisible(true);
        }
    }
}

class Okrag extends Figura implements Serializable
{
    private double Radius;
    private double X;
    private double Y;

    public Okrag(double Radius,double X,double Y)
    {
        this.Radius = Radius;
        this.X = X;
        this.Y = Y;
    }

    public Okrag()
    {
        this(0,0,0);
    }

    public String KodOkrag()
    {
        return (Radius + "") + "-" + (X + "") + "-" + (Y + "");
    }

    public class OkragEdit 
    {
        private JFrame okno;
        private JTextField radius,x,y;
        private JButton save,cancel;

        public OkragEdit()
        {
            okno = new JFrame("FIGURA EDIT");
            okno.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            okno.setSize(500,400);
            okno.setLocationRelativeTo(null);

            Container kontener = okno.getContentPane();
            GridLayout uklad = new GridLayout(4,2);
            kontener.setLayout(uklad);

            radius = new JTextField(String.valueOf(Radius));
            x = new JTextField(String.valueOf(X));
            y = new JTextField(String.valueOf(Y));

            kontener.add(new JLabel("Promien"));
            kontener.add(radius);
            kontener.add(new JLabel("X"));
            kontener.add(x);
            kontener.add(new JLabel("Y"));
            kontener.add(y);

            save = new JButton("ZAPISZ");
            cancel = new JButton("ANULUJ");

            kontener.add(save);
            kontener.add(cancel);

            save.addActionListener(
                new ActionListener() 
                {
                    public void actionPerformed(ActionEvent event)
                    {
                        try
                        {
                            Radius = Double.parseDouble(radius.getText());
                            X = Double.parseDouble(x.getText());
                            Y = Double.parseDouble(y.getText());
                        }
                        catch (NumberFormatException except)
                        {
                            System.err.println("Blad : nieprawidlowy format danych w okienku");
                            Radius = 0.0;
                            X = 0.0;
                            Y = 0.0;
                        }
                        try
                        {
                            FileOutputStream fileOut = new FileOutputStream("okrag.ser");
                            ObjectOutputStream out = new ObjectOutputStream(fileOut);
                            out.writeObject(Okrag.this);
                            out.close();
                            fileOut.close();
                        }
                        catch(FileNotFoundException e)
                        {
                            System.err.println("Nie można znaleźć pliku i nie udało się utworzyć nowego: ");
                        }
                        catch(IOException e)
                        {
                            System.err.println("Błąd we/wy: ");
                        }
                    }
                }
            );

            cancel.addActionListener(
                new ActionListener() 
                {
                    public void actionPerformed(ActionEvent event)
                    {
                        radius.setText(String.valueOf(Radius));
                        x.setText(String.valueOf(X));
                        y.setText(String.valueOf(Y));

                        okno.dispose();
                    }
                }
            );
            okno.pack();
            okno.setVisible(true);
        }
    }
}

class Trojkat extends Figura implements Serializable
{
    private double Kat1;
    private double Kat2;
    private double Kat3;

    public Trojkat(double Kat1,double Kat2,double Kat3)
    {
        this.Kat1 = Kat1;
        this.Kat2 = Kat2;
        this.Kat3 = Kat3;
    }

    public Trojkat()
    {
        this(0,0,0);
    }

    public String KodTrojkat()
    {
        return (Kat1 + "") + "-" + (Kat2 + "") + "-" + (Kat3 + "");
    }

    public class TrojkatEdit 
    {
        private JFrame okno;
        private JTextField k1,k2,k3;
        private JButton save,cancel;

        public TrojkatEdit()
        {
            okno = new JFrame("FIGURA EDIT");
            okno.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            okno.setSize(500,400);
            okno.setLocationRelativeTo(null);

            Container kontener = okno.getContentPane();
            GridLayout uklad = new GridLayout(4,2);
            kontener.setLayout(uklad);

            k1 = new JTextField(String.valueOf(Kat1));
            k2 = new JTextField(String.valueOf(Kat2));
            k3 = new JTextField(String.valueOf(Kat3));

            kontener.add(new JLabel("Kat1"));
            kontener.add(k1);
            kontener.add(new JLabel("Kat2"));
            kontener.add(k2);
            kontener.add(new JLabel("Kat3"));
            kontener.add(k3);

            save = new JButton("ZAPISZ");
            cancel = new JButton("ANULUJ");

            kontener.add(save);
            kontener.add(cancel);

            save.addActionListener(
                new ActionListener() 
                {
                    public void actionPerformed(ActionEvent event)
                    {
                        try
                        {
                            Kat1 = Double.parseDouble(k1.getText());
                            Kat2 = Double.parseDouble(k2.getText());
                            Kat3 = Double.parseDouble(k3.getText());
                        }
                        catch (NumberFormatException except)
                        {
                            System.err.println("Blad : nieprawidlowy format danych w okienku");
                            Kat1 = 0.0;
                            Kat2 = 0.0;
                            Kat3 = 0.0;
                        }
                        try
                        {
                            FileOutputStream fileOut = new FileOutputStream("trojkat.ser");
                            ObjectOutputStream out = new ObjectOutputStream(fileOut);
                            out.writeObject(Trojkat.this);
                            out.close();
                            fileOut.close();
                        }
                        catch(FileNotFoundException e)
                        {
                            System.err.println("Nie można znaleźć pliku i nie udało się utworzyć nowego: ");
                        }
                        catch(IOException e)
                        {
                            System.err.println("Błąd we/wy: ");
                        }
                    }
                }
            );

            cancel.addActionListener(
                new ActionListener() 
                {
                    public void actionPerformed(ActionEvent event)
                    {
                        k1.setText(String.valueOf(Kat1));
                        k2.setText(String.valueOf(Kat2));
                        k3.setText(String.valueOf(Kat3));

                        okno.dispose();
                    }
                }
            );
            okno.pack();
            okno.setVisible(true);
        }
    }
}