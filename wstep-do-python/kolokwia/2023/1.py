
def kwadrat(bok, grubosc):
    for i in range(grubosc):
        print('*' * bok)
    for i in range(bok - 2*grubosc):
        print('*' * grubosc + ' ' * (bok - 2*grubosc) + '*' * grubosc)
    for i in range(grubosc):
        print('*' * bok)

kwadrat(15, 3)