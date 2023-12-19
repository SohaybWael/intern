#1 - Input : A binary string 's' representing a street where each character represents the type of building at that position. '0' denotes an office building. '1' denotes a restaurant.
#2 - Objective : The goal is to select 3 buildings for random inspection.
#3 - The rule : No two consecutive buildings out of the selected three can be of the same type.

def numberOfWays(s):
    NumWays = 0
    #waysThemselves = []
    for i in range(len(s)-2):
        for j in range(i+1, len(s)-1):
            for k in range(j+1, len(s)):
                if s[i] != s[j] and s[j] != s[k]:
                    NumWays += 1
                    #waysThemselves.append(s[i] + s[j] + s[k])
    return NumWays#, waysThemselves

print(numberOfWays("1100110"))


