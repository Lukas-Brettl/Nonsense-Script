class Functions:
    def getIndexs(self, content, value):
        result = []
        valueIndex = 0
        for i in content:
            if i in value:
                result.append(valueIndex)
            valueIndex+=1
        return result
    def printToConsole(toPrint):
        print(toPrint)

    def buildFunction(self, sentence, object_, numLine, editSentence):
        leftCall = editSentence.index("(")
        rightCall = editSentence.index(")")

        valueRange = editSentence[leftCall + 1:rightCall]

        for value in valueRange:
            if value in [" ", ",", "'", '"']:
                continue        
            else:
                isPrinted = False
                valueType = ""
                adressRange = len(sentence)
                for i in range(adressRange + 1):
                    
                    
                    try:
                        if object_["line" + str(numLine)][str(numLine) + str(i)]["type"] == "variable":
                            valueType = "variable"
                            print("lllkkkkkkkkkkkkkkkkkkkkkkkkk")
                    except:
                        pass
                for key, thelines in object_.items():
                    for keyadress, adress in thelines.items():
                        if valueType == "variable"  and adress["equalTo"] and adress["type"] == "variable":
                            Functions.printToConsole(adress["equalTo"])
                            
                            isPrinted = not isPrinted
                            continue
                if isPrinted:
                    Functions.printToConsole(adress["equalTo"])

