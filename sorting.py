from ash import swap, unsorted, mergeSort, ShellSort
from typing import List


def bubble_sort(alist: List[str]):
    total_range = range(len(alist) - 1);
    for j in total_range:
        for i in total_range:
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    print(alist)


def insertion_sort(alist):
    total_range = range(1, len(alist))
    for i in total_range:
        value_insert = alist[i]
        hold = i

        while hold > 0 and alist[hold - 1] > value_insert:
            alist[hold] = alist[hold - 1]
            hold -= 1

        alist[hold] = value_insert

    print(alist)


def selectionSort(alist):
    for i in range(len(alist)):
        index_min = i

        for j in range(i + 1, len(alist)):
            if alist[j] < alist[index_min]:
                index_min = j

        if index_min != i:
            temp = alist[index_min]
            alist[index_min] = alist[i]
            alist[i] = temp

    print(alist)


# bubble_sort(unsorted)
# insertion_sort(unsorted)
# selectionSort(unsorted)
mergeSort(unsorted)
# ShellSort(unsorted)
