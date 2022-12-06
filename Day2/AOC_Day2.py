score = 0
optimized_score = 0;
battle = {'B X':1,'A X':4,'C X':7,'C Y':2,'B Y':5,'A Y':8,'A Z':3,'C Z':6,'B Z':9}
optimized_battle = {'B X':1,'A X':3,'C X':2,'C Y':6,'B Y':5,'A Y':4,'A Z':8,'C Z':7,'B Z':9}

strat_lines = [line.rstrip() for line in open('Day2/day-2-input.txt')]
for i in strat_lines:
    score += battle[i]
    optimized_score += optimized_battle[i]
print(score)
print(optimized_score)