forest = []
file = 'Day8/day-8-test-input.txt'#'Day8/day-8-input.txt'
trees = open(file).read().splitlines()
for i, row in enumerate(trees):
    forest.append(list(row))
rows = len(forest)
cols = len(forest[0])
visible = (rows*2) + (cols*2) - 4
highest = 1

def isVisible(l,r,u,d,tree):
    ml = (max(l)<tree) 
    mr = (max(r)<tree) 
    mu = (max(u)<tree) 
    md = (max(d)<tree)
    return ml or mr or mu or md

def countTrees(comp,tree):
    dir_total = 1
    for c in comp:
        if c < tree:
            dir_total += 1
        elif c <= tree:
            dir_total += 1
            return dir_total
    return dir_total

#updated to use range to skip edges that were included in my original enumerate loop
for row in range(1, rows-1):
    for col in range(1, cols-1):
        tree = forest[row][col]
        #pt1
        #for left, right, up, and down > if the tallest tree in the list is shorter than our tree our tree is visible
        l = [ forest[row][col-i] for i in range(1, col+1)    ]
        r = [ forest[row][col+i] for i in range(1, cols-col) ]
        u = [ forest[row-i][col] for i in range(1, row+1)    ]
        d = [ forest[row+i][col] for i in range(1, rows-row) ]
        if isVisible(l,r,u,d,tree):
            visible += 1
        score = countTrees(l,tree)*countTrees(r,tree)*countTrees(u,tree)*countTrees(d,tree)
        print(score)
        if score > highest:
            highest = score

print("pt1:", visible)
print("pt2: ", highest)