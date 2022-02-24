counts = dict()
line = input("Enter txt:\n")
words = line.split()

print("Words:", words)
print("processing...")

for word in words:
  counts[word] = counts.get(word,0) +1
print("counts", counts)

