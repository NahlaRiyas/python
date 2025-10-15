text=input("Enter text: ").lower().split()
counts={}
for w in text:
    counts[w]= counts.get(w,0) + 1
print(counts)
