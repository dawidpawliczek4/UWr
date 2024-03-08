def usun_duplikaty(L):    
    indexed_list = [(value, index) for index, value in enumerate(L)]    
    print(indexed_list)
    indexed_list.sort()
    result = []
    
    if indexed_list:
        result.append(indexed_list[0])
    
    for i in range(1, len(indexed_list)):
        if indexed_list[i][0] != indexed_list[i-1][0]:
            result.append(indexed_list[i])
    
    print(result)
    result.sort(key=lambda x: x[1])
    
    return [value for value, index in result]



print(usun_duplikaty([1, 2, 3, 1, 2, 3, 8, 2, 2, 9, 9, 4]))