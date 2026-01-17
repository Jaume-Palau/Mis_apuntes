# TRANSACTION CONTROL LANGUAGE (TCL)

**Controla las transacciones y cuándo se guardan o deshacen los cambios.**

## Transacciones

| Comando             | Descripción                                                                   | Ejemplo                  |
| ------------------- | ----------------------------------------------------------------------------- | ------------------------ |
| `START TRANSACTION` | Inicia una transacción (los cambios no se guardan hasta `COMMIT`).            | `START TRANSACTION;`     |
| `COMMIT`            | Confirma y guarda definitivamente los cambios de la transacción.              | `COMMIT;`                |
| `ROLLBACK`          | Deshace los cambios no confirmados de la transacción.                         | `ROLLBACK;`              |
| `SAVEPOINT`         | Crea un punto intermedio para poder volver atrás dentro de la transacción.    | `SAVEPOINT punto1;`      |
| `TRUNCATE`          | Vacía la tabla completa (en MySQL normalmente no se revierte con `ROLLBACK`). | `TRUNCATE TABLE alumno;` |