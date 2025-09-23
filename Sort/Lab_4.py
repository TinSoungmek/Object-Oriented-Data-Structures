l = [e for e in input("Enter Input : ").split()]

if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))

    temp_list_sorted = []
    temp_list_original = []

    for new_num in l:
        temp_list_original.append(new_num)
        
        if len(temp_list_sorted) == 0:
            temp_list_sorted.append(new_num)
        else:
            inserted = False
            for i in range(len(temp_list_sorted)):
                if new_num < temp_list_sorted[i]:
                    temp_list_sorted.insert(i, new_num)
                    inserted = True
                    break
            if not inserted:
                temp_list_sorted.append(new_num)

        n = len(temp_list_sorted)
        median = 0.0
        if n % 2 == 1:
            # ถ้าจำนวนข้อมูลเป็นเลขคี่, มัธยฐานคือตัวตรงกลาง
            median = float(temp_list_sorted[n // 2])
        else:
            # ถ้าจำนวนข้อมูลเป็นเลขคู่, มัธยฐานคือค่าเฉลี่ยของ 2 ตัวตรงกลาง
            mid1 = temp_list_sorted[(n // 2) - 1]
            mid2 = temp_list_sorted[n // 2]
            median = (mid1 + mid2) / 2.0
        
        print(f"list = {temp_list_original} : median = {median}")