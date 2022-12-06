contains = 0
contains_at_all = 0
cleanup = [line.rstrip() for line in open('Day4/day-4-input.txt')]
for task in cleanup:
    e1,e2 = task.split(",")
    se1,ee1 = e1.split("-")
    se2,ee2 = e2.split("-")
    if(int(se1)<=int(se2) and int(ee2)<=int(ee1) or 
    int(se2)<=int(se1) and int(ee1)<=int(ee2)):
        contains+=1
    if not(int(ee1)<int(se2) or int(ee2)<int(se1)):
        contains_at_all+=1
        
print(contains)
print(contains_at_all)