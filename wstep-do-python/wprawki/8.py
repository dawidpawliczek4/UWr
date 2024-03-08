string = '150-2*24+12/20=147'
string = '147=150-2*24+12/20'

def fn(string):
    string = string.split('=')
    string1 = string[0]
    string2 = string[1]
    for i in range(len(string1)):
        for j in range(i+1, len(string1) + 1):
            nowyStr = string1[:i] + '(' + string1[i:j] + ')' + string1[j:]
            try:
                wynik = eval(nowyStr)                        
                if float(wynik) == float(string2):                    
                    return nowyStr + "=" + string2
            except:
                continue

    string1, string2 = string2, string1
    for i in range(len(string1)):
        for j in range(i+1, len(string1) + 1):
            nowyStr = string1[:i] + '(' + string1[i:j] + ')' + string1[j:]
            try:
                wynik = eval(nowyStr)                        
                if float(wynik) == float(string2):                    
                    return string2 + "=" + nowyStr
            except:
                continue
    return ''

print(fn(string))