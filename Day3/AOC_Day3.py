sack_sum  = 0;
badge_sum = 0; 
val_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
rucksacks = [line.rstrip() for line in open('Day3/day-3-input.txt')]
for sack in rucksacks:
    left  = sack[:len(sack)//2]
    right = sack[len(sack)//2:]
    intersect = ''.join(set(left).intersection(right))
    sack_sum += val_str.index(intersect)+1
print(sack_sum)

group_arr = []
for sack in rucksacks:
    if len(group_arr) <= 3:
        group_arr.append(sack)
    if len(group_arr) == 3:
        result = set(group_arr[0]).intersection(group_arr[1])
        badge = ''.join(set(result).intersection(group_arr[2]))
        group_arr = []
        badge_sum += val_str.index(badge)+1
print(badge_sum)
        