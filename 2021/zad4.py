ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

final_word = ""

def MaxCountValues(array):
    keys = []
    values = []
    
    for e in array:
        if(keys.__contains__(e)):
            id = keys.index(e)
            values[id] += 1
        else:
            keys.append(e)
            values.append(1)
        
    max_val = max(values)
    return [keys[values.index(max_val)], max_val]

def Step(instruction, value, word):
    
    if (instruction == "DOPISZ"):
        word += value
        return word
    elif (instruction == "ZMIEN"):
        list_word = list(word)
        if(len(word) > 0):
            list_word[-1] = value    
        return "".join(list_word)
    elif (instruction == "USUN"):
        list_word = list(word)
        if(len(word) > 0):
            list_word.pop()
        return "".join(list_word)
    elif (instruction == "PRZESUN"):
        i = 0
        while word[i] != value:
            i += 1
        else:
            char_id = ALPHA.index(word[i])
            list_word = list(word)
            if(char_id == len(ALPHA) - 1):
                list_word[i] = ALPHA[0]
            else:
                list_word[i] = ALPHA[char_id + 1]
            word = "".join(list_word)
        return word
    else:
        return Exception("Wrong instruction")

file = open("instrukcje.txt", "r+")
i_set = []

for inst in file.readlines():
    i_set.append(inst.strip().split(" "))
    
file.close()

inst_counter = 0
inst_memory = i_set[0][0]

memory = []
counter = []

append_inst_value = []

for instruction_value in i_set:
    
    if(instruction_value[0] != inst_memory):
        memory.append(inst_memory)
        counter.append(inst_counter)
        inst_counter = 1
        inst_memory = instruction_value[0]
    else:
        inst_counter += 1 
        
    if instruction_value[0] == "DOPISZ":
        append_inst_value.append(instruction_value[1])
    
    final_word = Step(instruction_value[0], instruction_value[1], final_word)

print("4.1. {}".format(len(final_word)))

print("4.2. rodzaj instrukcji - {}, długość ciągu - {}".format(memory[counter.index(max(counter))], max(counter)))

print("4.3. litera {}, dopisywana {} razy".format(MaxCountValues(append_inst_value)[0], MaxCountValues(append_inst_value)[1]))

print("4.4. {}".format(final_word))
