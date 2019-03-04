from typing import List, NoReturn

unsorted = [20, 100, 5, 50, 20, 20, 100, 5, 20, 7]


def swap(a, b):
    temp = a
    a = b
    b = temp
    return [a, b]


def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


def ShellSort(alist: List[int]):
    sublistCount = len(alist) // 2

    while sublistCount > 0:
        for i in range(sublistCount):
            SublistInsertSort(alist, i, sublistCount)

        print('Sublist Count:', sublistCount, 'List after sorted:', alist)
        sublistCount = sublistCount // 2


def SublistInsertSort(alist: List[int], start: int, gapSize: int):
    for i in range(start + gapSize, len(alist), gapSize):
        currentValue = alist[i]
        index = i
        while index >= gapSize and alist[index - gapSize] > currentValue:
            alist[index] = alist[index - gapSize]
            index = index - gapSize
        alist[index] = currentValue
