
def wypisz(t):
    if t != None:
        wypisz(t.left)
        if t.val > 0:
            print(t.val)
        wypisz(t.right)