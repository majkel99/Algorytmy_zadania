import random
def partition(tab, first, last, start, mid):
    pivot = tab[last]
    end=last
    while(mid[0] <= end):
        if(tab[mid[0]]<pivot):
            tab[mid[0]], tab[start[0]] = tab[start[0]], tab[mid[0]]
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
        elif (tab[mid[0]] > pivot):
            tab[mid[0]], tab[end] = tab[end], tab[mid[0]]
            end = end - 1
        else:
            mid[0] = mid[0] + 1
def quickSort(tab, first, last):
    if (first >= last):
        return
    if (last == first + 1):
        if (tab[first] > tab[last]):
            tab[first], tab[last] = tab[last], tab[first]
            return
    start = [first]
    mid = [first]
    partition(tab, first, last, start, mid)
    quickSort(tab, first, start[0] - 1)
    quickSort(tab, mid[0], last)
def gen_array(size):
    arr = []
    for i in range(0,size):
        arr.append(random.randint(0,size))
    return arr
tab = []
tab=gen_array(50)
print("Przed sortowaniem:")
print(tab)
quickSort(tab, 0, len(tab) - 1)
print("Po sortowaniu:")
print(tab)