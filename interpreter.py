def consolePrint(str_):
    print(str_)
    

def lexer(contents): 
    lines = contents.split("\n")
    keywords = {
        'helloWorld': consolePrint
    }
    
    code = []
    for line in lines:
        if line == '':
            continue
        sentence = []
        word = ""
        str_start = False
        str_ = ""
        if "'" in line or '"' in line:
            for letter in line:
                if str_start:
                    if letter in ["'", '"']:
                        str_start = False
                        sentence.append(word)
                        word = ""
                        
                    else:
                        word += letter
                        str_ += letter
                else:
                    if letter in ["'", '"']:
                        if word:
                            sentence.append(word)
                            word = ""
                        str_start = True
                    elif letter in ["(", ")", " "]:
                        if word:
                            sentence.append(word)
                            word = ""

                    else:
                        word += letter

            if word:
                sentence.append(word)

        else:
            sentence.append(line.split())

        word=""
        
        for word_ in sentence:
            if word_ in keywords:
                function_ = keywords[word_]
                function_(str_)
            
        code.append(sentence)
        
    
            


def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens