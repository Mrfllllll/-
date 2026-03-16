def sum_odd_even(nums):
    sum_odd = 0
    sum_even = 0

    for x in nums:
        if x % 2 == 0:
            sum_even = sum_even + x
        else:
            sum_odd = sum_odd + x

    return sum_odd, sum_even
numbers = [1, 2, 3, 4, 5, 10, 11]
odd_sum, even_sum = sum_odd_even(numbers)

print("Список:", numbers)
print("Сумма нечётных:", odd_sum)
print("Сумма чётных:", even_sum)