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

def wordHasAPathInGrid(grid:list, word:str) -> bool:
    for row in range(4):
        for col in range(4):
            if grid[row][col] == word[0]:
                return lookForPath(grid, [], row, col, word[1:])

def lookForPath(grid:list, visitedCoords:list, rowCoord:int, colCoord:int, wordFragment:str) -> bool:
    visitedCoordsCopy = visitedCoords.copy() # FIX THIS 
    visitedCoordsCopy.append((rowCoord,colCoord))
    for rowIndex in range(rowCoord-1,rowCoord+2,1):
        for colIndex in range(colCoord-1,colCoord+2,1):
            if (0 <= rowIndex < 4) and (0 <= colIndex < 4):
                if (rowIndex, colIndex) not in visitedCoordsCopy:
                    if grid[rowIndex][colIndex] == wordFragment[0]: # found a adjascent spot with next letter
                        return True if len(wordFragment) == 1 else lookForPath(grid, visitedCoordsCopy, rowIndex, colIndex, wordFragment[1:])
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
    given = getInputLetters(16)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÍÁÓÑÜÉÚ"
    charList = list(given.upper())
    grid = [charList[i:i+4] for i in range(0,16,4)]
    unusedLetters = ''.join([letter for letter in alphabet if letter not in charList])
    wordList = []
    with open("dictionaries/englishFull.txt",'r', encoding='utf-8') as textFile:
        for word in textFile:
            word = word.strip() # get rid of that \n
            if len(word) >= 3:
                if not badLettersInWord(unusedLetters, word):
                    if not wordHasTooManyOfALetter(charList, word):
                        if wordHasAPathInGrid(grid, word):
                            wordList.append(word)
    sortedList = mergeSort(wordList)
    print(sortedList)

if __name__=="__main__": 
    main()

# accents = ÍÁÓÑÜÉÚ