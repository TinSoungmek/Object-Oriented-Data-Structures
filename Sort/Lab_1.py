def bubble_sort(arr, start, end, swapped_in_pass=False):
    if end == 0:
        return

    if start == end:
        if not swapped_in_pass:
            return
        else:
            bubble_sort(arr, 0, end - 1, False)
    else:
        if arr[start] > arr[start + 1]:
            arr[start], arr[start + 1] = arr[start + 1], arr[start]
            bubble_sort(arr, start + 1, end, True)
        else:
            bubble_sort(arr, start + 1, end, swapped_in_pass)

inp = [int(i) for i in input("Enter Input : ").split()]
bubble_sort(inp, 0, len(inp) - 1, False) 
print(inp)