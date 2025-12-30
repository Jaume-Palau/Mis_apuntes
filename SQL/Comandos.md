| Comando                      | Descripción                                                                 | Ejemplo |
|------------------------------|-----------------------------------------------------------------------------|---------|
| SHOW DATABASES;              | Muestra todas las bases de datos                                           | SHOW DATABASES; |
| USE nombre;                  | Selecciona una base de datos                                               | USE sakila; |
| SHOW TABLES;                 | Lista todas las tablas de la base seleccionada                             | SHOW TABLES; |
| DESCRIBE tabla;              | Muestra columnas, tipos y detalles de la tabla                             | DESCRIBE actor; |
| SELECT * FROM tabla;         | Devuelve todos los registros de una tabla                                  | SELECT * FROM film; |
| SELECT col1, col2 FROM tabla;| Devuelve columnas específicas                                               | SELECT first_name, last_name FROM actor; |
| WHERE                        | Filtra resultados por condición                                             | SELECT * FROM film WHERE rating='PG'; |
| ORDER BY                     | Ordena resultados                                                           | SELECT * FROM film ORDER BY title ASC; |
| LIMIT n;                     | Limita el número de resultados                                              | SELECT * FROM film LIMIT 10; |
| COUNT()                      | Cuenta registros                                                            | SELECT COUNT(*) FROM customer; |
| DISTINCT                     | Elimina valores duplicados                                                  | SELECT DISTINCT country FROM customers; |
| INSERT INTO                  | Inserta un nuevo registro                                                   | INSERT INTO cliente (nombre, edad) VALUES ('Ana', 30); |
| UPDATE                       | Modifica registros existentes                                               | UPDATE cliente SET edad=31 WHERE nombre='Ana'; |
| DELETE                       | Elimina registros                                                           | DELETE FROM cliente WHERE edad < 18; |
| CREATE DATABASE nombre;      | Crea una base de datos                                                      | CREATE DATABASE tienda; |
| DROP DATABASE nombre;        | Borra una base de datos completa                                            | DROP DATABASE tienda; |
| CREATE TABLE                 | Crea una tabla nueva                                                        | CREATE TABLE test(id INT, nombre VARCHAR(50)); |
| DROP TABLE nombre;           | Elimina una tabla entera                                                    | DROP TABLE test; |
| AVG()                        | Calcula la media de una columna                                             | SELECT AVG(salary) FROM employees; |
| GROUP BY columna             | Agrupa los resultados por una columna                                       | SELECT country, COUNT(*) FROM customers GROUP BY country; |
| HAVING condición             | Filtra grupos después de usar GROUP BY                                      | SELECT country, COUNT(*) FROM customers GROUP BY country HAVING COUNT(*) > 5; |
| ROLLUP                       | Genera subtotales y total general                                           | SELECT col1, col2, SUM(...) FROM tabla GROUP BY col1, col2 WITH ROLLUP; |
| CASE                         | Condición dentro de un SELECT                                               | CASE WHEN cond THEN val ELSE otro END |
| GROUP_CONCAT(columna)        | Une valores de una columna en un solo texto                                 | GROUP_CONCAT(columna SEPARATOR ', '); |