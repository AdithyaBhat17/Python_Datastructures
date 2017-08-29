name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words=list()
for line in handle:
    if not line.startswith('From'):
        continue
    line=line.split()
    words.append(line[1])
    
counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1

maxcount=None
maxWord=None
for word,count in counts.items():
    if count is None or count>maxcount:
        maxWord=word
        maxcount=count

print(maxWord,maxcount)
