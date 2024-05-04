# Laboratorio No. 2
En este ejercicio, tu tarea es crear dos clases en Python: Pokemon y Trainer. Estas clases representarán a los personajes del mundo Pokémon y tendrán atributos y métodos específicos.

## Objetivo
El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos como: Clases, Ojetos, Atributos, Métodos e Instancias

## Paso 1: Crear la clase Pokemon

La clase Pokemon debe tener los siguientes atributos:

id: Un número entero que representa el identificador único del Pokémon.
name: Una cadena de caracteres que representa el nombre del Pokémon.
weight: Un número decimal que representa el peso del Pokémon.
height: Un número decimal que representa la altura del Pokémon.
type: Una cadena de caracteres que representa el tipo del Pokémon.
trainer: Una cadena de caracteres que representa el nombre del entrenador del Pokémon.
Además, la clase Pokemon debe tener implementado el método __str__(), que devuelve el nombre del Pokémon.

## Paso 2: Crear la clase Trainer

La clase Trainer debe tener los siguientes atributos:

id: Un número entero que representa el identificador único del entrenador.
first_name: Una cadena de caracteres que representa el nombre del entrenador.
last_name: Una cadena de caracteres que representa el apellido del entrenador.
age: Un número entero que representa la edad del entrenador.
level: Un número entero que representa el nivel del entrenador.
La clase Trainer también debe tener implementado el método __str__(), que devuelve el nombre completo del entrenador (nombre y apellido).

## ¿Cómo realizar las pruebas?

Para realizar las prueba de este repositorio debes ejecutar el siguiente comando

### Linux / Macos
Ejecutar una prueba concreta
~~~ 
python3 -m unittest tester_class.PokemonTester.test_module_exist
~~~
Ejecutar todas las pruebas
~~~ 
python3 -m unittest tester_class.PokemonTester.test_module_exist
~~~

### Windows
Ejecutar una prueba concreta
~~~ 
python -m unittest tester_class.PokemonTester.test_module_exist
~~~
Ejecutar todas las pruebas
~~~ 
python -m unittest tester_class.PokemonTester.test_module_exist
~~~

## Notas adicionales

Para cada clase, asegúrate de que los atributos estén correctamente inicializados en el constructor (__init__()).
Puedes definir métodos adicionales en cada clase si lo consideras necesario.
Después de crear las clases, puedes usarlas para crear instancias de Pokémon y entrenadores según las pruebas proporcionadas.
¡Buena suerte!
