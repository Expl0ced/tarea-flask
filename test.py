import json


ruta='pokedex.json'
with open(ruta) as contenido:
    resultado=json.load(contenido)
    mylist=resultado.items()
    print(type(mylist))
    mylist=list(mylist)
    print(mylist)
    for i in mylist:
        pokemon=resultado[i]
        print(pokemon[1])
# for i in range(1,151):
#     pokemon=resultado['pokemon'][i]['num']

            
            

# print(pokemon)