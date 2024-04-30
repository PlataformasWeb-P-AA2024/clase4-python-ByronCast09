#leer archivo csv
archivo= open("data/atp_tennis.csv","r")

lineas = archivo.readlines()
#contar len
print(len(lineas))
print(lineas[0])
print("--------------------")
print(lineas[1])
print("-------------")
