def solution(A):
    if len(A) > 1000000000:
        return -1

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inversions = merge_sort(arr[:mid])
        right, right_inversions = merge_sort(arr[mid:])

        merged = []
        i, j = 0, 0
        inversions = left_inversions + right_inversions

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
            else:
                merged.append(left[i])
                i += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    _, inversions = merge_sort(A)
    return inversions


integers = [-1, 6, 3, 4, 7, 4]
inversion = solution(integers)
print(inversion)