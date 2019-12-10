# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    a = arrA[:]
    b = arrB[:]
    merged = []
    # TO-DO

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    return merged + a + b


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    sorted_left = merge_sort(arr[:middle])
    sorted_right = merge_sort(arr[middle:])

    return merge(sorted_left, sorted_right)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
