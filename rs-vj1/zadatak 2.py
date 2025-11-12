godine = int(input("unesi godine: "))
if godine % 4 == 0 and godine % 100 != 0 or godine % 400 == 0 :
    print(f"Godina {godine}. je prijestupna.")
else:
    print(f"Godina {godine} nije prijestupna.")
