file = open("mecz.txt", "r+")
data = file.read()
file.close()

def part1(data):
    c = 0
    m = data[0]
    for match in data:
        if(match != m):
            c += 1
            m = match 

    return c

print(part1(data))

def part2(data):
    a = 0
    b = 0
    
    for match in data:
        a = a + 1 if match == "A" else a
        b = b + 1 if match == "B" else b
        
        if (abs(a - b) >= 3):
            if(a > b):
                if (a >= 1000):
                    return "A {}:{}".format(a, b)
                elif (b >= 1000):
                    return "B {}:{}".format(a, b)
            else:
                if (a >= 1000):
                    return "A {}:{}".format(a, b)
                elif (b >= 1000):
                    return "B {}:{}".format(a, b)
            
print(part2(data))

def part3(data):
    a = []
    b = []
    
    c = 0
    m = data[0]
    
    for match in data:
        if(match != m):
            if(c >= 10):
                if(match == "A"):
                    b.append(c)
                elif(match == "B"):
                    a.append(c)
            c = 1
            m = match
        else:
            c += 1
            
    max_a = max(a)
    max_b = max(b)
    total = len(a) + len(b)
    
    if max_a > max_b:
        return "{} A {}".format(total, max_a)
    else:
        return "{} B {}".format(total, max_b)
    
print(part3(data))