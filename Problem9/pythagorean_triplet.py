import math

# a^2 + b^2 = c^2
# a < b < c
#one such triplet with a+b+c = 1000

# a range 1-995
# b range 2-996
# c range 3-997


def is_pythagorean_triplet(var_a, var_b, var_c):
    return var_a ** 2 + var_b ** 2 == var_c ** 2


def is_sum_1000(var_a, var_b, var_c):
    return var_a + var_b + var_c == 1000


def is_both(var_a, var_b, var_c):
    return is_pythagorean_triplet(var_a, var_b, var_c) & is_sum_1000(var_a, var_b, var_c)


def find_triplet(oddnumber):
    first_a = math.sqrt(oddnumber)
    term = (first_a ** 2 + 1) / 2
    second_b = (term - 1)
    third_c = term
    if first_a.is_integer() & second_b.is_integer() & third_c.is_integer():
        erg_dict = {}
        erg_dict['a'] = int(first_a)
        erg_dict['b'] = int(second_b)
        erg_dict['c'] = int(third_c)
        return erg_dict


print(find_triplet(15))

a = 1

while(a < 1000):
    if(find_triplet(a)):
        print(find_triplet(a))
    a += 2

print(31*480*481)

