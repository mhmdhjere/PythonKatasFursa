def compare_versions(version1, version2):
    ver1_list = [int(n) for n in version1.split('.')]
    ver2_list = [int(n) for n in version2.split('.')]
    
    while len(ver1_list) < 3:
        ver1_list.append(0)
    while len(ver2_list) < 3:
        ver2_list.append(0)

    for i in range(len(ver1_list)):
        if ver1_list[i] > ver2_list[i]: 
            return 1
        elif ver1_list[i] < ver2_list[i]:
            return -1
    
    return 0


if __name__ == '__main__':
    print(f"'1.0.0' compared to '1.0.1': {compare_versions('1.0.0', '1.0.1')}")  # Expected: -1
    print(f"'2.1.0' compared to '1.9.9': {compare_versions('2.1.0', '1.9.9')}")  # Expected: 1
    print(f"'1.2.3' compared to '1.2.3': {compare_versions('1.2.3', '1.2.3')}")  # Expected: 0

    # Additional test cases
    print(f"'1.2' compared to '1.2.0': {compare_versions('1.2', '1.2.0')}")  # Expected: 0
    print(f"'1.10.0' compared to '1.2.0': {compare_versions('1.10.0', '1.2.0')}")  # Expected: 1
    print(f"'2.0.0' compared to '10.0.0': {compare_versions('2.0.0', '10.0.0')}")  # Expected: -1