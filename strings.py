inputStr = input()

if len(inputStr) < 10:
    print(inputStr)
else:
    for i in range(0, 10):
        print(inputStr[i],end='')
    print('...')
