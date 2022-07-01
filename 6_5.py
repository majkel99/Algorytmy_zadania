import testing
def merge_sort(tab):
    def merge(left,right):
        out=[]
        while len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                out+=[left.pop(0)]
            else:
                out+=[right.pop(0)]
        while len(left)>0:
            out+=[left.pop(0)]
        while len(right)>0:
            out+=[right.pop(0)]
        return out
    def sort(tab):
        if len(tab)>1:
            left=sort(tab[:int(len(tab)/2)])
            right=sort(tab[int(len(tab)/2):])
            return merge(left,right)
        else:
            return tab
    sort(tab)
testing.test_algorithm(merge_sort)