# DATA MANIPULATION LANGUAGE (DML)

**Manipula los datos de las tablas (insertar, modificar, borrar filas).**

| Comando   | Descripción                                                                                                      | Ejemplo                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `INSERT`  | Inserta un nuevo registro en una tabla.                                                                          | `INSERT INTO alumno (id, nombre) VALUES (1, 'Ana');`   |
| `UPDATE`  | Modifica registros existentes (normalmente con `WHERE`).                                                         | `UPDATE alumno SET nombre = 'Juan' WHERE id = 1;`      |
| `DELETE`  | Borra registros (normalmente con `WHERE`).                                                                       | `DELETE FROM alumno WHERE id = 1;`                     |
| `REPLACE` | Inserta o reemplaza: si ya existe una fila con la misma clave única/PK, la borra y la vuelve a insertar (MySQL). | `REPLACE INTO alumno (id, nombre) VALUES (1, 'Luis');` |

