import statistics
import csv

'''
Media: Promedio de todas las ventas mensuales.
Mediana: Valor medio de las ventas ordenadas, útil cuando hay valores extremos.
Moda: Valor que más se repite en las ventas.
Desviación Estándar y Varianza: Miden la dispersión de las ventas respecto a la media; la desviación estándar está en las mismas unidades que los datos, mientras que la varianza está en unidades al cuadrado.
Máximo y Mínimo: Ventas más altas y más bajas registradas.
Rango: Diferencia entre la venta más alta y la más baja.
'''

# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#Hallar la media 
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

#Hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Desviacion Estandar
stdev_sales = statistics.stdev(sales)
print(f"La desviacion estandar es: {stdev_sales}")

#Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f"Rango de ventas: {range_sales}")