import heapq
import itertools

REMOVED = '<removed>'  # znacznik usunięcia

class PodwojnaKolejkaPriorytetowa:
    def __init__(self):
        # min_heap – kopiec rosnący, elementy postaci (wartosc, id)
        self.min_heap = []
        # max_heap – kopiec malejący, realizowany przez przechowywanie (-wartosc, id)
        self.max_heap = []
        # unikalny generator identyfikatorów
        self.counter = itertools.count()
        # słownik: id -> [wartosc, id]; pozwala śledzić aktywne wpisy
        self.entry_finder = {}

    def insert(self, wartosc):
        """Wstawia element do kolejki."""
        id = next(self.counter)
        entry = [wartosc, id]
        self.entry_finder[id] = entry
        heapq.heappush(self.min_heap, entry)
        # W kopcu maksymalnym przechowujemy (-wartosc, id)
        heapq.heappush(self.max_heap, (-wartosc, id))

    def _clean_heap(self, heap):
        """
        Usuwa z kopca wpisy oznaczone jako usunięte.
        Zwraca aktualny korzeń kopca lub None, jeśli kopiec jest pusty.
        """
        while heap:
            wart, id = heap[0]
            if id not in self.entry_finder:
                heapq.heappop(heap)
            else:
                return heap[0]
        return None

    def find_min(self):
        """Zwraca minimalny element (bez usuwania) lub None, jeśli kolejka jest pusta."""
        entry = self._clean_heap(self.min_heap)
        return entry[0] if entry is not None else None

    def find_max(self):
        """Zwraca maksymalny element (bez usuwania) lub None, jeśli kolejka jest pusta."""
        entry = self._clean_heap(self.max_heap)
        return -entry[0] if entry is not None else None

    def deletemin(self):
        """Usuwa i zwraca minimalny element lub None, jeśli kolejka jest pusta."""
        while self.min_heap:
            wart, id = heapq.heappop(self.min_heap)
            if id in self.entry_finder:
                # usuń wpis z entry_finder – oznaczony jako usunięty
                del self.entry_finder[id]
                return wart
        return None

    def deletemax(self):
        """Usuwa i zwraca maksymalny element lub None, jeśli kolejka jest pusta."""
        while self.max_heap:
            wart, id = heapq.heappop(self.max_heap)
            if id in self.entry_finder:
                del self.entry_finder[id]
                return -wart
        return None

    def __len__(self):
        return len(self.entry_finder)

