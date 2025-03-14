import itertools

class Kopiec:
    def __init__(self, min_heap=True):
        """
        Tworzy kopiec.
        Jeśli min_heap == True, kopiec minimalny (rodzic <= dzieci),
        w przeciwnym razie kopiec maksymalny (rodzic >= dzieci).
        Kopiec przechowywany jest w liście self.heap.
        """
        self.heap = []
        self.min_heap = min_heap

    def __len__(self):
        return len(self.heap)

    def rodzic(self, i):
        return (i - 1) // 2 if i > 0 else None

    def lewy_syn(self, i):
        return 2 * i + 1

    def prawy_syn(self, i):
        return 2 * i + 2

    def porownaj(self, a, b):
        """
        Zwraca True, jeśli element a powinien być powyżej elementu b.
        Dla kopca minimalnego: a < b, dla maksymalnego: a > b.
        Porównujemy krotki – porównanie odbywa się najpierw względem wartości.
        """
        return a < b if self.min_heap else a > b

    def dodaj(self, wartosc):
        """
        Dodaje nowy element do kopca (na koniec listy) i przesiewa go w górę.
        """
        self.heap.append(wartosc)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0:
            p = self.rodzic(i)
            if p is not None and not self.porownaj(self.heap[p], self.heap[i]):
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
            else:
                break

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            lewy = self.lewy_syn(i)
            prawy = self.prawy_syn(i)
            k = i  # kandydat do zamiany
            if lewy < n and not self.porownaj(self.heap[k], self.heap[lewy]):
                k = lewy
            if prawy < n and not self.porownaj(self.heap[k], self.heap[prawy]):
                k = prawy
            if k != i:
                self.heap[i], self.heap[k] = self.heap[k], self.heap[i]
                i = k
            else:
                break

    def usun_korzen(self):
        """
        Usuwa i zwraca element z korzenia kopca.
        Jeśli kopiec jest pusty, zwraca None.
        """
        if not self.heap:
            return None
        korzen = self.heap[0]
        ostatni = self.heap.pop()
        if self.heap:
            self.heap[0] = ostatni
            self._heapify_down(0)
        return korzen

    def get_korzen(self):
        """Zwraca korzeń kopca bez usuwania (None, jeśli kopiec jest pusty)."""
        return self.heap[0] if self.heap else None

    def buduj_kopiec(self, lista):
        """Buduje kopiec z podanej listy."""
        self.heap = lista[:]
        n = len(self.heap)
        for i in range((n - 2) // 2, -1, -1):
            self._heapify_down(i)


class PodwojnaKolejkaPriorytetowa:
    def __init__(self):
        """
        Podwójna kolejka priorytetowa realizowana jest przy użyciu dwóch kopców:
         - min_heap: kopiec minimalny – korzeń to najmniejszy element
         - max_heap: kopiec maksymalny – korzeń to największy element
        Każdy element jest zapisywany jako krotka (wartość, id).
        Aby umożliwić usuwanie z obu kopców bez konieczności synchronizacji,
        stosujemy słownik entry_finder, który śledzi aktywne wpisy.
        """
        self.min_heap = Kopiec(min_heap=True)
        self.max_heap = Kopiec(min_heap=False)
        self.counter = itertools.count()  # generator unikalnych identyfikatorów
        self.entry_finder = {}  # id -> (wartość, id)

    def insert(self, value):
        """Wstawia element do kolejki priorytetowej."""
        ident = next(self.counter)
        entry = (value, ident)
        self.entry_finder[ident] = entry
        self.min_heap.dodaj(entry)
        self.max_heap.dodaj(entry)

    def _clean_min_heap(self):
        """
        Usuwa z kopca min_heap wpisy, które zostały już usunięte (nie są w entry_finder).
        """
        while self.min_heap.heap and self.min_heap.heap[0][1] not in self.entry_finder:
            self.min_heap.usun_korzen()

    def _clean_max_heap(self):
        """
        Usuwa z kopca max_heap wpisy, które zostały już usunięte.
        """
        while self.max_heap.heap and self.max_heap.heap[0][1] not in self.entry_finder:
            self.max_heap.usun_korzen()

    def find_min(self):
        """Zwraca minimalny element bez usuwania lub None, jeśli kolejka jest pusta."""
        self._clean_min_heap()
        if not self.min_heap.heap:
            return None
        return self.min_heap.heap[0][0]

    def find_max(self):
        """Zwraca maksymalny element bez usuwania lub None, jeśli kolejka jest pusta."""
        self._clean_max_heap()
        if not self.max_heap.heap:
            return None
        return self.max_heap.heap[0][0]

    def deletemin(self):
        """
        Usuwa i zwraca minimalny element z kolejki.
        Jeśli kolejka jest pusta, zwraca None.
        """
        self._clean_min_heap()
        if not self.min_heap.heap:
            return None
        entry = self.min_heap.usun_korzen()
        if entry is not None:
            value, ident = entry
            if ident in self.entry_finder:
                del self.entry_finder[ident]
            return value
        return None

    def deletemax(self):
        """
        Usuwa i zwraca maksymalny element z kolejki.
        Jeśli kolejka jest pusta, zwraca None.
        """
        self._clean_max_heap()
        if not self.max_heap.heap:
            return None
        entry = self.max_heap.usun_korzen()
        if entry is not None:
            value, ident = entry
            if ident in self.entry_finder:
                del self.entry_finder[ident]
            return value
        return None

    def __len__(self):
        """Zwraca liczbę aktualnych (aktywnych) elementów w kolejce."""
        return len(self.entry_finder)


# Przykładowe użycie
if __name__ == '__main__':
    print("==== Podwójna kolejka priorytetowa ====")
    pkp = PodwojnaKolejkaPriorytetowa()
    dane = [5, 3, 8, 1, 9, 2, 7]
    
    print("Wstawianie elementów:")
    for x in dane:
        pkp.insert(x)
        print(f"Wstawiono {x} -> min: {pkp.find_min()}, max: {pkp.find_max()}")
    
    print("\nUsuwanie elementów metodą deletemin:")
    while len(pkp) > 0:
        min_elem = pkp.deletemin()
        print("deletemin:", min_elem, "-> Nowe min:", pkp.find_min(), "max:", pkp.find_max())
    
    # Dla demonstracji wstawiamy elementy ponownie
    for x in dane:
        pkp.insert(x)
    
    print("\nUsuwanie elementów metodą deletemax:")
    while len(pkp) > 0:
        max_elem = pkp.deletemax()
        print("deletemax:", max_elem, "-> Nowe min:", pkp.find_min(), "max:", pkp.find_max())
