def palindromo(num):
    num = str(num)
    lista = list(num)
    
    reverse = []
    for i in num:
        reverse.insert(0, i)
    
    if lista == reverse:
        return True
    return False


a = palindromo(int(input("Qual número: ")))
print(a)