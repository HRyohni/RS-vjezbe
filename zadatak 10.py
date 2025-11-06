def brojanje_riječi(tekst):
    temp = {}
    for rijec in tekst.split(' '):
        temp[rijec] = tekst.count(rijec)
    return temp


print(brojanje_riječi("Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."))


