def bubble_sort(arr, start, end):
    if end == 0:
        return

    if start < end:
        if arr[start] > arr[start + 1]:
            arr[start], arr[start + 1] = arr[start + 1], arr[start]
        bubble_sort(arr, start + 1, end)
    else:
        bubble_sort(arr, 0, end - 1)

inp = [int(i) for i in input("Enter Input : ").split()]
bubble_sort(inp, 0, len(inp) - 1)
print(inp)
