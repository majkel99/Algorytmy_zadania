import testing
def quick_sort(tab):
    def part(tab,beg,end):
        i=beg-1
        pivot=tab[end]
        for j in range(beg,end):
            if tab[j] < pivot:
                i+=1
                tab[i], tab[j] = tab[j], tab[i]
        tab[i+1], tab[end] = tab[end], tab[i+1]
        return i+1
    def sort(tab, beg, end):
        if beg<end:
            split=part(tab,beg,end)
            sort(tab, beg, split-1)
            sort(tab, split+1, end)
    sort(tab, 0, len(tab)-1)
testing.test_algorithm(quick_sort)