# import pdb
# pdb.set_trace()


def find_second_smallest(numbers):
    smallest = -float("inf")  # infinity
    second_smallest = -float("inf")

    for i in range(len(numbers) + 1):
        number = numbers[i]
        if number < smallest:
            smallest = number
            second_smallest = smallest
        elif number < second_smallest:
            second_smallest = number
    return second_smallest


print(find_second_smallest([1, 2, 3, 4, 5]))
print(find_second_smallest([7, 3, 5, 10, 2]))
