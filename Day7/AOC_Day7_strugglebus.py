prev_dirs = [];
cur_dir   = '';
cur_cmd   = '';
filesystem = {}
lines  = [line.rstrip() for line in open('Day7/day-7-input.txt')]
for line in lines:
    if line[:1] == "$":
        command = line[2:].split(' ')
        if command[0] == 'cd':
            cur_cmd = 'cd'
            prev_dirs.append(command[1]);
            if filesystem == {}:
                filesystem[command[1]] = []
            elif command[1] not in filesystem[cur_dir]:
                filesystem[cur_dir].append({command[1]:[]})        
            cur_dir = command[1]
        if command[0] == 'ls':
            cur_cmd = 'ls'
        if command[0] == '..':
            cur_dir = prev_dirs.pop()
    elif cur_cmd == 'ls':
        dir_ls_line = line.split(' ')
        if dir_ls_line[0] == 'dir':
            dir_ls_line[1]
#            if dir_ls_line[1] in filesystem[cur_dir]:
#                filesystem[cur_dir].append({dir_ls_line[1]:[]})
            if dir_ls_line[1] not in filesystem[cur_dir]:
                filesystem[cur_dir].append({dir_ls_line[1]:[]})
       # else:
       #     filesystem[cur_dir].append({dir_ls_line[1]:dir_ls_line[0]})
print(filesystem)
    #else:
    #    print(line)