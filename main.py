# nomes = ["Ana","Bruno","Carla","Diego","Fernanda"]
# print(nomes[1])
# print(len(nomes))
# nomes.append("Gabriel")
# nomes.insert(1,"Allan")
# print(nomes)
# nomes.clear
# print(nomes)
# del(nomes)
# print(nomes)


#Exemplo de Dicionário
info = {
  "Nomes": ["Ana","Bruno","Carla"],
  "Idades":(10,25,14),
  "parentesco":{
    "nome":"Ana",
    "Pais":["Maria","João"]
  }
}

# print(info.Nomes)

#Exenplos de tupla
notas = (9.4,8.3,5.2,10.0,4.8
print(f"Nota na posição 2: {notas[2]}")
notas.insert(1,10.0)
notas.append(5.8)
del(notas)