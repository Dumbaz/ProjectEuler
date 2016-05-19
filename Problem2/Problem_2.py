fib_numbers = [1,2]

def fib(first, second):
	if(first) not in fib_numbers:
		fib_numbers.append(first)
	if(second) not in fib_numbers:
		fib_numbers.append(second)
	fib_numbers.append(first+second)
	return (first + second)
	
	
while (fib_numbers[-1] < 4000000):
	fib(fib_numbers[-1], fib_numbers[-2])
	
print(fib_numbers)

sum = 0

for term in fib_numbers:
	if(term%2 == 0):
		sum += term
		
print(sum)
