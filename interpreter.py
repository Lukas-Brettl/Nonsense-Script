def printToConsole(toPrint):
    print(toPrint)

object_ = {}

keywordsObject_ = {
    "helloWorld": {
        "type": "buildInFunction",
        "codeValue": "helloWorld",
        "todo": printToConsole,
        "discription": "function to print something to terminal"
    },
    "print": {
        "type": "keywordVariable",
        "codeValue": "print",
        "discription": "This keyword declare variable"
    },
}

varList = {}

keywords = ["helloWorld", "print"]

def lexer(contents): 
    lines = contents.split("\n")
    
    sentence = []
    
    word = ""
    numLine = 1
#algorithm to split line with key words
    for line in lines:
        object_["line" + str(numLine)] = {}
        
        for letter in line:

            if letter in ["(", ")", '"', "'", ","] and word:
                if word in keywords:
                    object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = keywordsObject_[word]
                    sentence.append(word)
                    

                else:
                    object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = {"type": "undefinited", "codeValue": word}
                    sentence.append(word)
                word = letter
                object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = {"type": "undefinited", "codeValue": word}
                sentence.append(word)
                word = ""
            elif letter in ["(", ")", '"', "'", ","] and not word:
                word += letter
                object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = {"type": "undefinited", "codeValue": word}
                sentence.append(word)
                word=""
            elif letter == line[-1]:
                word += letter
                sentence.append(word)
                object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = {"type": "undefinited", "codeValue": word}
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
                
                object_["line" + str(numLine)][str(numLine) + str(i)]["type"] = "string"
        for printt in sentence:
            if "print" in printt and object_["line" + str(numLine)][str(numLine) + str(sentence.index(printt) + 1)]["type"] == "undefinited":
                
                sentenceForVariable = printt[sentence.index(printt) +5 :]
                var = ""
                for i in sentenceForVariable:
                    if i == " ":
                        continue
                    elif i == "+" or i == "-":
                        varValue = sentenceForVariable.replace(var, "")
                        varValue = varValue.replace(i, "")
                        varLength = len(var)
                        varResult = ""
                        if i == "+":
                            varResult = varLength + int(varValue)
                        elif i == "-":
                            varResult = varLength - int(varValue)

                        object_["line" + str(numLine)][str(numLine) + str(sentence.index(printt) + 1)] = {
                            "type": "variable",
                            "codeValue": var,
                            "equalTo": varResult,
                            "discription": "This is variable"
                        }
                        varList[str(var)] = varResult
                        
                    else:
                        var += i
            
        for i in sentence:
            try:
                if object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]["type"] == "buildInFunction":
                    
                    functionIndex = sentence.index(i)
                    editSentence = sentence[functionIndex + 1:]
                    leftCall = editSentence.index("(")
                    rightCall = editSentence.index(")")

                    valueRange = editSentence[leftCall + 1:rightCall]

                    for value in valueRange:
                        if object_["line" + str(numLine)][str(numLine) + str(sentence.index(value))]["type"] == "string":
                            printToConsole(str(value))
                        elif object_["line" + str(numLine)][str(numLine) + str(sentence.index(value))]["type"] == "undefinited" and value in varList:
                            
                            printToConsole(varList[value])
                    '''for value in valueRange:
                        if value in [" ", ",", "'", '"']:
                            continue        
                        else:
                            isPrinted = False
                            valueType = ""
                            adressRange = len(sentence)
                            for i in range(adressRange + 1):
                                try:
                                    if object_["line" + numLine][str(numLine + i)]["type"] == "variable":
                                        valueType = "variable"
                                        print("lll")
                                except:
                                    pass
                            for key, thelines in object_.items():
                                for keyadress, adress in thelines.items():
                                    if valueType == "variable"  and adress["equalTo"] and adress["type"] == "variable":
                                        printToConsole(adress["equalTo"])
                                        isPrinted = not isPrinted
                                        continue
                            if isPrinted:
                                printToConsole(value)
                elif object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]["type"] == "keywordVariable":
                    functionIndex = sentence.index(i)
                    editSentence = sentence[functionIndex + 1:]'''
            except:
                pass
        
        numLine += 1
        sentence.clear()
        
    print(object_)
def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens