# -*- coding: utf-8 -*-
import math

first_name = "Jhonier"
last_name = "Santana"
full_name = first_name + " " + last_name
country = "Santander"
city = "Socorro"
age = 19
year = 2003
is_true = True
is_light_on = True

num1, num2, num3 = 120, 123, 4

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_true))
print(type(is_light_on))
print(type(num1))
print(type(num2))
print(type(num3))

first_name_length = len(first_name)
print(first_name_length)

last_name_length = len(last_name)
if first_name_length == last_name_length:
    print("La longitud de los nombres es igual")
else:
    print("La longitud de los nombres es diferente")


num_one = 5
num_two = 4

addition = num_one + num_two
substract = num_one - num_two
multiply =  num_one * num_two
division = num_one / num_two
module = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", addition)
print("Diferencia:", substract)
print("Producto:", multiply)
print("División:", division)
print("Resto:", module)
print("Potencia:", exp)
print("División entera:", floor_division)

radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

user_Radius = float(input("Ingrsar el radio del ciruclo: "))
area_of_circle = math.pi * (user_Radius ** 2)
print("Area del ciruclo con radio", user_Radius, "es", area_of_circle)

# Obtener información del usuario
first_name1 = input("Ingresa tu primer nombre: ")
last_name1 = input("Ingresa tu apellido: ")
country1 = input("Ingresa tu país: ")
age1 = input("Ingresa tu edad: ")

print("Nombre:", first_name1)
print("Apellido:", last_name1)
print("País:", country1)
print("Edad:", age1)

help('keywords')
