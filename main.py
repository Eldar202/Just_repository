def merge(*lists):
    k = len(lists)
    list1=[]
    for i in range(0,k):
        list2 = lists[i]
        list1.extend(list2)
    list1.sort()
    print(list1)





