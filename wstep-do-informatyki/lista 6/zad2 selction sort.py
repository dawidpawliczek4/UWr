

def selection_sort(tab):
    for i in range(len(tab)):
        for j in range(i, len(tab)):
            if tab[j] < tab[i]:
                tab[i], tab[j] = tab[j], tab[i]
  
    print(tab)

selection_sort([2,4124,42110,9999,231,1,5195921,13])