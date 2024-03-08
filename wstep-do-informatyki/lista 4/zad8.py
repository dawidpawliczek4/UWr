def czy_podobne(n, m):
    # Przekształć liczby na stringi, aby łatwiej można było iterować przez cyfry
    n_str = str(n)
    m_str = str(m)

    # Stwórz słowniki do zliczania wystąpień cyfr w obu liczbach
    n_count = {}
    m_count = {}

    # Zlicz wystąpienia cyfr w pierwszej liczbie
    for cyfra in n_str:
        if cyfra in n_count:
            n_count[cyfra] += 1
        else:
            n_count[cyfra] = 1

    # Zlicz wystąpienia cyfr w drugiej liczbie
    for cyfra in m_str:
        if cyfra in m_count:
            m_count[cyfra] += 1
        else:
            m_count[cyfra] = 1

    # Porównaj słowniki
    for cyfra in n_count:
        if n_count[cyfra] != m_count.get(cyfra, 0):
            return False

    for cyfra in m_count:
        if m_count[cyfra] != n_count.get(cyfra, 0):
            return False

    return True

# Przykładowe wywołania
print(czy_podobne(123412, 223411))  # Powinno zwrócić True
print(czy_podobne(123412, 11234))   # Powinno zwrócić False
print(czy_podobne(123412, 1234512)) # Powinno zwrócić False

# O(n+m), O(n+m)