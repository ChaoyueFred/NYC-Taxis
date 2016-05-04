import sys
count ={}
for line in sys.stdin:
	k,v = line.strip().split(',')
	if k in count:
		count[k] += 1
	else:
		count[k]=1

for key in sorted(count):
    print "%s: %s" % (key, count[key])
