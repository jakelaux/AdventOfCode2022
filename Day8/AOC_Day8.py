forest = []
file = 'Day8/day-8-test-input.txt'#'Day8/day-8-input.txt'
trees = open(file).read().splitlines()
for i, row in enumerate(trees):
    forest.append(list(row))
visible = 0
visible = (((len(forest[0])*2) + (len(forest)*2)) - 4)

#def checkVisibile(row, col, tree):
#    print(row,col,tree)
#    global visible
#    l = len(forest[row][:col])-1
#    r = len(forest[row][col:])-1
#    u = len(forest[:row])-1
#    d = len(forest[row:])-1
#    lv = []
#    rv = []
#    uv = []
#    dv = []
#    tree_visible = 0
#    while l > 0:
#        l -= 1
#        if forest[row][l] < tree:
#            lv.append({'comp':forest[row][l],'tree':tree})
#        if len(lv) == l+1:
#            tree_visible += 1
#    while r > 0:
#        r -= 1
#        if forest[row][r] < tree:
#            rv.append(({'comp':forest[row][r],'tree':tree}))
#        if len(rv) == r+1:
#            tree_visible += 1
#    while u > 0:
#        u -= 1
#        if forest[u][col] < tree:
#            uv.append(({'comp':forest[u][col],'tree':tree}))    
#        if uv == u+1:
#            tree_visible += 1
#    while d > 0:
#        d -= 1
#        if forest[d][col] < tree:
#            dv.append(({'comp':forest[d][col],'tree':tree}))
#        if dv == d+1:
#            tree_visible += 1
#    if tree_visible > 0:
#        visible += 1

def checkVisibile(r,c,tree):
    global forest
    l  = len(forest[r][:c])-1
    rt = len(forest[r][c:])-1
    u  = [forest[row][c] for row in range(r)]
    d  = [forest[row][c] for row in range(r+1,len(forest[r]))]
    up    = map(lambda comp: comp < tree, u)
    down  = map(lambda comp: comp < tree, d)
    left  = map(lambda comp: comp < tree, forest[r][:l])
    right = map(lambda comp: comp < tree, forest[r][rt+1:])
    print(up,down,left,right,r,c,tree)
    return up or down or left or right

rows = []
for r, row in enumerate(forest):
    skip = False
    rows.append(row)
    if r == 0 or (r+1) == len(forest):
        continue
    for c, tree in enumerate(row):
        if c == 0 or (c+1) == len(row):
            continue
        if(not checkVisibile(r,c,tree)):
            visible += 1

print(visible)
for r in forest:
    print(r)