#setup garbage pt.1
crates = [["G","F","V","H","P","S"],
["G","J","F","B","V","D","Z","M"],
["G","M","L","J","N"],
["N","G","Z","V","D","W","P"],
["V","R","C","B"],
["V","R","S","M","P","W","L","Z"],
["T","H","P"],
["Q","R","S","N","C","H","Z","V"],
["F","L","G","P","V","Q","J"]]
#setup garbage pt.2
crates_9001 = [["G","F","V","H","P","S"],
["G","J","F","B","V","D","Z","M"],
["G","M","L","J","N"],
["N","G","Z","V","D","W","P"],
["V","R","C","B"],
["V","R","S","M","P","W","L","Z"],
["T","H","P"],
["Q","R","S","N","C","H","Z","V"],
["F","L","G","P","V","Q","J"]]
instructions = [line.rstrip() for line in open('Day5/day-5-input.txt')]
instructions_9001 = [line.rstrip() for line in open('Day5/day-5-input.txt')]
#pt. 1 > split input into tuple move, from, to
#for each crate to move, pop it off from and append to the to
for instruction in instructions:
    mv,frm,to = tuple(int(x) for x in instruction.split())
    i=0
    while i<mv:
        move = crates[frm-1].pop()
        crates[to-1].append(move)
        i+=1
#pt. 2 > split input to tuple move, from, to
#Get move crates by slicing -move from from crates
#Set new value of from to slice off end of arr
#extend to array by move array
for instruction in instructions_9001:
    mv,frm,to = tuple(int(x) for x in instruction.split())
    move = crates_9001[frm-1][-mv:]
    crates_9001[frm-1] = crates_9001[frm-1][:-mv]
    crates_9001[to-1].extend(move)

tops = []
tops_9001 = []
for crate in crates:
    tops.append(crate.pop())
print(''.join(tops))
for crate in crates_9001:
    tops_9001.append(crate.pop())
print(''.join(tops_9001))