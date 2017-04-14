firstInputStr = input()
secondInputStr = input()

index = firstInputStr.find(secondInputStr)

if index == -1:
    print (firstInputStr)
else:
    for i in range(index + len(secondInputStr) + 1, len(firstInputStr)):
        print(firstInputStr[i], end='')