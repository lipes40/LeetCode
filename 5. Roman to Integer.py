def conta(array):
        result = 0
        while len(array) > 0:
            maximo = max(array)
            index = array.index(maximo)
            sub = sum(array[:index])
            result += (maximo - sub) #+ sum(array[index:])
            array = array[index+1:]
        return result

def romanToInt(s):

    lista = list(s)

    map = [] 

    result = 0

    for i in lista:
        if i == "M":
            map.append(1000)
        if i == "D":
            map.append(500)
        if i == "C":
            map.append(100)
        if i == "L":
            map.append(50)
        if i == "X":
            map.append(10)
        if i == "V":
            map.append(5)
        if i == "I":
            map.append(1)


    result += conta(map)
    return(result)

a = romanToInt("")
print(a)