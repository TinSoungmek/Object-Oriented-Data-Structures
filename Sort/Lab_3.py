def insertion_sort(arr):

    def _recursive_sort(current_arr, n):

        if n >= len(current_arr):
            print("sorted")
            return
        key = current_arr[n]

        def _insert(sub_arr, j, key_to_insert):

            if j < 0 or sub_arr[j] <= key_to_insert:
                sub_arr[j + 1] = key_to_insert
                return j + 1
            else:
                sub_arr[j + 1] = sub_arr[j]
                return _insert(sub_arr, j - 1, key_to_insert)

        inserted_index = _insert(current_arr, n - 1, key)
        
        sorted_part = current_arr[:n+1]
        unsorted_part = current_arr[n+1:]
        
        print(f"insert {key} at index {inserted_index} : {str(sorted_part)}", end="")
        
        if unsorted_part:
            print(f" {str(unsorted_part)}")
        else:
            print()
        
        _recursive_sort(current_arr, n + 1)

    if len(arr) > 1:
        _recursive_sort(arr, 1)
    else:
        print("sorted")

inp = [int(i) for i in input("Enter Input : ").split()]
insertion_sort(inp)
print(inp)