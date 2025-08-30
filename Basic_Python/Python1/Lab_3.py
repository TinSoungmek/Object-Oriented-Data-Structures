print("*** Reading E-Book ***")
text,highlight = input("Text , Highlight : ").split(",")
ans = []
for word in text:
    if highlight == word:
        ans.append(f"[{highlight}]")
    else:
        ans.append(word)
for i in ans:
    print(i,end="")
