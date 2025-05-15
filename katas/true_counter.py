def count_true_values(array):
    return sum(1 for val in array if val is True)

if __name__ == '__main__':
    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed
