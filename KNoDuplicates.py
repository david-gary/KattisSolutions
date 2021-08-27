phrase = list(map(str, input().split()))
counts = []
for i in phrase:
    counts.append(phrase.count(i))
if max(counts) > 1:
    print("no")
else:
    print("yes")
        
