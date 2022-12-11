import json

def getChildren(dirs, parent):
    children = []
    d_keys = dirs.keys()
    for k in d_keys:
        if dirs[k]['parent'] == parent:
            children.append(k)
    return children

lines  = [line.rstrip() for line in open('Day7/day-7-input.txt')]
prev_dirs = []
dirs = {};
cur_dir = '';
cur_cmd = ''; 

#for each line
for i, line in enumerate(lines):
    #check if the line is a command
    if line[:1] == "$":
        command = line[2:].split(' ')
        cur_cmd = command[0]
        #if it's a cd, set current command
        if cur_cmd == 'cd':
            parent = ''
            #if there are any previous directories, there's a parent
            if(len(prev_dirs) > 0):
                parent = prev_dirs[-1]
            #if the command is .. remove current dir from prev dirs
            #elif the dir is not in dirs yet (and it's not ..) add it to dirs
            #else add the dir to prev dirs as we're moving into it
            if command[1] == '..':
                cur_dur = prev_dirs.pop()
                continue
            elif command[1] not in dirs and command[1] != '..':
                cur_dir = command[1]
                dirs[command[1]] = {"parent":parent,'content':[],'name':command[1]}
                prev_dirs.append(command[1])
            else:
                prev_dirs.append(command[1])
        elif command[0] == 'ls':
            cur_cmd = 'ls'
    elif cur_cmd == 'ls':
        ls_line = line.split(' ')
        if ls_line[0] != 'dir':
            dirs[cur_dir]['content'].append({"size":ls_line[0],"file":ls_line[1]})
for dir in dirs:
    children = getChildren(dirs,dir)
    if(children != []):
        dirs[dir]['children'] = children
pt1_arr = []
total_pt1 = 0

def buildFilesystem(dirs, parent):
    global total_pt1,pt1_arr
    filesystem = {}
    filesystem[parent] = {}
    filesystem[parent]['size'] = 0
    #If there are files, add to the filesize
    if 'content' in dirs[parent]:
        for file in dirs[parent]['content']:
            filesystem[parent]['size'] += int(file['size'])
    print(parent,filesystem[parent]['size'])
    #If there are children, insert to children, recursively call function
    #and then update teh size for the parent to include the size of the child
    if 'children' in dirs[parent]:
        filesystem[parent]['children'] = []
        for child in dirs[parent]['children']:
            subdir = buildFilesystem(dirs, child)
            filesystem[parent]['children'].append(subdir)
            filesystem[parent]['size'] += int(subdir[child]['size'])
    print(parent,filesystem[parent]['size'])
    pt1_arr.append([parent,filesystem[parent]['size']])
    return filesystem
directory_tree = buildFilesystem(dirs,'/')

add_string = '';
for dir in pt1_arr:
     if dir[1] <= 100000:
        total_pt1 += dir[1]

print(json.dumps(directory_tree,indent=1))