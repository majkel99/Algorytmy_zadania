import testing
def bubble_sort(tab):
    n=len(tab)
    for i in range(n):
        trig = False
        for j in range(n-i-1):
            if tab[j+1]<tab[j]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
                trig=True
        if trig==False:
            break
testing.test_algorithm(bubble_sort)