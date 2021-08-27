scores = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
trumps = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
inp = input().split()
hands = int(inp[0])
trumpHand = inp[1]
score = 0
for i in range(4*hands):
    hand = input()
    score += trumps[hand[0]] if hand[1] == trumpHand else scores[hand[0]]
print(score)