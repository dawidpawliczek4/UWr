

def podziel(s):
    czyTekst = False

    tab = []

    tekst = ""

    for c in s:
        if c != " ":
            czyTekst = True
        else:
            czyTekst = False
            if tekst:
                tab.append(tekst)
                tekst = ""
        if czyTekst:
            tekst += c

    print(tab)

podziel("  Ala ma  kota  ") 