# kcadriranje broja
print(list(map(lambda x : x**2, [1,2,3,4,5])))

# zvroj pa kvadriraj
print(list(map(lambda x : (x+x)**2, [1,2,3,4,5])))

#kvadriraj duljinu niza
print(list(map(lambda x : len(x) ** 2, ["asd","asd","asd"])))

# Pomnoži vrijednost s 5 pa potenciraj na x:+
print(list(map(lambda x : (x*x) ** 2, [1,2,3,4,5,6])))

# vrati true ako je broj paran
print(list(map(lambda x :True if  x % 2 == 0 else False , [1,2,3,4,5,6])))