def inversions_merge(array, temp_array, left, middle, right):
    i = left
    j = middle + 1
    k = left
    inversions_count = 0
    while i <= middle and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            inversions_count += (middle - i + 1)
            j += 1
        k += 1
    while i <= middle:
        temp_array[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        array[i] = temp_array[i]

    return inversions_count


def inversions_merge_sort(array, temp_array, left, right):
    inversions_count = 0
    if left < right:
        middle = (left + right) // 2
        inversions_count += inversions_merge_sort(array, temp_array, left, middle)
        inversions_count += inversions_merge_sort(array, temp_array, middle+1, right)
        inversions_count += inversions_merge(array, temp_array, left, middle, right)
    return inversions_count
