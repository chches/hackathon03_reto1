# RETO 1: 
# Ingresar 5 notas de un alumno e imprimir lista de notas, 
# nota promedio, nota menor, nota mayor.
# Considerar validaciones para las notas.

# 09:11

# Inicializando variables.
lista_notas = []    #Lista de notas.
cantidad_nota = 1   #Primera nota
no_es_nota = True #Booleano indicador numérico
nota = 0

print("PROGRAMA DE CALCULO NOTAS DE ALUMNO")
print("Ingrese 5 notas para obtener su nota promedio, ", end="")
print("menor y mayor.")
print()

#Solicitar notas hasta completar las 5. except KeyboardInterrupt
try:
    while True:
        no_es_nota = True

        while no_es_nota:
            try:
                print(f"Ingrese nota {cantidad_nota}: ", end="")
                nota = int(input())
                no_es_nota = False #Finaliza while al ingresar valor entero
            except Exception:
                print(f"[Error_tipo_dato]: Ingresar número entero, sin decimales.")

            if nota < 0 or nota > 20:
                no_es_nota = True
                print(f"[Error_valor_nota]: Ingresar número entre 0 y 20.")

        lista_notas.append(nota)

        if cantidad_nota == 5 and len(lista_notas) > 0:
            # calcular nota promedio
            nota_promedio = round(sum(lista_notas) / cantidad_nota)
            # determinar nota menor
            nota_menor = min(lista_notas)
            # determinar nota mayor
            nota_mayor = max(lista_notas)

            break
        
        cantidad_nota = cantidad_nota + 1
    print()
    print("RESULTADO DE NOTAS--------------------")
    print(f"Nota promedio: {nota_promedio}")
    print(f"Nota menor: {nota_menor}")
    print(f"Nota mayor: {nota_mayor}")

except KeyboardInterrupt:
    print(f"[Error_usuario]: Proceso cancelado por usuario.")
# 10:41--