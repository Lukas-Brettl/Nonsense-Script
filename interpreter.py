import functions

object_ = {}

keywordsObject_ = {
    "helloWorld": {
        "type": "buildInFunction",
        "codeValue": "helloWorld",
        "todo": "printToConsole",
        "discription": "function to print something to terminal"
    },
    "print": {
        "type": "keywordVariable",
        "codeValue": "print",
        "discription": "This keyword declare variable"
    },
}

keywords = ["helloWorld", "print"]

def lexer(contents): 
    lines = contents.split("\n")
    
    sentence = []
    
    word = ""
    numLine = 1

    #algorithm to split key words
    for line in lines:
        object_["line" + str(numLine)] = {}
        
        #for exery letter in line
        for letter in line:

            #if letter in key word and is something in word then add word and the letter to sentence
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
            #if letter in key word and it's nothing in word then add letter to word and then add word to sentence
            elif letter in ["(", ")", '"', "'", ","] and not word:
                word += letter
                object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = {"type": "undefinited", "codeValue": word}
                sentence.append(word)
                word=""

            #if last letter in line add to word and then word add to sentence
            elif letter == line[-1]:
                word += letter
                sentence.append(word)
                object_["line" + str(numLine)][str(numLine) + str(len(sentence))] = {"type": "undefinited", "codeValue": word}
                word = ""
            #if nothing else work add letter to word
            else:
                word += letter

        #print split sentence
        print(sentence)
        startSting = ""
        endString = ""
        
        #call imported modul
        f = functions.Functions()

        #if ' or " in sentence 
        if "'" in sentence or '"' in sentence:
            stringsIndex = f.getIndexs(sentence, ["'", '"'])


            trueI = 0
            if len(stringsIndex) % 2 == 0:
                for i in range(int((len(stringsIndex)/2))):
                    object_["line" + str(numLine)][str(numLine) + str(stringsIndex[trueI] + 1)]["type"] = "string"
                    trueI +=2
            elif len(stringsIndex) % 2 == 1:
                print("Error on line" + numLine)
                exit()
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
                        print(object_["line" + str(numLine)][str(numLine) + str(sentence.index(printt) + 1)]["equalTo"])
                    else:
                        var += i
            
        for i in sentence:
            functionIndex = sentence.index(i)
            editSentence = sentence[functionIndex + 1:]
            try: 
                if object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]:
                    if object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]["type"] == "buildInFunction":
                        print("nice")
                        f.buildFunction(sentence, object_, numLine, editSentence)
                    elif object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]["type"] == "keywordVariable":
                        functionIndex = sentence.index(i)
                        editSentence = sentence[functionIndex + 1:]
            except:
                pass
            try:
                if object_["line" + str(numLine)][str(numLine) + str(sentence.index(i) + 1)]:
                    if object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]["type"] == "buildInFunction":
                        print("nice")
                        f.buildFunction(sentence, object_, numLine, editSentence)
                    elif object_["line" + str(numLine)][str(numLine) + str(sentence.index(i))]["type"] == "keywordVariable":
                        functionIndex = sentence.index(i)
                        editSentence = sentence[functionIndex + 1:]
            except:
                pass

        
        numLine += 1
        sentence.clear()
        
    print(object_)
def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens