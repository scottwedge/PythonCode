#!/usr/bin/env python

def quickSort(array):
    mySort(array, 0, len(array))

def mySort(array, begin, end):
    if begin < end - 1:
        mid = partition(array, begin, end)
        mySort(array, begin, mid)
        mySort(array, mid+1, end)

# increasing sorting
def partition(array, begin, end):
    swap(array, begin, begin + (end - begin) / 2)
    cur = array[begin]
    j = begin
    for i in range(begin+1, end):
        if cur > array[i]:
            j = j + 1
            swap(array, i, j)
    swap(array, j, begin)
    return j

def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

if __name__ == '__main__':
    nums = []
    n = int(raw_input('Please input array size: '));
    for i in range(0, n):
        nums.append(int(raw_input('The ' + str(i) + 'th number: ')));
    quickSort(nums)
    for item in nums:
        print item
