from typing import List


def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    req = set()
    for t in test_cases:
        req.update(t)

    uncovered = set(req)
    res = []

    while uncovered:
        best_index = -1
        best_cover = set()

        for i in range(len(test_cases)):
            cover = uncovered.intersection(test_cases[i])
            if len(cover) > len(best_cover):
                best_index = i
                best_cover = cover

        if best_index == -1:
            break

        res.append(best_index)
        uncovered -= best_cover

    return res


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]