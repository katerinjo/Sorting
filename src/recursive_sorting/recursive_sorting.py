# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    shortest = min(len(arrA), len(arrB))
    merged = []
    # TO-DO

    for i in range(shortest):
        if arrA[i] < arrB[i]:
            merged.append(arrA[i])
        else:
            merged.append(arrB[i])

    return merged + arrA[shortest:] + arrB[shortest:]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
