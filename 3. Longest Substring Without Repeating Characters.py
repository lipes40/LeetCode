import time

def repeting(s):
    cont = 0
    for i, char1 in enumerate(s):
        eMapa = []
        eMapa.append(char1)
        for j in range(i + 1, len(s)):
            if not s[j] in eMapa:
                eMapa.append(s[j])
            else:
                break
        if len(eMapa) > cont:
            cont = len(eMapa)
    return cont

def lengthOfLongestSubstring(s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


string = "pwwkew"
inicio = time.time()
a = repeting(string)
print(a)
print(f"Tempo: {time.time() - inicio}")

inicio = time.time()
b = lengthOfLongestSubstring(string)
print(b)
print(f"Tempo: {time.time() - inicio}")
