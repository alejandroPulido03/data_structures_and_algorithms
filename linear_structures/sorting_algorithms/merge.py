def mergeSort(list):

    if len(list) <= 1:
        return list
    else:
        left = mergeSort(list[:len(list) // 2])
        right = mergeSort(list[len(list) // 2:])
        return merge(left, right)
    
def merge(list1, list2):
    mergedList = []
    
    i = 0
    for elem in list1:
        while i < len(list2) and list2[i] < elem:
            mergedList.append(list2[i])
            i += 1
        mergedList.append(elem)
    
    mergedList.extend(list2[i:])

    return mergedList

