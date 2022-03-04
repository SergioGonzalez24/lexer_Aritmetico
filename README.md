# lexer_Aritmetico

Una de las aplicaciones de los autómatas finitos determinísticos es la implementación de reconocedores de tokens en un lenguaje de programación (conocido como Lexer en los compiladores). En esta actividad deberás hacer un programa que reciba como entrada un archivo con una serie de expresiones aritméticas, escritas bajo ciertas reglas, y entregará como salida el conjunto de tokens reconocidos, indicando su tipo, o indicando que hay un error en su formación, es decir, no se respetaron las reglas establecidas.

ntrada

Un archivo tipo texto que contenga una o más expresiones aritméticas, una por renglón.
Los tokens no necesariamente deben estar separados por un blanco, o pueden tener separación de más de un blanco
Por ejemplo:

b=7

a = 32.4 *(-8.6 - b)/       6.1

d = a ^ b // Esto es un comentario

 

Salida

Debe entregar la siguiente salida:

Token

Tipo

b

Variable

=

Asignación

7

Entero

a

Variable

=

Asignación

32.4

Real

*

Multiplicación

(

Paréntesis que abre

-

Resta

8.6

Real

-

Resta

b

Variable

)

Paréntesis que cierra

/

División

6.1

Real

d

Variable

=

Asignación

^

Potencia

b

Variable

// Esto es un comentario

Comentario

 

Reglas de formación de algunos tokens

Variables:
Deben empezar con una letra (mayúscula o minúscula).
Sólo están formadas por letras, números y underscore (‘_’).
Números reales (de punto flotante):
Pueden o no tener parte decimal o entera pero deben contener un punto (e.g. 10. o 10.0 o .10)
Comentarios:
Inician con // y todo lo que sigue hasta que termina el renglón es un comentario
En caso de encontrar un error en una expresión (por ejemplo la secuencia "b?" es inválida, pues no se apega a las reglas de formación de ninguna categoría de tokens), mostrar un mensaje de error. El mensaje de error puede ser general (por ejemplo, "El archivo solicitado contiene errores.") o específico (por ejemplo, al imprimir la tabla de tokens señalar un error en una línea específica).

