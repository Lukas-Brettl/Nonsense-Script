def printToConsole(toPrint):
    print(toPrint)

object_ = {}

keywordsObject_ = {
    "helloWorld": {
        "type": "buildInFunction",
        "codeValue": "helloWord",
        "todo": printToConsole
    }
}

keywords = ["helloWorld"]

def lexer(contents): 
    lines = contents.split("\n")
    
    sentence = []
    word = ""
    numLine = 1
    for line in lines:
        object_["line" + str(numLine)] = {}
        for letter in line:
            if letter in ["(", ")", '"', "'", ","] and word:
                if word in keywords:
                    object_["line" + str(numLine)][word] = keywordsObject_[word]
                    sentence.append(word)

                else:
                    object_["line" + str(numLine)][word] = {"type": "undefinited",}
                    sentence.append(word)
                word = letter
                object_["line" + str(numLine)][word] = {"type": "undefinited",}
                sentence.append(word)
                word = ""
            elif letter in ["(", ")", '"', "'", ","] and not word:
                word += letter
                object_["line" + str(numLine)][word] = {"type": "undefinited",}
                sentence.append(word)
                word=""
            elif letter == line[-1]:
                word += letter
                sentence.append(word)
                object_["line" + str(numLine)][word] = {"type": "undefinited",}
                word = ""
            else:
                word += letter
        

        print(sentence)

        startSting = ""
        endString = ""
        if "'" in sentence:
            for i, element in enumerate(sentence):
                if element == "'" and not startSting:
                    startSting = i
                elif element == "'" and startSting:
                    endString = i

        elif '"' in sentence:
            for i, element in enumerate(sentence):
                if element == '"' and not startSting:
                    startSting = i
                elif element == '"' and startSting:
                    endString = i
        
        if startSting and endString:
            for i in range(startSting + 1, endString):
                object_["line" + str(numLine)][sentence[i]]["type"] = "string"
        
        for i in sentence:
            if object_["line" + str(numLine)][i]["type"] == "buildInFunction":
                functionIndex = sentence.index(i)
                editSentence = sentence[functionIndex + 1:]

                leftCall = editSentence.index("(")
                rightCall = editSentence.index(")")

                valueRange = editSentence[leftCall + 1:rightCall]
                for value in valueRange:
                    if value in [" ", ",", "'", '"']:
                        continue        
                    else:
                        printToConsole(value)
                
                
        numLine += 1
        sentence.clear()
    print(object_)
def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens