def count_vowels_consonants(tekst):
    vowels , consonants , rezultat= "aeiouAEIOU", "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" , {'vowels': 0, 'consonants': 0}

    for slovo in tekst:
        if  slovo in vowels:
            rezultat['vowels'] += 1
        elif slovo in consonants:
            rezultat['consonants'] += 1

    return rezultat


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))
# {'vowels': 30, 'consonants': 48}