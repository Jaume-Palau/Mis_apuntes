# Tipos de funciones:

https://www.w3schools.com/sql/sql_ref_mysql.asp

## Funciones de tipo string:

**Estas funciones nos permiten trabajar con cadenas de caracteres y se pueden combianar entre ellas**

| Función    | Descripción                                       | Ejemplo sencillo                       | Resultado    |
| ---------- | ------------------------------------------------- | -------------------------------------- | ------------ |
| `UPPER()`  | Convierte un string a mayúsculas                  | `SELECT UPPER('hola');`                | `HOLA`       |
| `LOWER()`  | Convierte un string a minúsculas                  | `SELECT LOWER('HOLA');`                | `hola`       |
| `LENGTH()` | Devuelve la longitud de una cadena (en bytes)     | `SELECT LENGTH('Hola');`               | `4`          |
| `CONCAT()` | Une cadenas de caracteres                         | `SELECT CONCAT('Hola', ' ', 'Mundo');` | `Hola Mundo` |
| `LTRIM()`  | Elimina espacios en blanco a la izquierda         | `SELECT LTRIM(' Hola');`               | `Hola`       |
| `RTRIM()`  | Elimina espacios en blanco a la derecha           | `SELECT RTRIM('Hola ');`               | `Hola`       |
| `LOCATE()` | Devuelve la posición de una cadena dentro de otra | `SELECT LOCATE('la', 'Hola');`         | `3`          |
| `SUBSTR()` | Extrae parte de un string                         | `SELECT SUBSTR('Hola Mundo', 6, 5);`   | `Mundo`      |
| `REPEAT()` | Repite una cadena un número de veces              | `SELECT REPEAT('Hi', 3);`              | `HiHiHi`     |

## Funciones numéricas:

**Nos permiten hacer operaciones y trabajar con núneros**

| Función             | Descripción                                    | Ejemplo sencillo             | Resultado  |
| ------------------- | ---------------------------------------------- | ---------------------------- | ---------- |
| `ABS()`             | Devuelve el valor absoluto de un número        | `SELECT ABS(-5);`            | `5`        |
| `CEIL()`            | Devuelve el entero más cercano por arriba      | `SELECT CEIL(4.2);`          | `5`        |
| `FLOOR()`           | Devuelve el entero más cercano por abajo       | `SELECT FLOOR(4.8);`         | `4`        |
| `MOD()` / `%`       | Devuelve el resto de una división              | `SELECT MOD(10, 3);`         | `1`        |
| `PI()`              | Devuelve el valor de π                         | `SELECT PI();`               | `3.141593` |
| `POW()` / `POWER()` | Eleva un número a una potencia                 | `SELECT POWER(2, 3);`        | `8`        |
| `SQRT()`            | Devuelve la raíz cuadrada                      | `SELECT SQRT(16);`           | `4`        |
| `RAND()`            | Devuelve un número aleatorio entre 0 y 1       | `SELECT RAND();`             | `0.XXXX`   |
| `ROUND()`           | Redondea un número                             | `SELECT ROUND(4.567, 2);`    | `4.57`     |
| `SIGN()`            | Devuelve el signo del número                   | `SELECT SIGN(-10);`          | `-1`       |
| `TRUNCATE()`        | Trunca un número a N decimales (sin redondear) | `SELECT TRUNCATE(4.567, 2);` | `4.56`     |


## Creacion de Funciones
## Funciones definidas por el usuario (User Defined Functions)

| Elemento               | Descripción                                                       | Ejemplo                                                  |
| ---------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- |
| `CREATE FUNCTION`      | Crea una función definida por el usuario.                         | `CREATE FUNCTION doble(x INT) RETURNS INT RETURN x * 2;` |
| `RETURNS tipo`         | Define el tipo de dato que devuelve la función (**obligatorio**). | `RETURNS DECIMAL(10,2)`                                  |
| `RETURN`               | Devuelve el valor calculado por la función (**obligatorio**).     | `RETURN precio * 1.21;`                                  |
| `IN`                   | Parámetro de entrada (por defecto, no se escribe `IN`).           | `CREATE FUNCTION f(x INT) ...`                           |
| `DETERMINISTIC`        | Siempre devuelve el mismo resultado con los mismos parámetros.    | `DETERMINISTIC`                                          |
| `NOT DETERMINISTIC`    | El resultado puede variar (por ejemplo, usa `RAND()` o fechas).   | `NOT DETERMINISTIC`                                      |
| `NO SQL`               | La función no contiene sentencias SQL.                            | `NO SQL`                                                 |
| `READS SQL DATA`       | La función solo lee datos (`SELECT`).                             | `READS SQL DATA`                                         |
| `CONTAINS SQL`         | La función contiene SQL pero no modifica datos.                   | `CONTAINS SQL`                                           |
| `SQL SECURITY DEFINER` | Se ejecuta con los permisos del creador.                          | `SQL SECURITY DEFINER`                                   |
| `SQL SECURITY INVOKER` | Se ejecuta con los permisos del usuario que la llama.             | `SQL SECURITY INVOKER`                                   |
| `DROP FUNCTION`        | Elimina una función.                                              | `DROP FUNCTION doble;`                                   |

# Plantilla general:
`CREATE` `FUNCTION` nombre_funcion (parametro tipo)  
`RETURNS` tipo_retorno  
[`DETERMINISTIC` | NOT `DETERMINISTIC`]  
[`NO SQL` |` READS SQL DATA` | `CONTAINS SQL`]  
[`SQL` SECURITY DEFINER | `SQL` SECURITY INVOKER]  
`BEGIN`  
    -- declaraciones  
    -- lógica  
    `RETURN` valor;  
`END`;
