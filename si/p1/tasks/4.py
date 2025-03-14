import copy

def opt_dist(lst, d):
    min_changes = float('inf')
    for i in range(0, len(lst) - d + 1):        
        changes = 0
        for j in range(i, i+d):
            if lst[j] == 0:                
                changes += 1
        for j in range(0, i):
            if lst[j] == 1:
                changes += 1
        for j in range(i+d, len(lst)):
            if lst[j] == 1:
                changes += 1
        if changes < min_changes:
            min_changes = changes
    return min_changes

with open("zad4_input.txt", encoding="utf-8") as fin, \
     open("zad4_output.txt", "w", encoding="utf-8") as fout:
    for line in fin:        
        lst, D = line.strip().split(" ")
        D = int(D)
        lst = [int(ch) for ch in lst]
        out = opt_dist(lst, D)        
        fout.write(str(out) + "\n")                  