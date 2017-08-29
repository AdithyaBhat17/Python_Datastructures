# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if(len(fname)==0):
    fname='mbox-short.txt'
fh = open(fname)
count=0
tot=0
avg=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+1

	num=float(line[21:])
    tot=tot+num
avg=tot/count
print('Average spam confidence:'avg)
