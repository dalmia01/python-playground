def findJewelStones(jewels, stones):
    """
    Counts how many jewels are stones in a string.
    """
    if (not isinstance(jewels, str)) or (not isinstance(stones, str)) or (len(jewels.strip()) <= 0) or (len(stones.strip()) <= 0):
        return 0
    
    count = 0
    jewels = jewels.strip()
    stones = stones.strip()
    for char in jewels:
        if char in stones:
            count = count + 1;
            
    return count
    
print("Total jewels that are stones : ", findJewelStones("aAA", "aaABBBB"))
print("Total jewels that are stones : ", findJewelStones("z", "ZZ"))
print("Total jewels that are stones : ", findJewelStones(1, 123))
print("Total jewels that are stones : ", findJewelStones(". ", "AA "))
print("Total jewels that are stones : ", findJewelStones("z ZZ", "ZZ Cr"))
