forest  = []
trees   = [line.rstrip() for line in open('Day8/day-8-input.txt')]
count   = 0;
for i, row in enumerate(trees):
    forest.append(list(row))
visible = (((len(forest[0])*2) + (len(forest)*2)) - 4)

def checkTree(index,tree,index_setter,dir):
    is_visible = True
    i=index_setter
    while i >= 0:
        i-=1
        comp_tree = 0
        if dir=='updown':
            comp_tree = forest[index][i]
        elif dir=='leftright':
            comp_tree = forest[i][index]
        if tree <= comp_tree:
            continue
        else:
            is_visible = False
            break
    return is_visible

def checkVisibile(row,column,tree):
    if checkTree(column,tree,column-1,'updown') or checkTree(column,tree,len(forest)-column-1,'updown') or checkTree(row,tree,row-1,'leftright') or checkTree(row,tree,len(forest[0])-row-1,'leftright'):
        return True
    return False

for i, row in enumerate(forest):
    if i == 0 or (i+1) == len(forest):
        continue
    for j, tree in enumerate(row):
        if j == 0 or (j+1) == len(row):
            continue
        elif checkVisibile(i,j,tree):
            visible += 1

            
print(visible)