data = input("Enter All Bid : ").split(" ")
bid = list(map(int,data))

def Winner(bid):
    start = 0
    second = 0
    if len(bid) <= 1:
        return "not enough bidder"
    else :
        for win in bid:
            if win > start:
                start = win
            elif win == start:
                return "error : have more than one highest bid"
        bid.remove(start)
        for sec in bid:
            if sec > second:
                second = sec
        return f"winner bid is {start} need to pay {second}"


print(Winner(bid))


