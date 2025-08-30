print("*** Mod Position ***")
s,arr = input("Enter Input : ").split(",")
arr = int(arr)
ans = []
def mod_position(arr, s):
    for i in range (len(s)):
        if (i+1)%arr == 0:
            ans.append(s[i])
    return ans

ans = mod_position(arr,s)
print(ans)
    