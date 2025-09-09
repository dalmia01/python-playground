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
            count = count + 1
            
    return count
    
print("Total jewels that are stones : ", findJewelStones("aAA", "aaABBBB"))
print("Total jewels that are stones : ", findJewelStones("z", "ZZ"))
print("Total jewels that are stones : ", findJewelStones(1, 123))
print("Total jewels that are stones : ", findJewelStones(". ", "AA "))
print("Total jewels that are stones : ", findJewelStones("z ZZ", "ZZ Cr"))

print("----------")

def removeDuplicatesWithTrailingPlaceholder(arr, placeholder = "*"):
    """
    return an array which only contains uniques in sorted array
    """
    if (not arr) or len(arr) == 0:
        return []
        
    newArr = [arr[0]]
    count = 0
    for index in range(1, len(arr)):
        if arr[index] in newArr:
            count += 1
        else:
            newArr.append(arr[index])
    
    newArr.extend(placeholder * count)
            
    return newArr
        
print("Remove duplicates array with trailing placeholders : ", removeDuplicatesWithTrailingPlaceholder([0,1,1,1,1,2,2,2,3,3,4]))
print("Remove duplicates array with trailing placeholders : ", removeDuplicatesWithTrailingPlaceholder([]))
print("Remove duplicates array with trailing placeholders : ", removeDuplicatesWithTrailingPlaceholder([1], "_"))
print("Remove duplicates array with trailing placeholders : ", removeDuplicatesWithTrailingPlaceholder([1, 1, 1], "+"))
print("Remove duplicates array with trailing placeholders : ", removeDuplicatesWithTrailingPlaceholder([1, 1, 2, 2, 3, 4, 4], "%"))
