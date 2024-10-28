import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_ten_or_more_numbers():
    input_arr = [34, 7, 23, 32, 5, 62, 76, 43, 9, 12]
    expected_result = 1
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == expected_result)

def test_bubble_sort_zero_numbers():
    input_arr = []
    expected_result = 0
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == expected_result)

def test_bubble_sort_not_integers():
    input_arr = [1.8, 2.3, 7.9, 8.0, 4.5, 9.3, 5.6]
    expected_result = 2
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == expected_result)