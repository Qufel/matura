file = open("woda.txt")
dane = []
for line in file.readlines():
    arr = line.strip().split("	")
    arr[1] = int(arr[1])
    dane.append(arr)
file.close()
