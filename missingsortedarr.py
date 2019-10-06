import random

def binarySearchMissingNum(arr):
    start = 0
    end = len(arr) - 1
    mid = lambda: (start + end) // 2
    while start < end:
        m = mid()
        if arr[m] - m == 1:
            start = m + 1
        elif arr[m] - m == 2:
            end = m - 1
    if start == 0:
        return 1 if arr[start] == 2 else 2
    elif arr[start] - 1 == arr[start - 1]:
        return arr[start] + 1
    elif arr[start - 1] == arr[start] - 2:
        return arr[start] - 1

while True:
    z = random.randint(2,200000)
    a = list(range(1, z + 1))
    r = random.randint(0,z-1) 
    val = a[r]
    del a[r]
    ans = binarySearchMissingNum(a)
    assert ans == val
    print(f'Missing number was {val}')
