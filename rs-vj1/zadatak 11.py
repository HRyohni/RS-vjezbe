def grupiraj_po_paritetu(lista):
    rezultat = {'parni': [], 'neparni': []}
    [rezultat['parni'].append(x) if x%2 == 0 else rezultat['neparni'].append(x) for x in lista]
    return rezultat

print(grupiraj_po_paritetu([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))