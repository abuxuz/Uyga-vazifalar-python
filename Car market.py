ferari= {"model":"Ferari","rangi":"ko'k","narxi":"600 ming $","tezlik":"280 km/h"}
cars= {}
cars['model']= "Gentra"
cars['rangi']= "Oq"
cars['narx']= "15 ming $"
cars['tezlik']= "220 km/h"
print(f'\t Meni dadam yangi mashina oldi uning nomi {cars["model"]}. Uning rangi {cars["rangi"]}. Narxi esa {cars["narx"]}. Tezliki esa {cars["tezlik"]}.')
print(cars.get("model"))
print(cars.get("modl","Bunday kalit so'z yo'q."))
print(cars.keys())
print(cars.values())

