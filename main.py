#Comentario

from cgi import print_form


print("Que miedo de la guerra")

nivelAgua=int(input("Digita la cantidad de agua de la represa: "))

print(f"El nivel de agua es {nivelAgua}")

print("Oe")

if(nivelAgua<200):
    print("No tengo agua")
elif(nivelAgua>=200 and nivelAgua<450):
    print("Todo bien energía corriente")
else:
    print("Ojo con caucasia")