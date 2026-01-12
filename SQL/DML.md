# DATA MANIPULATION LANGUAGE (DML)

## DML

| Comando   | Descripción                                                                                                      | Ejemplo                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `INSERT`  | Inserta un nuevo registro en una tabla.                                                                          | `INSERT INTO alumno (id, nombre) VALUES (1, 'Ana');`   |
| `UPDATE`  | Modifica registros existentes (normalmente con `WHERE`).                                                         | `UPDATE alumno SET nombre = 'Juan' WHERE id = 1;`      |
| `DELETE`  | Borra registros (normalmente con `WHERE`).                                                                       | `DELETE FROM alumno WHERE id = 1;`                     |
| `REPLACE` | Inserta o reemplaza: si ya existe una fila con la misma clave única/PK, la borra y la vuelve a insertar (MySQL). | `REPLACE INTO alumno (id, nombre) VALUES (1, 'Luis');` |


## Transacciones

| Comando             | Descripción                                                                   | Ejemplo                  |
| ------------------- | ----------------------------------------------------------------------------- | ------------------------ |
| `START TRANSACTION` | Inicia una transacción (los cambios no se guardan hasta `COMMIT`).            | `START TRANSACTION;`     |
| `COMMIT`            | Confirma y guarda definitivamente los cambios de la transacción.              | `COMMIT;`                |
| `ROLLBACK`          | Deshace los cambios no confirmados de la transacción.                         | `ROLLBACK;`              |
| `SAVEPOINT`         | Crea un punto intermedio para poder volver atrás dentro de la transacción.    | `SAVEPOINT punto1;`      |
| `TRUNCATE`          | Vacía la tabla completa (en MySQL normalmente no se revierte con `ROLLBACK`). | `TRUNCATE TABLE alumno;` |


## Modificaciondes de tablas (DDL)

| Comando         | Descripción                                                                           | Ejemplo                                                                 |
| --------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `ALTER TABLE`   | Modifica la estructura de una tabla (se usa junto con `ADD`, `DROP`, `MODIFY`, etc.). | `ALTER TABLE alumno ADD edad INT;`                                      |
| `ADD`           | Añade una columna (u otros objetos) a una tabla.                                      | `ALTER TABLE alumno ADD edad INT;`                                      |
| `DROP`          | Elimina una columna (u otros objetos) de una tabla.                                   | `ALTER TABLE alumno DROP COLUMN edad;`                                  |
| `MODIFY`        | Cambia el tipo/propiedades de una columna (MySQL).                                    | `ALTER TABLE alumno MODIFY edad TINYINT;`                               |
| `AFTER`         | Coloca una columna después de otra (MySQL).                                           | `ALTER TABLE alumno ADD dni VARCHAR(9) AFTER nombre;`                   |
| `FIRST`         | Coloca una columna como primera (MySQL).                                              | `ALTER TABLE alumno ADD dni VARCHAR(9) FIRST;`                          |
| `CHANGE COLUMN` | Renombra una columna y permite redefinir su tipo (MySQL).                             | `ALTER TABLE alumno CHANGE COLUMN nombre nombre_completo VARCHAR(100);` |
| `RENAME TABLE`  | Renombra una tabla.                                                                   | `RENAME TABLE alumno TO alumnos;`                                       |
| `DROP TABLE`    | Elimina una tabla entera.                                                             | `DROP TABLE alumnos;`                                                   |
