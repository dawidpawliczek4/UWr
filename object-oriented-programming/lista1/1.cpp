// Dawid Pawliczek, lista 1 zadanie 1, g++

#include <iostream>
#include <cmath>

enum TypFigury
{
    TROJKAT,
    KOLO,
    KWADRAT
};

struct Punkt
{
    float x, y;

    Punkt(float x, float y) : x(x), y(y) {}
};

struct Figura {
    TypFigury typ;
    Punkt pozycja;
    float rozmiar;    

    Figura(TypFigury typ, Punkt pozycja, float rozmiar) : typ(typ), pozycja(pozycja), rozmiar(rozmiar) {}
};


Figura* new_square(float x, float y, float size)
{
    if (size <= 0)
    {
        std::cerr << "Błąd: nieprawidłowy rozmiar boku kwadratu." << std::endl;
        return nullptr;
    }
    return new Figura(KWADRAT, Punkt(x, y), size);
}

Figura* new_circle(float x, float y, float size)
{
    if (size <= 0)
    {
        std::cerr << "Błąd: nieprawidłowy promień." << std::endl;
        return nullptr;
    }
    return new Figura(KOLO, Punkt(x, y), size);
}

Figura *new_triangle(float x, float y, float size)
{
    if (size <= 0)
    {
        std::cerr << "Błąd: nieprawidłowy rozmiar boku trojkąta." << std::endl;
        return nullptr;
    }
    return new Figura(KWADRAT, Punkt(x, y), size);
}

float pole(Figura* f)
{
    switch (f->typ)
    {
    case KWADRAT:
        return f->rozmiar * f->rozmiar;
    case KOLO:
        return M_PI * f->rozmiar * f->rozmiar;
    case TROJKAT:
        return (sqrt(3) / 4) * f->rozmiar * f->rozmiar;
    default:
        return 0;
    }
}

void przesun(Figura *f, float x, float y)
{
    f->pozycja.x += x;
    f->pozycja.y += y;
}

void show(Figura *f)
{
    std::cout << "Typ figury: ";
    switch (f->typ)
    {
    case KWADRAT:
        std::cout << "Kwadrat";
        break;
    case KOLO:
        std::cout << "Koło";
        break;
    case TROJKAT:
        std::cout << "Trójkąt";
        break;
    default:
        std::cout << "Nieznany";
    }
    std::cout << ", Pozycja: (" << f->pozycja.x << ", " << f->pozycja.y << "), Rozmiar: " << f->rozmiar << std::endl;
}

float sumaPol(Figura *f[], int size)
{
    float suma = 0;
    for (int i = 0; i < size; ++i)
    {
        suma += pole(f[i]);
    }
    return suma;
}

int main()
{
    Figura *figury[3];
    figury[0] = new_square(0, 0, 2);
    figury[1] = new_circle(0, 0, 2);
    figury[2] = new_triangle(0, 0, 2);
    std::cout << sumaPol(figury, 3) << std::endl;
    return 0;
}