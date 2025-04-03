import sympy as sp

class Polinomio:
    def __init__(self, expresion):
        self.expresion = sp.sympify(expresion)

    def __repr__(self):
        return str(self.expresion)

    def restar(self, otro):
        return Polinomio(self.expresion - otro.expresion)

    def dividir(self, otro):
        cociente, residuo = sp.div(self.expresion, otro.expresion)
        return Polinomio(cociente), Polinomio(residuo)

    def eliminar_termino(self, termino):
        nuevo_polinomio = self.expresion - sp.sympify(termino)
        return Polinomio(nuevo_polinomio)

    def contiene_termino(self, termino):
        return sp.sympify(termino) in self.expresion.as_ordered_terms()


p1 = Polinomio("x**3 + 2*x**2 + 3*x + 4")
p2 = Polinomio("x + 1")

print("Polinomio 1:", p1)
print("Polinomio 2:", p2)


resultado_resta = p1.restar(p2)
print("Resta:", resultado_resta)


cociente, residuo = p1.dividir(p2)
print("División - Cociente:", cociente)
print("División - Residuo:", residuo)


resultado_eliminar = p1.eliminar_termino("3*x")
print("Polinomio sin término 3*x:", resultado_eliminar)


existe = p1.contiene_termino("2*x**2")
print("¿El polinomio contiene 2*x^2?", existe)
