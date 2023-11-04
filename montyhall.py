
# there should be 3 rooms
# one should be the "correct" room
# after picking, eliminate one of the rooms (that is not the "correct room")
# simulate both with switching the success rate and without switching

import random

ans = 0
for i in range(0, 1000):
    choices = [1, 2, 3]
    correct = random.choice(choices)
    guess = random.choice(choices)
    elim = []
    for num in choices:
        if num != correct and num != guess:
            elim.append(num)

    elimchoice = random.choice(elim)
    choices.remove(elimchoice)
    for num in choices:
        if num != guess:
            guess = num
            break

    if guess == correct:
        ans += 1

print('If the player swaps doors, he wins: ' + str(ans / 1000) + ' percent of the time')

ans = 0
for i in range(0, 1000):
    choices = [1, 2, 3]
    correct = random.choice(choices)
    guess = random.choice(choices)

    if guess == correct:
        ans += 1

print('If the player does not swap doors, he wins: ' + str(ans / 1000) + ' percent of the time')
