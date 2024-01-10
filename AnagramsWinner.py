from icecream import ic # ice cream so good, gang gang

def badLettersInWord(unusedLetters:str, word:str) -> bool:
    wordSet = set(word)
    for letter in unusedLetters:
        if letter in wordSet:
            return True #nuh uh
    return False #cool

def wordHasTooManyOfALetter(charList:list, word:str) -> bool:
    copyOfCharList = charList.copy()
    for letter in word:
        if letter in copyOfCharList:
            copyOfCharList.remove(letter)
        else: # ruh roh
            return True #cant be having more of a letter than is in charlist
    return False

def mergeSort(arr:list):
    return arr if len(arr) <= 1 else merge(mergeSort(arr[:len(arr)//2]), mergeSort(arr[len(arr)//2:]))

def merge(left:list, right:list):
    mergedList = []
    leftIndex = rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if len(left[leftIndex]) > len(right[rightIndex]):
            mergedList.append(left[leftIndex])
            leftIndex += 1
        else:
            mergedList.append(right[rightIndex])
            rightIndex += 1
    mergedList += left[leftIndex:] + right[rightIndex:]
    return mergedList

def getInputLetters(length:int):
    given = input("Enter letters as a line: ")
    return given if len(given) == length else getInputLetters(length)

def main():
    given = getInputLetters(6)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÍÁÓÑÜÉÚ"
    charList = list(given.upper())
    unusedLetters = ''.join([letter for letter in alphabet if letter not in charList])
    wordList = []
    with open("dictionaries/spanishSmall.txt",'r', encoding='utf-8') as textFile:
        for word in textFile:
            word = word.strip() # get rid of that \n
            if len(word) >= 3:
                if not badLettersInWord(unusedLetters, word):
                    if not wordHasTooManyOfALetter(charList, word):
                        wordList.append(word)
    sortedList = mergeSort(wordList)
    print(sortedList)

if __name__=="__main__": 
    main() 

# accents = Í Á Ó Ñ Ü É Ú 