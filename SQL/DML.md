# DATA MANIPULATION LANGUAGE (DML)

- insert
- update
- delete
- replace

transacciones:

- start transaction
- commit
- rollback
- savepoints
- truncate-> rollback no funciona

| Categoría     | Comando             | Descripción                                                                                              | Ejemplo sencillo                                       |
| ------------- | ------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| DML           | `INSERT`            | Inserta un nuevo registro en una tabla.                                                                  | `INSERT INTO alumno (id, nombre) VALUES (1, 'Ana');`   |
| DML           | `UPDATE`            | Modifica registros existentes (normalmente con `WHERE`).                                                 | `UPDATE alumno SET nombre = 'Juan' WHERE id = 1;`      |
| DML           | `DELETE`            | Borra registros (normalmente con `WHERE`).                                                               | `DELETE FROM alumno WHERE id = 1;`                     |
| DML (MySQL)   | `REPLACE`           | Inserta o reemplaza: si ya existe una fila con la misma clave única/PK, la borra y la vuelve a insertar. | `REPLACE INTO alumno (id, nombre) VALUES (1, 'Luis');` |
| Transacciones | `START TRANSACTION` | Inicia una transacción (los cambios no se guardan hasta `COMMIT`).                                       | `START TRANSACTION;`                                   |
| Transacciones | `COMMIT`            | Confirma y guarda definitivamente los cambios de la transacción.                                         | `COMMIT;`                                              |
| Transacciones | `ROLLBACK`          | Deshace los cambios no confirmados de la transacción.                                                    | `ROLLBACK;`                                            |
| Transacciones | `SAVEPOINT`         | Crea un punto intermedio para poder volver atrás dentro de la transacción.                               | `SAVEPOINT punto1;`                                    |
| Transacciones | `TRUNCATE`          | Vacía la tabla completa. En muchos motores (p. ej. MySQL), no se revierte con `ROLLBACK`.                | `TRUNCATE TABLE alumno;`                               |
