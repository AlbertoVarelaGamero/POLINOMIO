def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover piedra de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)


n = 5
hanoi(n, 'A', 'C', 'B')
