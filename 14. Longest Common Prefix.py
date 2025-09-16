def main(strs):
    listagem = strs
    result = ""
    map = []
    for i, num in enumerate(listagem[0]):
        for j in strs:
            if i < len(j):
                if j[i] == num:
                    map.append(j[i])
        if len(map) == len(listagem):
            result += map[0]
        else:
            return result
        map = []
    return result
    

        
    


# strs = ["flower","flow","flight"]
strs = ["a"]
result = main(strs)
print(result)