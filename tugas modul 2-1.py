# Fungsi A: Menggunakan nested loop - O(n²)
def find_duplicates_nested_loop(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates


# Fungsi B: Menggunakan set - O(n)
def find_duplicates_set(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# Contoh penggunaan
test_list = [1, 2, 3, 2, 4, 3, 5, 1]
print("Nested Loop:", find_duplicates_nested_loop(test_list))
print("Set Method:", find_duplicates_set(test_list))
