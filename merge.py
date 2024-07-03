
l1 = [12,15,17,20]
l2 = [1,3,15,29,59,60]

def merge(list1, list2):

    one = 0
    two = 0
    merged = []

    while one < len(list1) and two < len(list2):
        if list1[one] < list2[two]:
            merged.append(list1[one])
            one += 1
        else:
            merged.append(list2[two])
            two += 1

    if one == len(list1):
        merged = merged + list2[two:]
    else:
        merged = merged + list1[one:]

    return merged

print(merge(l1,l2))