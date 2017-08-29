fname = input("Enter file name: ")

fh = open(fname)
count = 0
lst=list()
for line in fh:
    if not line.startswith("From "):
       continue
    else:
        words=line.split()
        lst.append(words[1])
for i in lst:
    print(i)
    count=count+1
print('There were',count,'lines in the file with From as the first word')
    
