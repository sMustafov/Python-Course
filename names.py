input_str = input().split(' ')

for name in input_str:
    if name[0].upper() == name[0]:
        print(name[0] + '.', end='')