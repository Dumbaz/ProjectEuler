def produce_triplet_with_sum(number_sum):
    for i in range(1, number_sum, 1):
        for j in range(1, number_sum-1, 1):
            k = number_sum-i-j
            if i ** 2 + j ** 2 == k**2:
                return i*j*k

product = produce_triplet_with_sum(1000)

print(product)
