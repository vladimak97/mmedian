
# Write a Python function to calculate the mean and median of a given list of numbers.

def calculate_mean_median(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return mean, median

numbers = [1, 2, 3, 4, 5]
mean, median = calculate_mean_median(numbers)
print(f"Mean: {mean}, Median: {median}")