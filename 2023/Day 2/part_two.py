import re, sys, os

max_dict = {'blue':14, 'green':13, 'red':12}      

def power(line):
    myList = re.split(':', line)
    tries =  re.split(';', myList[1])
    power = 1
    max_val = 0
    for x in max_dict:
        for one_try in tries:
            for y in one_try.split(','):
                if y.split()[1] == x and int(y.split()[0]) > max_val:
                    max_val = int(y.split()[0])
                   
        power = power * max_val
        max_val = 0
    
    return power
    

file_name = os.path.join(sys.path[0], "input_two.txt")
file1 = open(file_name, 'r')
sum_of_all = 0

while True:
    line = file1.readline()
    
    if not line:
        break
        
    sum_of_all += power(line)
    
print(f"Sum of all possible games : {sum_of_all}") 