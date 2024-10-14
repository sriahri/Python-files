f = open('E:/idledoc/hw4.txt','r')
l = f.readlines()
wayne_state_scores = []
others_scores = []
n = len(l)
for i in range(n):
    x = l[i].split(':')
    wayne_state_scores.append(int(x[2]))
    others_scores.append(int(x[4]))
win = 0
for i in range(n):
    if wayne_state_scores[i] > others_scores[i]:
        win += 1
print('a : Win - Loss Record is',win, n-win)
print()
average_wayne_score = sum(wayne_state_scores)/n
average_other_scores = sum(others_scores)/n
print('b : The average score of Wayne state is',average_wayne_score)
print('b : The average score of other states is',average_other_scores)
print()
winning_margin = 0
losing_margin = 0
for i in range(n):
    if wayne_state_scores[i] > others_scores[i]:
        winning_margin += wayne_state_scores[i] - others_scores[i]
    else:
        losing_margin += others_scores[i] - wayne_state_scores[i]
print('c : The average wiining margin is', winning_margin/n)
print()
print('d : The average losing margin is', losing_margin/n)
print()
print(wayne_state_scores)
print(others_scores)
largest_win = 0
worst_defeat = 0
for i in range(n):
    if wayne_state_scores[i] > others_scores[i] :
        if wayne_state_scores[i] - others_scores[i] > largest_win:
            largest_win = wayne_state_scores[i] - others_scores[i]
    else:
        if others_scores[i] - wayne_state_scores[i] > worst_defeat :
            worst_defeat = others_scores[i] - wayne_state_scores[i]
print('e : The biggest win is with a margin of',largest_win)
print()
print('f : The worst defetat is with a margin of',worst_defeat)