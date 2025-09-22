def count_numbers(nums):
    freq = {}
    order = []

    for num in nums:
        if num not in freq:
            freq[num] = 1
            order.append(num)
        else:
            freq[num] += 1

    result = []
    for num in order:
        result.append([num, freq[num]])

    def custom_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j][1] < arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    sorted_result = custom_sort(result)

    for num, total in sorted_result:
        print(f"number {num}, total: {total}")

inp = [int(i) for i in input("Enter list  of numbers: ").split()]
count_numbers(inp)