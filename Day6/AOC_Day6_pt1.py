from collections import Counter

input  = ''.join([line.rstrip() for line in open('Day6/day-6-input.txt')])
setup  = input
buffer = input[0:4]
input  = input[4:]
garbo  = ''
#for each character 
for char in input:
    num_uniq = len(Counter(buffer))
    if num_uniq == len(buffer):
        print(len(garbo)+len(buffer))
        break
    else:
        first_char = buffer[0]
        buffer = buffer[1:]
        buffer += char
        garbo += first_char