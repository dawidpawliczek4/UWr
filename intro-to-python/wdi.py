
def sumaPN(r):
    def pomoc(r, i):
        nonlocal sumyParzyste, sumyNieparzyste
        if i % 2 == 0:
            sumyParzyste += r.val
        else:
            sumyNieparzyste += r.val
        
        if r.left != None:
            pomoc(r.left, i+1)
        if r.right != None:
            pomoc(r.right, i+1)

    sumyParzyste = r.val
    sumyNieparzyste = 0

    pomoc(r.left, 1)
    pomoc(r.right, 1)
    
    return sumyParzyste - sumyNieparzyste

