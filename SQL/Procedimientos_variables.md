# Procedimientos almacenados (Stored Procedures. DDL)

**Un procedimiento almacenado es un bloque de código SQL guardado en la base de datos que se puede ejecutar cuando se necesite. Permite reutilizar lógica, automatizar tareas y centralizar operaciones.**

| Comando            | Descripción                                                   | Ejemplo                                                                                |
| ------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `CREATE PROCEDURE` | Crea un procedimiento almacenado.                             | `CREATE PROCEDURE listar_alumnos() BEGIN SELECT * FROM alumno; END;`                   |
| `CALL`             | Ejecuta un procedimiento almacenado.                          | `CALL listar_alumnos();`                                                               |
| `DROP PROCEDURE`   | Elimina un procedimiento almacenado.                          | `DROP PROCEDURE listar_alumnos;`                                                       |
| `ALTER PROCEDURE`  | Modifica propiedades de un procedimiento (limitado en MySQL). | `ALTER PROCEDURE listar_alumnos COMMENT 'Lista alumnos';`                              |
| `IN`               | Parámetro de entrada (recibe valores).                        | `CREATE PROCEDURE p(IN id INT) BEGIN SELECT * FROM alumno WHERE alumno_id = id; END;`  |
| `OUT`              | Parámetro de salida (devuelve valores).                       | `CREATE PROCEDURE p(OUT total INT) BEGIN SELECT COUNT(*) INTO total FROM alumno; END;` |
| `INOUT`            | Parámetro de entrada y salida.                                | `CREATE PROCEDURE p(INOUT x INT) BEGIN SET x = x + 1; END;`                            |


## Variables dentro de procedimientos almacenados

| Tipo de variable  | Descripción                                              | Ejemplo                                   |
| ----------------- | -------------------------------------------------------- | ----------------------------------------- |
| `DECLARE`         | Declara una variable local dentro del procedimiento.     | `DECLARE total INT;`                      |
| `SET`             | Asigna un valor a una variable local.                    | `SET total = 5;`                          |
| `SELECT INTO`     | Asigna el resultado de un `SELECT` a una variable local. | `SELECT COUNT(*) INTO total FROM alumno;` |
| Parámetro `IN`    | Variable de entrada (recibe un valor).                   | `CREATE PROCEDURE p(IN x INT) ...`        |
| Parámetro `OUT`   | Variable de salida (devuelve un valor).                  | `CREATE PROCEDURE p(OUT total INT) ...`   |
| Parámetro `INOUT` | Variable de entrada y salida.                            | `CREATE PROCEDURE p(INOUT x INT) ...`     |


## Variables fuera de procedimientos (variables de sesión / globales)

| Tipo de variable | Descripción                                                  | Ejemplo                                  |
| ---------------- | ------------------------------------------------------------ | ---------------------------------------- |
| `@variable`      | Variable de **sesión** (existe mientras dura la conexión).   | `SET @total = 10;`                       |
| `SELECT INTO`    | Asigna el resultado de un `SELECT` a una variable de sesión. | `SELECT COUNT(*) INTO @num FROM alumno;` |
| `@@variable`     | Variable **del sistema** (configuración de MySQL).           | `SELECT @@autocommit;`                   |
| `SET GLOBAL`     | Modifica una variable global del sistema.                    | `SET GLOBAL max_connections = 200;`      |
| `SET SESSION`    | Modifica una variable solo para la sesión actual.            | `SET SESSION sql_mode = '';`             |
