# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # clean up symbols and convert to lowercase
    word = word.replace("'", "").replace("-","").replace("_","").replace(" ","").lower()
    anagram = anagram.replace("'", "").replace("-","").replace("_","").replace(" ","").lower()
    # check if all letters exist in each both lists, length of characters must be equal
    anagramList= list(anagram)
    wordList = list(word)
    check = False
    if len([i for i in wordList if i != ' ']) == len([i for i in anagramList if i != ' ']):
        check = all([True if i in anagramList else False for i in wordList])

    return check


# Test Anagrams
anagram1 = find_anagrams("below","elbow")
print(anagram1)
anagram2 = find_anagrams("hello", "check")
print(anagram2)
anagram3 = find_anagrams("rescue", "secure")
print(anagram3)
anagram4 = find_anagrams("aide", "idea")
print(anagram4)
anagram5 = find_anagrams("diagnose", "san diego")
print(anagram5)
anagram6 = find_anagrams("a decimal point", "i'm a dot in place")
print(anagram6)
anagram7 = find_anagrams("dynamite", "may it end")
print(anagram7)
anagram8 = find_anagrams("eleven plus two", "twelve plus one")
print(anagram8)
anagram9 = find_anagrams("hitler woman", "mother-in-law")
print(anagram9)