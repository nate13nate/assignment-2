import re

### open files ###
inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

def getWordcounts(input: str) -> dict[str, int]:
    wordcounts: dict[str, int] = {}

    lowercase = input.lower()
    noSpecialCharacters = re.sub(r'[^a-zA-Z0-9\']+', ' ', lowercase) # removing special characters so that it's only the words, including contractions
    words = noSpecialCharacters.split(' ')

    for word in words:
        if word in wordcounts:
            wordcounts[word] += 1
            continue
        wordcounts[word] = 1
    
    return wordcounts

def wordcountsToString(wordcounts: dict[str, int]) -> str:
    output = ''
    for wordcount in wordcounts.items():
        output += wordcount[0] + ': ' + str(wordcount[1]) + '\n'
    return output

def main():
    input = inputFile.read()
    wordcounts = getWordcounts(input)
    wordcountsStr = wordcountsToString(wordcounts)
    outputFile.write(wordcountsStr)

main()

### close files ###
inputFile.close()
outputFile.close()
