import testing
def insertion_sort(tab):
    n=len(tab)
    for i in range(n):
        x=tab[i]
        y=i-1
        while x<tab[y] and y>=0:
            tab[y+1]=tab[y]
            y-=1
        tab[y+1]=x
testing.test_algorithm(insertion_sort)