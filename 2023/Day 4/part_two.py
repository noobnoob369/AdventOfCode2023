import os, sys, re

def getPuzzleInput(Input):
    with open(Input, "r", encoding="utf-8") as f:
        data = f.read().splitlines()
        return data

def processInputData(lines):
    #Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    buffer = lines.split(":")
    CardID = buffer[0]
    CardID = CardID.replace("Card ", "")
    buffer = buffer[1].split("|")
    WinningNumbers = buffer[0].rstrip().strip()
    WinningNumbers = WinningNumbers.split(" ")
    WinningNumbers[:] = [item for item in WinningNumbers if item != '']
    CardNumbers = buffer[1].rstrip().strip()
    CardNumbers = CardNumbers.split(" ")
    CardNumbers[:] = [item for item in CardNumbers if item != '']
    return WinningNumbers, CardNumbers
    
    
   

def calculateWinningNumbers(WinningNumbers, CardNumbers):
    CardValue = 0
    for cn in CardNumbers:
        for wn in WinningNumbers:
            if(cn == wn):
                CardValue += 1
                  
    if(CardValue > 0):    
        CardValue = pow(2, CardValue-1)

    return CardValue 
    
    
if __name__ == "__main__":
    
    result = 0
    
    file_name = os.path.join(sys.path[0], "input_one.txt")
    data = getPuzzleInput(file_name)
    for lines in data:
        WinningNumbers, CardNumbers = processInputData(lines)
        result += calculateWinningNumbers(WinningNumbers, CardNumbers )
        
    print(result)