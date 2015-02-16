i = 0
y = 0

for x in xrange(1,1000):
	if (x%3) == 0 or (x%5) == 0:
		i = i + 1
		y = y + x
		print x

print i
print y