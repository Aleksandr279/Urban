numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Исходный список: ',numbers_)
primes_ = []
not_primes_ = []
numbers_.remove(1)
print('Число 1 не является ни простым ни составным числом.')
for i in range(len(numbers_)):
    is_prime_ = 0
    for j in range(len(numbers_[0:i])):
        if numbers_[i] % numbers_[j] == 0:
            is_prime_ = is_prime_ + 1
            if is_prime_ == 1:
                break
    if is_prime_ == 0:
        primes_.append(numbers_[i])
    else:
        not_primes_.append(numbers_[i])
print('В исходном списке числа ',primes_,'являются простыми числами.')
print('В исходном списке числа ',not_primes_,'являются составными числами.')
