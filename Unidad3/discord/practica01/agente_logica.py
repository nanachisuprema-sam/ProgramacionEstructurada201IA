"""
Funcion que recibe texto y decide responder.
implementa programacino estructurada pura
"""

def procesar_pregunta(mensaje_usuario):

    mensaje_usuario = mensaje_usuario.lower().strip()

    conocimiento = {

        #CONCEPTOS DE ESTRUCTURA DE CONTROL
        

        "if": "Estructura de control que permite ejecutar un bloque de código si se cumple una condición.",
        "else": "Estructura de control que permite ejecutar un bloque de código si no se cumple una condición.",
        "elif": "Estructura de control que permite ejecutar un bloque de código si se cumple una condición adicional después de un if.",
        "for": "Estructura de control que permite ejecutar un bloque de código un número determinado de veces.",
        "while": "Estructura de control que permite ejecutar un bloque de código mientras se cumpla una condición.",
        "break": "Instrucción que permite salir de un bucle antes de que se cumpla la condición de finalización.",
        "continue": "Instrucción que permite saltar a la siguiente iteración de un bucle sin ejecutar el código restante en la iteración actual.",
        
        #CONCEPTOS DE FUNCIONES
        "def": "Palabra clave que se utiliza para definir una función en Python.",
        "return": "Palabra clave que se utiliza para devolver un valor desde una función.",
        "import": "Palabra clave que se utiliza para importar módulos en Python.",
        "class": "Palabra clave que se utiliza para definir una clase en Python.", 

        #Tipos de datos
        "int": "Tipo de dato que representa números enteros.",
        "float": "Tipo de dato que representa números con decimales.",
        "str": "Tipo de dato que representa cadenas de caracteres.",
        "bool": "Tipo de dato que representa valores booleanos (verdadero o falso).",
        "list": "Tipo de dato que representa una lista de valores.",
        "tuple": "Tipo de dato que representa una tupla de valores.",
        "dict": "Tipo de dato que representa un diccionario de valores.",
        "set": "Tipo de dato que representa un conjunto de valores.",

        #Operadores de sintaxis
        "print": "Función que se utiliza para mostrar información en la consola.",
        "input": "Función que se utiliza para recibir información del usuario a través de la consola.",
        "len": "Función que se utiliza para obtener la longitud de un objeto.",
        "type": "Función que se utiliza para obtener el tipo de un objeto.",
        "range": "Función que se utiliza para generar una secuencia de números.",

        #conceptos de programación estructurada
        "Algoritmo": "Son la secuencia de pasos lógicos que resuelven un problema, ¡son la base de la programación! ...",
        "Variable": "Es una unidad de almacenamiento y recuperación de datos, datos que utilizarás más adelante al programar. ...",
        "Función.":"Es un bloque de código reutilizable que realiza tareas específicas. Se le llama a través del comando function. Cada vez que llamemos a esa función se ejecutará ese código, por lo que se ahorra tiempo en escribir línea por línea.",
        "Tipos de datos": "Son los diferentes tipos de variables en las que se clasifica la información. Por ejemplo, los más utilizados son Number, String, y Boolean.",
        "Estructuras de Control.": "El código se lee de arriba hacia abajo. Pero estas estructuras permiten que el código se lea de diferentes maneras. Son el caso de los ciclos y las condicionales:",
    }

    for clave in conocimiento:
        if clave in mensaje_usuario:
            return(conocimiento[clave])
    return("Lo siento, no tengo información sobre ese tema.")

def main():
    procesar_pregunta()

if __name__ == "__main__":
    main()