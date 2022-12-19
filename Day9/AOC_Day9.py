#file = 'Day9/day-9-input.txt'
file = 'Day9/day-9-test-input.txt'
movements = open(file).read().splitlines()
rope = [
        ['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['H','.','.','.','.','.'],
]

h_index = [4,0]

for mov in movements:
    mov = mov.split(' ')
    dir = mov[0]
    num = int(mov[1])
    if dir == 'R':
        h_index = [h_index[0],h_index[1]+num]
    elif dir == 'L':
        h_index = [h_index[0],h_index[1]-num]
    elif dir == 'U':
        h_index = [h_index[0]-num,h_index[1]]
    elif dir == 'D':
        h_index = [h_index[0]+num,h_index[1]]
    rope[int(h_index[0])][int(h_index[1])] = 'H'

for line in rope:
    print(line)