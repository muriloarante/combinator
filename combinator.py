from itertools import combinations

def printCombinations(arr, size):
    for p in combinations(arr, size):
        for c in p:
            print(c, end=" ")
        print("")
    
size = 1 # Quantos elementos a lista deve ter.
chars = [c for c in range(1, size + 1)]
cSize = 1 # Quantos elementos cada combinação deve ter.

printCombinations(chars, cSize)
print(f"São {len(list(combinations(chars, cSize)))} listas.")
