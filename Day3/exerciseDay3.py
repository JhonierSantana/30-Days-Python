# Ejercicios - Día 3

# Declarar variables
edad = 25
altura = 1.75
numero_complejo = 3 + 4j

# Calcular el área de un triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = 0.5 * base * altura
print("El área del triángulo es:", area_triangulo)

# Calcular el perímetro de un triángulo
lado_a = float(input("Ingrese el lado a del triángulo: "))
lado_b = float(input("Ingrese el lado b del triángulo: "))
lado_c = float(input("Ingrese el lado c del triángulo: "))
perimetro_triangulo = lado_a + lado_b + lado_c
print("El perímetro del triángulo es:", perimetro_triangulo)

# Calcular el área y el perímetro de un rectángulo
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print("El área del rectángulo es:", area_rectangulo)
print("El perímetro del rectángulo es:", perimetro_rectangulo)

# Calcular el área y la circunferencia de un círculo
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia_circulo = 2 * pi * radio
print("El área del círculo es:", area_circulo)
print("La circunferencia del círculo es:", circunferencia_circulo)

# Calcular la pendiente, intersección con el eje x e intersección con el eje y de y = 2x - 2
pendiente = 2
interseccion_eje_y = -2
punto1 = (2, 2)
punto2 = (6, 10)
pendiente_calculada = (punto2[1] - punto1[1]) / (punto2[0] - punto1[0])
distancia_euclidiana = ((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)**0.5
print("Pendiente:", pendiente_calculada)
print("Distancia Euclidiana:", distancia_euclidiana)

# Comparar las pendientes de los puntos
if pendiente == pendiente_calculada:
    print("Las pendientes son iguales.")
else:
    print("Las pendientes son diferentes.")

# Calcular el valor de x para que y sea igual a 0
# y = x^2 + 6x + 9
# y = (x + 3)^2
# La ecuación es igual a cero cuando x = -3
valor_x_cero = -3

# Comparar longitudes de cadenas y hacer afirmaciones falsas
cadena1 = 'python'
cadena2 = 'dragón'

if len(cadena1) == len(cadena2):
    print("Las longitudes de las cadenas son iguales.")
else:
    print("Las longitudes de las cadenas son diferentes.")

# Comprobar si 'on' se encuentra en 'python' y 'dragon'
if 'on' in cadena1 and 'on' in cadena2:
    print("'on' se encuentra en ambas cadenas.")
else:
    print("'on' no se encuentra en ambas cadenas.")

# Usar el operador 'in' para verificar jerga en una oración
oracion = "Espero que este curso no esté lleno de jerga."
if 'jerga' in oracion:
    print("Hay jerga en la oración.")
else:
    print("No hay jerga en la oración.")

# Comprobar si un número es par
numero = 6
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número no es par.")

# Comprobar si la división de piso de 7 por 3 es igual a 2.7 convertido a entero
if int(7 // 3) == int(2.7):
    print("Las expresiones son iguales.")
else:
    print("Las expresiones no son iguales.")

# Comprobar el tipo de datos
if type('10') == type(10):
    print("Los tipos de datos son iguales.")
else:
    print("Los tipos de datos no son iguales.")

# Comprobar si int('9.8') es igual a 10
try:
    if int('9.8') == 10:
        print("Las expresiones son iguales.")
    else:
        print("Las expresiones no son iguales.")
except ValueError:
    print("No se puede convertir '9.8' a entero.")

# Calcular el salario de una persona
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
salario = horas_trabajadas * tarifa_por_hora
print("Ganancia semanal: ", salario)

# Calcular el número de segundos en una vida de 100 años
años_vividos = int(input("Ingrese el número de años que ha vivido: "))
segundos_por_anio = 365 * 24 * 60 * 60
segundos_vividos = años_vividos * segundos_por_anio
print("Has vivido", segundos_vividos, "segundos.")

# Mostrar la tabla solicitada
for i in range(1, 6):
    print(i, i, i**2, i**3, i**4)
