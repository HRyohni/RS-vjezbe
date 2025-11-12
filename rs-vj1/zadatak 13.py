def prvi_i_zadnji(list):
    return [list[0] ,list[-1]]

def maks_i_min(list):
    return [max(list) , min(list)]


def presjek(list1, list2):
    return set([x for x in list1 if x in list2])


print(prvi_i_zadnji([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # (1, 10)
print(maks_i_min([5, 10, 20, 50, 100, 11, 250, 50, 80])) # (250, 5)
print(presjek({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})) # {4, 5}
