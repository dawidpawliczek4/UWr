
def bubbleSort(tab):

    for i in range(len(tab)-1):
        for j in range(len(tab)-1 - i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    
    print(tab)


bubbleSort([142,32,3241,94,2,1])