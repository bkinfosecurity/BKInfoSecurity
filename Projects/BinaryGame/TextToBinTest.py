import random as rnd
import difflib

def MakeList():
    textArr = [""]
    file = open("words_alpha.txt", "r")
    for line in file:
        textArr.append(line.strip())

    print(len(textArr))
    Main(0, textArr)


def Main(score, textArr):
  #  textArr = ["time","year","people","way","day","man","thing","woman","life","child","world","school","state","family","student","group","country","problem","hand","part","place","case","week","company","system","program","question","work","government","number","night","point","home","water","room","mother","area","money","story","fact","month","lot","right","study","book","eye","job","word","business","issue","side","kind","head","house","service","friend","father","power","hour","game","line","end","member","law","car",
  #         "city","community","name","president","team","minute","idea","kid","body","information","back","parent","face","others","level","office","door","health","person","art","war","history","party","result","change","morning","reason","research","girl","guy","moment","air","teacher","force","education"]

    testString = textArr[rnd.randint(0, len(textArr))]
    byte_array = testString.encode()


    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)



    ans1 = int(input("1 - Text to Bin\n2 - Bin to Text\n->"))
    if ans1 == 1:
        TextToBin(binary_string, testString, score, textArr)
    elif ans1 == 2:
        BinToText(binary_string, testString, score, textArr)


def TextToBin(binary_string, testString, score, textArr):
    testAns = input("What is the binary form of \"" + testString + "\"\n")

    binary_string = binary_string.replace("b","")
    binary_string = binary_string.strip()

    for i in range(0, len(binary_string) + (int(len(binary_string)/9))):
        if i % 9 == 0:
            binary_string = binary_string[:i] + " " + binary_string[i:]
    
    
    if testAns == binary_string.strip():
        score+=1
        print("\nCorrect!\nScore = %d" %score)
    else:
        print("\nIncorrect, the correct answer was \n" + binary_string)
    Main(score, textArr)

def BinToText(binary_string, testString, score, textArr):

    binary_string = binary_string.replace("b","")

    for i in range(0, len(binary_string) + (int(len(binary_string)/9))):
        if i % 9 == 0:
            binary_string = binary_string[:i] + " " + binary_string[i:]
    
    testAns = input("What is the text form of " + binary_string + "\n")
    if testAns == testString:
        score+=1
        print("\nCorrect!\nScore = %d" %score)
        
    else:
        
        print("\nIncorrect, the correct answer was \n" + testString)
    Main(score, textArr)

MakeList()
