

def usun_w_nawiasach(s):
    deleting = False
    temp = ""
    for c in s:
        if deleting:
            if c == ")":
                deleting = False
        else:
            if c == "(":
                deleting = True
            else:
                temp += c
    return temp
        



s = "Ala ma(abc) kota(eee)!"
print(usun_w_nawiasach(s))


