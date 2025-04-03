
from EJERCICIOS import Ejercicio1
from EJERCICIOS import Ejercicio2
from EJERCICIOS import Ejercicio3
from EJERCICIOS import Ejercicio4

def ejecutar_ejercicio_1():
    print("Ejecutando Ejercicio 1: Puzzle de la Pirámide de Piedras Preciosas")
    Ejercicio1.hanoi(5, 'A', 'C', 'B')

def ejecutar_ejercicio_2():
    print("\nEjecutando Ejercicio 2: Secreto de la Cifra Mágica")
    matrix_3x3 = [[2, -3, 1], [2, 0, -1], [1, 4, 5]]
    print("Determinante (Recursivo):", Ejercicio2.determinant_recursive(matrix_3x3))
    print("Determinante (Iterativo):", Ejercicio2.determinant_iterative(matrix_3x3))

def ejecutar_ejercicio_3():
    print("\nEjecutando Ejercicio 3: Gran Rally Espacial")
    print("Naves ordenadas por nombre:", Ejercicio3.naves_ordenadas_nombre)
    print("Cinco naves con más pasajeros:", Ejercicio3.naves_mas_pasajeros)
    print("Nave con más tripulación:", Ejercicio3.nave_mas_tripulacion)
    print("Naves cuyo nombre empieza con GX:", Ejercicio3.naves_GX)
    print("Naves con seis o más pasajeros:", Ejercicio3.naves_mas_seis_pasajeros)
    print("Nave más pequeña:", Ejercicio3.nave_mas_pequena)
    print("Nave más grande:", Ejercicio3.nave_mas_grande)

def ejecutar_ejercicio_4():
    print("\nEjecutando Ejercicio 4: Matemática de los Encantamientos")
    p1 = Ejercicio4.Polinomio("x**3 + 2*x**2 + 3*x + 4")
    p2 = Ejercicio4.Polinomio("x + 1")
    print("Resta:", p1.restar(p2))
    cociente, residuo = p1.dividir(p2)
    print("División - Cociente:", cociente, "Residuo:", residuo)
    print("¿El polinomio contiene 2*x^2?", p1.contiene_termino("2*x**2"))

def main():
    ejecutar_ejercicio_1()
    ejecutar_ejercicio_2()
    ejecutar_ejercicio_3()
    ejecutar_ejercicio_4()

if __name__ == "__main__":
    main()

