class Kopiec:
    def __init__(self):
        # Kopiec przechowywany jest jako lista
        self.heap = []

    def rodzic(self, index):
        # Zwraca indeks rodzica danego elementu
        if index == 0:
            return None
        return (index - 1) // 2

    def lewy_syn(self, index):
        # Zwraca indeks lewego syna
        return 2 * index + 1

    def prawy_syn(self, index):
        # Zwraca indeks prawego syna
        return 2 * index + 2

    def dodaj(self, wartosc):
        # Dodajemy nowy element do kopca
        self.heap.append(wartosc)
        # Przywracamy własność kopca (przesiewamy w górę)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Przesiewanie w górę: porównujemy wstawiony element z rodzicem i zamieniamy, jeśli zachodzi potrzeba
        while index > 0:
            parent = self.rodzic(index)
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def usun_min(self):
        # Usuwamy najmniejszy element (korzeń kopca)
        if not self.heap:
            return None
        min_val = self.heap[0]
        ostatni = self.heap.pop()  # usuwamy ostatni element
        if self.heap:
            # Umieszczamy ostatni element na miejscu korzenia i przesiewamy w dół
            self.heap[0] = ostatni
            self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        # Przesiewanie w dół: przywracanie własności kopca od korzenia
        n = len(self.heap)
        while True:
            lewy = self.lewy_syn(index)
            prawy = self.prawy_syn(index)
            najmniejszy = index

            if lewy < n and self.heap[lewy] < self.heap[najmniejszy]:
                najmniejszy = lewy
            if prawy < n and self.heap[prawy] < self.heap[najmniejszy]:
                najmniejszy = prawy

            if najmniejszy == index:
                break

            self.heap[index], self.heap[najmniejszy] = self.heap[najmniejszy], self.heap[index]
            index = najmniejszy

    def get_min(self):
        # Zwraca minimalny element kopca (bez usuwania)
        if self.heap:
            return self.heap[0]
        return None

    def buduj_kopiec(self, lista):
        # Budowanie kopca na podstawie podanej listy
        self.heap = lista[:]
        # Rozpoczynamy od ostatniego rodzica i przesiewamy w dół
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self._heapify_down(i)


# Przykładowe użycie:
if __name__ == '__main__':
    kopiec = Kopiec()

    # Dodawanie elementów do kopca
    dane = [5, 3, 8, 1, 9, 2]
    for wartosc in dane:
        kopiec.dodaj(wartosc)
        print("Dodano:", wartosc, "Kopiec:", kopiec.heap)

    print("Minimum:", kopiec.get_min())

    # Usuwanie elementów z kopca
    while kopiec.heap:
        print("Usuwam min:", kopiec.usun_min(), "Kopiec:", kopiec.heap)
