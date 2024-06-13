def lexer(contents): 
    lines = contents.split("\n")
    keywords = ["helloWorld"]
    print(lines)

    for line in lines:
        
        if "'" in line or '"' in line:
            sentence = []
            for i in range(36):
                word = ""
                end_line = False
                if end_line:
                    break

                for letter in line:
                    if letter == line[-1]:
                        end_line = True
                    elif letter == " ":
                        break
                    else:
                        word +=letter
                x =line.replace(word, "")
                print(x)
                sentence.append(word)
            print(sentence)               

                
   
        

        
       

def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens