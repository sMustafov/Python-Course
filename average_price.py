inputStr = float(input())
list = []

while inputStr != 'stop':
    list.append(float(inputStr))
    inputStr = input()

list.sort()
first = list[0]
last = list[-1]

sum = 0
counter = 0

for i in sorted(list):
    if i != first and i != last:
        sum += i
        counter += 1

if counter > 0:
    average = sum / counter
    print(average)
else:
    print ('No prices')

