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


print("----------")

import string
import random

def secretLanguageEncodeCode(text_string):
    """
    create a secret encoded code for a text_string
    """
    
    alphabet_letters = list(string.ascii_lowercase)
    
    if not text_string:
        return ""
    elif len(text_string) < 3:
        return text_string[::-1]
    else:
        encoded = ""
        text_string = text_string[1:] + text_string[0]
        for index in range(6):
            random_integer_range = random.randrange(0, 26)
            if index == 3:
                encoded += text_string
                encoded += alphabet_letters[random_integer_range]
            else:
                encoded += alphabet_letters[random_integer_range]
                
        return encoded
        
def secretLanguageDecodeCode(text_string):
    """
    create a decode code for a text_string
    """
    
    if not text_string:
        return ""
    elif len(text_string) < 3:
        return text_string[::-1]
    else:
        decoded = ""
        for index in range(3, len(text_string) - 3):
            decoded += text_string[index]
        
        decoded = decoded[-1] + decoded[0:-1]
        return decoded

original = "abcdef"
encoded = secretLanguageEncodeCode(original)
decoded = secretLanguageDecodeCode(encoded)
print("Original string: ", original)
print("Encoded string: ", encoded)
print("Decoded string: ", decoded)

original = "zrtyu"
encoded = secretLanguageEncodeCode(original)
decoded = secretLanguageDecodeCode(encoded)
print("Original string: ", original)
print("Encoded string: ", encoded)
print("Decoded string: ", decoded)

print("----------")

def checkArrDuplicates(arr):
    """
    check if all elements in array are uniques then return false else true
    """
    keys = {
        
    }
    
    for item in arr:
        if item in keys:
            return True
        else:
            keys[item] = 1
    
    return False
    
print("what is the value : ", checkArrDuplicates([1,2,3,1]))
print("what is the value : ", checkArrDuplicates([1,2,3,4]))


print("----------")



text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

def isAnagram(str1, str2):
    """
    check if strings provided are anagram or not
    """
    if(len(str1) != len(str2)):
        return "Not Anagram"
    else:
        count = 0
        for char in str2:
            if(char in str1):
                count += 1
            else:
                return "Not Anagram"
        
        if (count) == len(str1):
            return "Anagram"
        
print(isAnagram(text1, text2))
    
