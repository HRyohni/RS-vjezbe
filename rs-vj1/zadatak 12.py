def obrni_rjecnik(param):
    rijec = {}
    for x in param:
        rijec[param[x]] = x
    return rijec

print(obrni_rjecnik({"ime": "Ivan", "prezime": "Ivić", "dob": 25}))