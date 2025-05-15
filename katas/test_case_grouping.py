def group_test_cases(test_case_group_sizes):
    test_groups = {}
    res = []
    for i in range(len(test_case_group_sizes)):
        curr_test = test_case_group_sizes[i]

        if curr_test not in test_groups:
            test_groups[curr_test] = [[]]

        if len(test_groups[curr_test][-1]) ==  curr_test:
            test_groups[curr_test].append([])

        test_groups[curr_test][-1].append(i)

    for group_lists in test_groups.values():
        res.extend(group_lists)
    return res         


if __name__ == '__main__':
    # Example 1
    test_case_group_sizes1 = [1, 2, 3, 3, 3, 2]
    result1 = group_test_cases(test_case_group_sizes1)
    print(f"Input: {test_case_group_sizes1}")
    print(f"Output: {result1}")  # Expected: something like [[0], [1, 5], [2, 3, 4]]

    # Verification
    if result1:
        valid = True
        covered_indices = []

        for group in result1:
            # Check if all elements in this group require same group size
            expected_size = test_case_group_sizes1[group[0]]
            if not all(test_case_group_sizes1[idx] == expected_size for idx in group):
                valid = False
                print("Invalid: Not all test cases in a group require the same group size")
                break

            # Check if group size matches the required size
            if len(group) != expected_size:
                valid = False
                print(f"Invalid: Group {group} has size {len(group)} but should have size {expected_size}")
                break

            covered_indices.extend(group)

        # Check if all test cases are covered exactly once
        if sorted(covered_indices) != list(range(len(test_case_group_sizes1))):
            valid = False
            print("Invalid: Not all test cases are covered exactly once")

        print(f"Solution is valid: {valid}")

    # Example 2 - simpler case
    test_case_group_sizes2 = [2, 2, 1, 1]
    result2 = group_test_cases(test_case_group_sizes2)
    print(f"\nInput: {test_case_group_sizes2}")
    print(f"Output: {result2}")  # Expected: something like [[0, 1], [2], [3]]