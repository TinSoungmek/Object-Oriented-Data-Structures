def bubble_sort(arr, start, end, swapped=False):
    if end == 0:
        return

    if start == end:
        if not swapped:
            return
        else:
            bubble_sort(arr, 0, end - 1, False)
    else:
        if arr[start] > arr[start + 1]:
            arr[start], arr[start + 1] = arr[start + 1], arr[start]
            bubble_sort(arr, start + 1, end, True)
        else:
            bubble_sort(arr, start + 1, end, swapped)

inp = [int(i) for i in input("Enter Input : ").split()]
bubble_sort(inp, 0, len(inp) - 1, False) 
print(inp)