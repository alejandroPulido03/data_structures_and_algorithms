def quickSort(list):
    import random
    import sys
    sys.setrecursionlimit(10**5)
    random.shuffle(list)
    return pivotList(list,0 ,len(list) - 1)

def pivotList(list, i, j):
    pivot = list[i]
    a = i + 1
    b = j
    if a < b:
        while a < b:
            if list[a] > pivot:
                if list[b] < pivot:
                    swap(list, a, b)
                    a += 1    
                b -=1
            else:
                a += 1
        if pivot > list[a]:
            swap(list, i, a)
        else:
            swap(list, i, a - 1)
        pivotList(list, i, a - 1)
        pivotList(list, a, j)
    return list

def swap(list, i, j):
    aux = list[i]
    list[i] = list[j]
    list[j] = aux

