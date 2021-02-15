import base58
import sys

#print(sys.argv[1])
f1 = open(input("Enter file to be read: "), 'r')
f2 = open (input("Enter file to be created: "), 'w')
count = 0

while True:
  line = f1.readline()
  if not line:
    break
  line = line[:-1] # remove newline
  adr160 = base58.b58decode_check(line).hex()[2:]
  f2.write(str(adr160) + "\n")
  count += 1

print("finished writing/converting {} addresses", count)
