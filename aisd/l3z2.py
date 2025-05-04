def majority_element_dc(A, low, high):
    """
    Rekurencyjna funkcja zwracająca kandydata na element większościowy
    dla fragmentu tablicy A[low..high].
    Jeśli w danym przedziale nie ma elementu większościowego, funkcja zwraca None.
    """
    # Przypadek bazowy: fragment jednoelementowy
    if low == high:
        return A[low]
    
    # Dzielimy tablicę na dwie połówki
    mid = (low + high) // 2
    left_candidate = majority_element_dc(A, low, mid)
    right_candidate = majority_element_dc(A, mid + 1, high)
    
    # Jeśli obaj kandydaci są tacy sami, zwracamy jednego z nich
    if left_candidate == right_candidate:
        return left_candidate
    
    # W przeciwnym razie, liczymy wystąpienia obu kandydatów w przedziale A[low..high]
    left_count = sum(1 for i in range(low, high + 1) if A[i] == left_candidate)
    right_count = sum(1 for i in range(low, high + 1) if A[i] == right_candidate)
    
    # Określamy, czy któryś z kandydatów spełnia warunek większości (więcej niż połowa elementów)
    if left_count > (high - low + 1) // 2:
        return left_candidate
    elif right_count > (high - low + 1) // 2:
        return right_candidate
    else:
        return None

def find_majority_element(A):
    """
    Funkcja pomocnicza, która wywołuje rekurencyjną funkcję majority_element_dc
    dla całej tablicy i przeprowadza ostateczną weryfikację kandydata.
    """
    candidate = majority_element_dc(A, 0, len(A) - 1)
    # Weryfikacja: liczymy wystąpienia kandydata w całej tablicy
    if candidate is not None and A.count(candidate) > len(A) // 2:
        return candidate
    else:
        return None

# Przykład użycia:
if __name__ == "__main__":
    A = [2, 2, 1, 2, 3, 2, 2]
    result = find_majority_element(A)
    if result is not None:
        print("Element większościowy:", result)
    else:
        print("Brak elementu większościowego")