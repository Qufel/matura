file = open("sygnaly.txt", "r+")
dane = []
for line in file.readlines():
    dane.append(line.strip())
file.close()

def first(dane):
    
    word = ""
    
    i = 39
    while i <= len(dane):
        word += dane[i][9]
        i += 40
        
    return word

print("4.1. {}".format(first(dane)))

def second(dane):
    
    div = []
    count_div = []
    
    for word in dane:
        unique = []
        
        for char in word:
            if char not in unique:
                unique.append(char)

        div.append(unique)
    
    for d in div:
        count_div.append(len(d))
    
    return [dane[count_div.index(max(count_div))], max(count_div)]

print("4.2. {} {}".format(second(dane)[0], second(dane)[1]))

def third(dane):
    
    words = []
    
    for word in dane:
        for i in range(len(word)):
            is_larger = False
            for j in range(len(word)):
                if(abs(ord(word[i]) - ord(word[j])) > 10):
                    is_larger = True
                    break
            if(is_larger):
                break
        else:
            words.append(word)
                
    return words
                
res = third(dane)
print("4.3.")
for r in res:
    print(r)