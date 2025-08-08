import time

def twoSum(nums, target):
    inicio = time.time()
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if j != i and num1 + num2 == target:
                print(f"Tempo: {time.time() - inicio}")
                return [i, j]

def twoSumMap(nums, target):
    inicio = time.time()
    mapa = {}
    for i, num in enumerate(nums):
        alvo = target - num
        if alvo in mapa:
            print(f"Tempo: {time.time() - inicio}")
            return [mapa[alvo], i]
        mapa[num] = i


nums = [1, 3, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,22,2,2,22,2,2,2,2,2,2,2,2,2,2,22,22,22,22,3]
target = 6

a = twoSum(nums, target)
b = twoSumMap(nums, target)
print(a)
print(b)