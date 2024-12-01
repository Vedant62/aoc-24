with open("aoc_1.txt") as file:
    arr1 = []
    arr2 = []
    dist = 0
    allLines = file.readlines()
    total = 0
    for line in allLines:
        ads = line.split("   ")
        a, b = int(ads[0]), int(ads[1].strip("\n"))
        arr1.append(a)
        arr2.append(b) 
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        dist += abs(arr1[i]-arr2[i])
    for num in arr1:
        total+= num*arr2.count(num)
    print("(1)",dist)
    print("(2)",total)