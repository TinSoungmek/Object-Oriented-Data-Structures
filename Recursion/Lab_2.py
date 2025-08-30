def reverse_sort_list(list):
    if len(list) <= 1:
        return list
    
    max_value = max(list)
    list.remove(max_value)

    return [max_value] + reverse_sort_list(list)

inp = input("Enter your List : ").split(",")
inp = list(map(int,inp))
print("List after Sorted :",reverse_sort_list(inp))