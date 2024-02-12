file = open("2019/liczby.txt", "r+")
nums = []

def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n - 1)

def NWD(a, b):
    return NWD(b, a%b) if b else a

for row in file.readlines():
    nums.append(int(row.strip()))

# print(nums)

def zad1(array):
    counter = 0
    for num in array:
        n = 0
        while(num >= pow(3,n)):
            if(num == pow(3,n)):
                counter += 1
                break
            n += 1
    print(counter)

def zad2(array):
    for num in array:
        text = str(num)
        sum = 0
        for chr in text:
            sum += fact(int(chr))
        
        if(num == sum):
            print(num)

def zad3(array):
    max_sequence = []
    max_nwd = 0
    
    for i in range(len(array) - 1):
        sequence = [array[i]]
        nwd = 0
        nwd_memory = 0
        for j in range(i,len(array)):
            nwd_memory = nwd
            if(nwd == 0):
                nwd = NWD(array[j], array[j + 1])
            else:
                nwd = NWD(nwd, array[j + 1])
                
            if(nwd > 1):
                sequence.append(array[j+1])
            else:
                if(len(sequence) >= len(max_sequence)):
                    max_sequence = sequence
                    max_nwd = nwd_memory
                print(sequence)
                break
    
    print("pierwsza liczba ciągu {first}, długość {len}, największy wspólny dzielnik {max}".format(first = max_sequence[0], len = len(max_sequence), max = max_nwd))
    
# zad1(nums)
# zad2(nums)
zad3(nums)