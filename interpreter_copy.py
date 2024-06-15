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
    for line in lines:
        for letter in line:
            if letter in ["(", ")", '"', "'"] and word:
                if word in keywords:
                    object_[word] = keywordsObject_[word]
                    sentence.append(word)
                else:
                    object_[word] = {"type": "undefinited",}
                    sentence.append(word)
                word = letter
                object_[word] = {"type": "undefinited",}
                sentence.append(word)
                word = ""
            elif letter in ["(", ")", '"', "'"] and not word:
                word += letter
                object_[word] = {"type": "undefinited",}
                sentence.append(word)
                word=""
            else:
                word += letter
        print(sentence)
        sentence.clear()
    print(object_)
def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens