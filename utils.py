def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number
    return max