"""
    Manejo de excepciones en Python
"""

# Se establece una bandera, variable de tipo boleana
# para controlar la ejecución del bucle
# Se inicializa en True (verdadero)
bandera = True

# Se inicia un bucle que continuará hasta que el usuario ingrese datos válidos,
# Caso contrario, seguirá ejecutándose el ciclo
while bandera:
    # Se inicia un bloque try para capturar posibles errores durante la ejecución
    try:
        # Se solicita al usuario un valor para el numerador y se convierte a float
        numerador = input("Ingrese un valor numérico como numerador: ")
        numerador = float(numerador)

        # Se solicita al usuario un valor para el denominador y se convierte a float
        denominador = input("Ingrese un valor numérico como denominador: ")
        denominador = float(denominador)

        # Validación del numerador: debe ser mayor o igual a 20
        # Si no cumple, se lanza una excepción personalizada usando raise Exception
        if numerador < 20:
            raise Exception("Error: El numerador debe ser mayor o igual a 20.")

        # Se realiza la operación de división
        division = numerador / denominador
        
        # Se imprime el resultado de la división, formateado con 2 decimales
        print(f"La división entre {numerador}/{denominador} es igual a {division:.2f}")
        
        # Se cambia la bandera a False para salir del bucle
        bandera = False

    # Se captura el error ValueError cuando el usuario ingresa un valor no numérico
    except ValueError as v:
        print("Error: Se debe ingresar un valor numérico válido.")
        print(v)  # Se muestra el mensaje técnico del error

    # Se captura el error ZeroDivisionError cuando el usuario intenta dividir por cero
    except ZeroDivisionError as z:
        print("Error: No se puede dividir por cero.")
        print(z)  # Se muestra el mensaje técnico del error

    # Se captura cualquier otra excepción, incluyendo la generada por raise Exception
    except Exception as e:
        print(e)  # Se muestra el mensaje de error personalizado

# Mensaje final del programa, se ejecuta independientemente de si hubo error o no
print("Fin del programa")
