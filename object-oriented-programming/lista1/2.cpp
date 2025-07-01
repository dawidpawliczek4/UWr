// Dawid Pawliczek, lista 1 zadanie 2, g++
#include <iostream>

struct Ulamek
{
    int licznik;
    int mianownik;
    Ulamek(int licznik, int mianownik) : licznik(licznik), mianownik(mianownik) {};
};

int nwd(int a, int b)
{
    while (b != 0)
    {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

Ulamek *nowy_ulamek(int num, int denom)
{
    if (denom == 0)
    {
        std::cerr << "Mianownik nie może być równy 0" << std::endl;
        return nullptr;
    }

    int dzielnik = nwd(num, denom);
    num /= dzielnik;
    denom /= dzielnik;

    if (denom < 0)
    {
        num = -num;
        denom = -denom;
    }

    return new Ulamek(num, denom);    
}

void show(Ulamek *u)
{
    if (u != nullptr)
    {
        std::cout << u->licznik << "/" << u->mianownik << std::endl;
    }
}

Ulamek *dodaj(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr) return nullptr;

    int num = u1->licznik * u2->mianownik + u2->licznik * u1->mianownik;
    int denom = u1->mianownik * u2->mianownik;
    return nowy_ulamek(num, denom);
}

void dodaj2(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr ) return;

    int licznik = u1->licznik * u2->mianownik + u2->licznik * u1->mianownik;
    int mianownik = u1->mianownik * u2->mianownik;

    int dzielnik = nwd(licznik, mianownik);
    licznik /= dzielnik;
    mianownik /= dzielnik;

    u2->licznik = licznik;
    u2->mianownik = mianownik;
}

Ulamek *odejmij(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr) return nullptr;
    
    int num = u1->licznik * u2->mianownik - u2->licznik * u1->mianownik;
    int denom = u1->mianownik * u2->mianownik;

    return nowy_ulamek(num, denom);
}

void odejmij2(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr) return;

    int licznik = u1->licznik * u2->mianownik - u2->licznik * u1->mianownik;
    int mianownik = u1->mianownik * u2->mianownik;

    int dzielnik = nwd(licznik, mianownik);
    licznik /= dzielnik;
    mianownik /= dzielnik;

    u2->licznik = licznik;
    u2->mianownik = mianownik;
}

Ulamek *mnoz(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr) return nullptr;

    int num = u1->licznik * u2->licznik;
    int denom = u1->mianownik * u2->mianownik;

    return nowy_ulamek(num, denom);
}

void mnoz2(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr) return;

    int licznik = u1->licznik * u2->licznik;
    int mianownik = u1->mianownik * u2->mianownik;

    int dzielnik = nwd(licznik, mianownik);
    licznik /= dzielnik;
    mianownik /= dzielnik;

    u2->licznik = licznik;
    u2->mianownik = mianownik;
}

Ulamek *dziel(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr || u2->licznik == 0)
    {
        std::cerr << "Nie można dzielić przez ułamek o liczniku równym 0" << std::endl;
        return nullptr;
    }
    int num = u1->licznik * u2->mianownik;
    int denom = u1->mianownik * u2->licznik;

    return nowy_ulamek(num, denom);
}

void dziel2(Ulamek *u1, Ulamek *u2)
{
    if (u1 == nullptr || u2 == nullptr || u2->licznik == 0) return;

    int licznik = u1->licznik * u2->mianownik;
    int mianownik = u1->mianownik * u2->licznik;

    int dzielnik = nwd(licznik, mianownik);
    licznik /= dzielnik;
    mianownik /= dzielnik;

    u2->licznik = licznik;
    u2->mianownik = mianownik;
}

int main() {

    Ulamek *u1 = nowy_ulamek(1, 2);
    Ulamek *u2 = nowy_ulamek(1, 3);
    Ulamek *u3 = dodaj(u1, u2);
    show(u3);

    return 0;
}