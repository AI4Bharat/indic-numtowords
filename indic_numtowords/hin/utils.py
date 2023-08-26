def combine(lis1, lis2, seperator = " "):
    inter_list = []
    for i in lis1:
        for j in lis2:
            inter_list.append((i + seperator + j).rstrip())
    return inter_list