def find_max(list):
    if len(list) == 1:
        return list[0]
    
    rest = find_max(list[1:])
    return list[0] if list[0] > rest else rest

def reverse_sort_list(list):
    if len(list) <= 1:
        return list
    
    max_value = find_max(list)
    list.remove(max_value)

    return [max_value] + reverse_sort_list(list)

inp = input("Enter your List : ").split(",")
inp = list(map(int,inp))
print("List after Sorted :",reverse_sort_list(inp))