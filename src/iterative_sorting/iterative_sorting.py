# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for border in range(0, len(arr) - 1):
        right = border
        left = active - 1

        while left >= 0:
            if arr[left] > arr[right]:
                arr[left], arr[right] = (arr[right], arr[left])
                left -= 1
                right -= 1
            else:
                break

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
