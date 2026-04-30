# i = 0
# while(i <= 100):
#   print(f"{i} \n")
#   i += 1

# for i in range(0, 101, 1):
#   print(f"{i} \n")

nomes = ["Ana", "bruno", "carla", "diego","eduarda"]
nomes.append("Felipe")
nomes.append("Gabriela")
nomes.insert(1,"André")
nomes2 = ["Heitor","Ingred","Julio","Kamila","ludson","Maria","nicolas"]
nomes.extend(nomes2)
nomes.append("Ana")
nomes.remove("Ana")
nomes.remove("Ana")
nomes.clear()
for nome in nomes:
  print(nome) 