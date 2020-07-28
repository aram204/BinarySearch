def quickSort(lst):
    if len(lst)<=1: return lst
    else:
        k = lst[len(lst) // 2]
        l = [i for i in lst if i<k]
        m = [k]*lst.count(k)
        r = [i for i in lst if i > k]
        return quickSort(l) + m + quickSort(r)

def get_num_in_array(a,lst):
    lst = quickSort(lst)
    i = 0
    j = len(lst)-1
    while j-i!=1:
        m = (i+j) // 2
        if lst[m] == a:
            return True
        if a < lst[m]:
            j = m
        if a > lst[m]:
            i = m
        print([i, m, j])
    if lst[i] == a: return True
    if lst[j] == a: return True
    else: return False

