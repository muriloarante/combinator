from itertools import combinations

def printCombinations(arr, size):
    for combination in combinations(arr, size):
        for char in combination:
            print(c, end=" ")
        print("")
    
n = 1 
elements = [c for c in range(1, size + 1)]
choose = 1 

printCombinations(elements, choose)
print(f"There are {len(list(combinations(elements, choose)))} combinations.")
