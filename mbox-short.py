fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
   # print count
    num = float(line[20:])
    total +=num
   # print total
    average = total/count
print("Average spam confidence:", average)
