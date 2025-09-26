distancia_marte = 225000000
for velocidad in range(10000,50000,10000):
    tiempo = distancia_marte / velocidad
print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo} días")
