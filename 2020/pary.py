f = open("./Dane_PR2/pary.txt", "r+")

rows = f.readlines()
pairs = []
for row in rows:
    pairs.append(row.strip().split(" "))

nums = []
words = []

for i in range(len(pairs)):
    pairs[i][0] = int(pairs[i][0])

for pair in pairs:
    nums.append(pair[0])
    words.append(pair[1])

def ComparePairs(pair_a, pair_b): #returns True if pair_a is smaller
    if pair_a[0] < pair_b[0]:
        return True
    elif pair_a[0] == pair_b[0] and pair_a[1] < pair_b[1]:
        return True
    else:
        return False

def first(nums):
    for num in nums:
        if (num % 2 == 0):
            subs = []
            for i in range(2, num):
                for j in range(2, i):
                    if(i % j == 0):
                        break
                else:
                    for x in range(i, num):
                        for y in range(i, x):
                            if(x % y == 0):
                                break
                        else:
                            if(i + x == num):
                                subs.append([i, x, abs(i - x)])
            diffs = []
            for sub in subs:
                diffs.append(sub[2])
            diff_max = max(diffs)
            id_max = diffs.index(diff_max)
            print(f"{num} {subs[id_max][0]} {subs[id_max][1]}")

def second(words):
    for word in words:
        last_char = word[0]
        counter = 1
        chains = []
        
        for i in range(1, len(word)):
            if(word[i] == last_char):
                counter += 1
            else:
                chains.append([last_char, counter])
                last_char = word[i]
                counter = 1
        else:
            chains.append([last_char, counter])
        
        lens = []
        for chain in chains:
            lens.append(chain[1])
        id_max = lens.index(max(lens))
        print(f"{chains[id_max][0] * chains[id_max][1]} {chains[id_max][1]}")

def third(pairs):
    good_pairs = []
    for pair in pairs:
        if pair[0] == len(pair[1]):
            good_pairs.append(pair)

    smallest = good_pairs[0]
    for i in range(1, len(good_pairs)):
        if ComparePairs(smallest, good_pairs[i]) == False:
            smallest = good_pairs[i]
            
    print(f"{smallest[0]} {smallest[1]}")
    

first(nums)
print("===")
second(words)
print("===")
third(pairs)