import testing
def heap_sort(tab):
    def heapify(tab, n, i):
        largest=i
        lindex = (2*i)+1
        rindex = lindex+1
        if lindex<n and tab[largest] < tab[lindex]:
            largest=lindex
        if rindex < n and tab[largest] < tab[rindex]:
            largest=rindex
        if largest != i:
            tab[i],tab[largest]=tab[largest],tab[i]
            heapify(tab,n,largest)
    n=len(tab)
    for i in range(n,-1,-1):
        heapify(tab,n,i)
    for i in range(n-1,0,-1):
        tab[i],tab[0]=tab[0],tab[i]
        heapify(tab, i, 0)
testing.test_algorithm(heap_sort)