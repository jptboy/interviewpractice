def f(a):
    i = 0
    j = 0
    while i < len(a):
        if a[i] == 0:
            a[j] = 0
            j += 1
        i += 1
    while j < len(a):
        a[j] = 1
        j += 1
    return a

print(f([0,1,0,1,1,1,0]))