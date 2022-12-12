lines  = [line.rstrip() for line in open('Day7/day-7-input.txt')]
prev_dirs = []
dirs = {}

#For each line in the input 
for line in lines:
    #Check if we're moving into a directory
    if line[:4] == '$ cd':
        #if we are, get the directory we're moving to
        dir = line.split()[-1]
        #if .. changing directories, update the file path by removing the last dir
        #otherwise add the new dir to the filepath
        if(dir == '..'):
            prev_dirs.pop()
        else:
            prev_dirs.append(dir)
    elif line[:1] != '$' and line[:3] != 'dir':
        #If the line is a file, get the size
        total_size = int(line.split()[0])
        #For each directory in the filepath, add a record of that file with the appropriate filesize
        for i, dir in enumerate(prev_dirs):
            filepath = '/'.join(prev_dirs[:i+1])
            if(filepath[:2] == '//'):
                filepath = filepath[1:]
            if filepath not in dirs:
                dirs[filepath] = 0  
            dirs[filepath] += total_size
#For each key value pair (filepath + size) if < 100000 add the values
#then for each directory in the path, add the filesize to the dir total

#Setup values for summing all dirs < 100000 pt1 and finding best dir pt2
#Neet to determine the required space for the install requred - (total disk space - /)
pt_1 = 0
required_space = 30000000 - (70000000 - dirs['/'])
best_dir  = { "name":"", "value":0 };
for key, value in dirs.items():
    if value <= 100000:
        pt_1 += value
    if value > required_space:
        if value < best_dir['value'] or best_dir['value'] == 0:
            best_dir['name']  = key
            best_dir['value'] = value

print('pt1:',pt_1)
print('pt2: ',best_dir['name'],best_dir['value'])