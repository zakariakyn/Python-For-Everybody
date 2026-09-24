fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    val = float(line[pos + 1:])
    total = total + val
    count = count + 1

if count > 0:
    print("Average spam confidence:", total / count)