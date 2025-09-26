edad = int(input("¿Qué edad tienes?"))
nivel_fisico = int(input("Introuzca su nivel físico en una escala del 1 al 10"))
if edad < 18:
    print("Debes ser mayor de edad")
elif nivel_fisico < 5:
    print("Debes estar en mejor forma")
else:
    print("¡Listo para despegar!")
