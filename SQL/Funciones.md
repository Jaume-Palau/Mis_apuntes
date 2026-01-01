# Tipos de funciones:

https://www.w3schools.com/sql/sql_ref_mysql.asp

## Funciones de tipo string:

**Estas funciones nos permiten trabajar con cadenas de caracteres y se pueden combianar entre ellas**

| Función | Descripción                                       | Ejemplo sencillo                     | Resultado  |
| ------- | ------------------------------------------------- | ------------------------------------ | ---------- |
| UPPER   | Convierte un string a mayúsculas                  | SELECT UPPER('hola');                | HOLA       |
| LOWER   | Convierte un string a minúsculas                  | SELECT LOWER('HOLA');                | hola       |
| LENGTH  | Devuelve la longitud de una cadena en bytes       | SELECT LENGTH('Hola');               | 4          |
| CONCAT  | Une cadenas de caracteres                         | SELECT CONCAT('Hola', ' ', 'Mundo'); | Hola Mundo |
| LTRIM   | Elimina espacios en blanco a la izquierda         | SELECT LTRIM(' Hola');               | Hola       |
| RTRIM   | Elimina espacios en blanco a la derecha           | SELECT RTRIM('Hola ');               | Hola       |
| LOCATE  | Devuelve la posición de una cadena dentro de otra | SELECT LOCATE('la', 'Hola');         | 3          |
| SUBSTR  | Extrae parte de un string                         | SELECT SUBSTR('Hola Mundo', 6, 5);   | Mundo      |
| REPEAT  | Repite una cadena un número de veces              | SELECT REPEAT('Hi', 3);              | HiHiHi     |

## Funciones numéricas:

**Nos permiten hacer operaciones y trabajar con núneros**

| Función     | Descripción                                    | Ejemplo sencillo           | Resultado |
| ----------- | ---------------------------------------------- | -------------------------- | --------- |
| ABS         | Devuelve el valor absoluto de un número        | SELECT ABS(-5);            | 5         |
| CEIL        | Devuelve el entero más cercano por arriba      | SELECT CEIL(4.2);          | 5         |
| FLOOR       | Devuelve el entero más cercano por abajo       | SELECT FLOOR(4.8);         | 4         |
| MOD (%)     | Devuelve el resto de una división              | SELECT MOD(10, 3);         | 1         |
| PI          | Devuelve el valor de π                         | SELECT PI();               | 3.141593  |
| POW / POWER | Eleva un número a una potencia                 | SELECT POWER(2, 3);        | 8         |
| SQRT        | Devuelve la raíz cuadrada                      | SELECT SQRT(16);           | 4         |
| RAND        | Devuelve un número aleatorio entre 0 y 1       | SELECT RAND();             | 0.XXXX    |
| ROUND       | Redondea un número                             | SELECT ROUND(4.567, 2);    | 4.57      |
| SIGN        | Devuelve el signo del número                   | SELECT SIGN(-10);          | -1        |
| TRUNCATE    | Trunca un número a N decimales (sin redondear) | SELECT TRUNCATE(4.567, 2); | 4.56      |
