class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros
    
    def __repr__(self):
        return f"{self.nombre} (Longitud: {self.longitud}, Tripulación: {self.tripulantes}, Pasajeros: {self.pasajeros})"


naves = [
    NaveEspacial("Cometa Veloz", 120, 8, 30),
    NaveEspacial("Titán del Cosmos", 200, 15, 50),
    NaveEspacial("GX-200", 90, 5, 10),
    NaveEspacial("Estrella Fugaz", 150, 7, 25),
    NaveEspacial("Nebulosa Azul", 180, 12, 45),
    NaveEspacial("GX-100", 95, 6, 12)
]


naves_ordenadas_nombre = sorted(naves, key=lambda x: x.nombre)
naves_ordenadas_longitud = sorted(naves, key=lambda x: x.longitud, reverse=True)


naves_especificas = [n for n in naves if n.nombre in ["Cometa Veloz", "Titán del Cosmos"]]


naves_mas_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]


nave_mas_tripulacion = max(naves, key=lambda x: x.tripulantes)


naves_GX = [n for n in naves if n.nombre.startswith("GX")]


naves_mas_seis_pasajeros = [n for n in naves if n.pasajeros >= 6]


nave_mas_pequena = min(naves, key=lambda x: x.longitud)
nave_mas_grande = max(naves, key=lambda x: x.longitud)


print("\n1. Naves ordenadas por nombre:")
print(naves_ordenadas_nombre)
print("\nNaves ordenadas por longitud:")
print(naves_ordenadas_longitud)

print("\n2. Información de 'Cometa Veloz' y 'Titán del Cosmos':")
print(naves_especificas)

print("\n3. Cinco naves con más pasajeros:")
print(naves_mas_pasajeros)

print("\n4. Nave con más tripulación:")
print(nave_mas_tripulacion)

print("\n5. Naves cuyo nombre comienza con 'GX':")
print(naves_GX)

print("\n6. Naves con seis o más pasajeros:")
print(naves_mas_seis_pasajeros)

print("\n7. Nave más pequeña:")
print(nave_mas_pequena)

print("\nNave más grande:")
print(nave_mas_grande)
