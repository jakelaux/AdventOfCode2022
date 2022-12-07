from collections import Counter
def fixmyphone(chunk):
    input  = ''.join([line.rstrip() for line in open('Day6/day-6-input.txt')])
    buffer = input[0:chunk]
    input  = input[chunk:]
    garbo  = ''
    #for each character 
    for char in input:
        num_uniq = len(Counter(buffer))
        if num_uniq == len(buffer):
            return len(garbo)+len(buffer)
        else:
            first_char = buffer[0]
            buffer = buffer[1:]
            buffer += char
            garbo += first_char

print(fixmyphone(4))
print(fixmyphone(14))