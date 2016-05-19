def isPalindrome(number):
    return str(number) == str(number)[::-1]


set = set()

for firstnumber in range(999,900, -1):
    for secondnumber in range(999,900, -1):
        set.add(firstnumber*secondnumber)


for element in set:
    if(isPalindrome(element)):
        print(element)
