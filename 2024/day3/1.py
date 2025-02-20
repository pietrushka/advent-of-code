f = open("day3/data.txt", "r")
data = f.read()

def convert(num):
    try:
        number = int(num)
        return number
    except ValueError:
        return None

total = 0

mul_active = True

# mul
mul_check = False
active = False
prefix = []
num1 = []
hasComma = False
num2 = []

# start/stop
command_tmp = []

for char in data:
    if not mul_check:
        if(char == 'd'):
            command_tmp.append(char)
            continue

        if(len(command_tmp) == 1 and char == 'o'):
            command_tmp.append(char)
            continue

        if(len(command_tmp) == 2 and char == '('):
            command_tmp.append(char)
            continue
        
        if(len(command_tmp) == 3 and char == ')'):
            command_tmp = []
            mul_active = True
            continue

        if(len(command_tmp) == 2 and char == 'n'):
            command_tmp.append(char)
            continue

        if(len(command_tmp) == 3 and char == "'"):
            command_tmp.append(char)
            continue
        
        if(len(command_tmp) == 4 and char == "t"): 
            command_tmp = []
            mul_active = False
            continue

    if mul_active:
        if len(prefix) == 0 and char == 'm':
            mul_check = True
            prefix.append(char)
        elif len(prefix) == 1 and char == 'u':
            prefix.append(char)
        elif len(prefix) == 2 and char == 'l':
            prefix.append(char)
        elif len(prefix) == 3 and char == '(':
            prefix.append(char)
        elif len(prefix) == 4 and not hasComma and type(convert(char)) == int: 
            num1.append(char)
        elif len(prefix) != 0 and char == ',':
            hasComma = True
        elif hasComma == True and type(convert(char)) == int:  
            num2.append(char)
        elif len(num2) != 0 and char == ')':
            total += int(''.join(num1)) * int(''.join(num2))

            mul_check = False
            prefix = []
            num1 = []
            hasComma = False
            num2 = []
        else:
            mul_check = False
            prefix = []
            num1 = []
            hasComma = False
            num2 = []

print(total)