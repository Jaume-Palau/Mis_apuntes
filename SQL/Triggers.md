# Triggers (Disparadores)

| Elemento       | Sintaxis / Valor                        |
| -------------- | --------------------------------------- |
| Crear trigger  | `CREATE TRIGGER nombre_trigger`         |
| Momento        | `BEFORE` | `AFTER`                      |
| Evento         | `INSERT` | `UPDATE` | `DELETE`          |
| Tabla          | `ON nombre_tabla`                       |
| Nivel          | `FOR EACH ROW` *(obligatorio en MySQL)* |
| Bloque         | `BEGIN ... END`                         |
| Acceso a datos | `NEW.columna`, `OLD.columna`            |
| Delimitador    | `DELIMITER` (necesario)                 |
