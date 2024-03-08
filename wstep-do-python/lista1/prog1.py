
# 3x3
# 5x5
# 7x7
# 9x9
# 11x11

# 3x3
# 4x4
# 5x5
# 6x6
# 7x7


def kwadrat(n, znak):
    for i in range(n):
       print (n * znak)      
  

ile = 3
for i in range(5):
    print ("Przebieg:", i)
    print (20 * "-")
    kwadrat(ile, "*")
    ile += 2

ile = 3
for i in range(5, 10):
    print("Przebieg: ", i)
    print (20 * "-")
    kwadrat(ile, "#")
    ile += 1
