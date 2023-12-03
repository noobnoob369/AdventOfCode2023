import re, os, sys

max_dict = {'blue':14, 'green':13, 'red':12}

def check_max(tries):
    for one_try in tries:
        for x in one_try.split(','):
            if int(x.split()[0]) > max_dict[x.split()[1]]: 
                return False
    return True        

def gameNumber(line):
    game_number = 0
    myList = re.split(':', line)
    tries =  re.split(';', myList[1])
    if(check_max(tries)):
        game_number = [int(str1) for str1 in myList[0].split() if str1.isdigit()][0]
    return game_number

file_name = os.path.join(sys.path[0], "input_one.txt")
file1 = open(file_name, 'r')
sum_of_all = 0

while True:
    line = file1.readline()
    
    if not line:
        break
        
    sum_of_all += gameNumber(line)
    
print(f"Sum of all possible games : {sum_of_all}") 