# a)
def sumy_podzbiorow(L):
    if not L:
        return {0}
    else:
        sums_with_first_element = {x + L[0] for x in sumy_podzbiorow(L[1:])}
        sums_without_first_element = sumy_podzbiorow(L[1:])
        return sums_with_first_element.union(sums_without_first_element)


L = [1, 2, 3, 100]
print(sumy_podzbiorow(L))