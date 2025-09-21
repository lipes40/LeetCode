def main(s):
    map = ""
    for j in range(len(s), 0, -1):
        # print("j:",j)
        for i in range(0, len(s), 1):
            map += s[i]
            if len(map) >= j:
                # print(f"map:{map}")
                invert = map[::-1]
                if invert == map:
                    return map
                else:
                    # print("i",i)
                    map = map[1:]
        map = ""



                

# s = "babad"
# s = "cbbd"
s = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
result = main(s)
print(result)