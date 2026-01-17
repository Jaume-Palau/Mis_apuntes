# DATA DEFINITION LANGUAGE (DDL)

**Define y modifica la estructura de la base de datos (tablas, vistas, índices, constraints).**

## Modificaciones de tablas

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


## Constraints (Restricciones)

| Comando       | Descripción                                                                     | Ejemplo                                                                                  |
| ------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `NOT NULL`    | Obliga a que la columna no pueda tener `NULL`.                                  | `CREATE TABLE alumno (nombre VARCHAR(50) NOT NULL);`                                     |
| `UNIQUE`      | Evita valores duplicados en la columna (o combinación de columnas).             | `CREATE TABLE alumno (email VARCHAR(100) UNIQUE);`                                       |
| `PRIMARY KEY` | Identifica de forma única cada fila (equivale a `UNIQUE` + `NOT NULL`).         | `CREATE TABLE alumno (id INT PRIMARY KEY);`                                              |
| `FOREIGN KEY` | Obliga a que un valor exista en la tabla referenciada (integridad referencial). | `CREATE TABLE matricula (alumno_id INT, FOREIGN KEY (alumno_id) REFERENCES alumno(id));` |
| `CHECK`       | Impone una condición que deben cumplir los valores.                             | `CREATE TABLE alumno (edad INT CHECK (edad >= 0));`                                      |
| `DEFAULT`     | Asigna un valor por defecto si no se indica uno.                                | `CREATE TABLE alumno (activo TINYINT DEFAULT 1);`                                        |

## Views (Vistas)

| Comando                  | Descripción                                 | Ejemplo                                                          |
| ------------------------ | ------------------------------------------- | ---------------------------------------------------------------- |
| `CREATE VIEW`            | Crea una vista (consulta guardada).         | `CREATE VIEW v_alumnos AS SELECT nombre, edad FROM alumno;`      |
| `SELECT` (vista)         | Consulta una vista como si fuera una tabla. | `SELECT * FROM v_alumnos;`                                       |
| `CREATE OR REPLACE VIEW` | Crea la vista o la reemplaza si ya existe.  | `CREATE OR REPLACE VIEW v_alumnos AS SELECT nombre FROM alumno;` |
| `DROP VIEW`              | Elimina una vista.                          | `DROP VIEW v_alumnos;`                                           |